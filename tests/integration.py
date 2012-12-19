from os import remove, path
from glob import glob
from unittest import TestCase, main
import pickle

from save_ipython_variables import (
    load_all_variables,
    load_variables,
    save_variable,
)


def remove_all_pickle_files():
    pkl_files = glob('test_*.pkl')
    for f in pkl_files:
        remove(f)
    if path.exists('saved_var_names.pkl'):
        remove('saved_var_names.pkl')


####
##
## save_variable
##
####

class _BaseSavingVariableTestCase(TestCase):

    def setUp(self):
        remove_all_pickle_files()
        self.execute()

    def tearDown(self):
        remove_all_pickle_files()


class WhenSavingVariableWithAutoLoad(_BaseSavingVariableTestCase):

    def execute(self):
        save_variable('test_saving_variable_var_1', 3)
        save_variable('test_saving_variable_var_2', 5)

    def test_variable_1_exists_on_disk(self):
        self.assertTrue(path.exists('test_saving_variable_var_1.pkl'))

    def test_variable_2_exists_on_disk(self):
        self.assertTrue(path.exists('test_saving_variable_var_2.pkl'))

    def test_saved_var_names_exists_on_disk(self):
        self.assertTrue(path.exists('saved_var_names.pkl'))

    def test_variable_3_does_not_exist_on_disk(self):
        self.assertFalse(path.exists('test_saving_variable_var_3.pkl'))

    def test_value_of_var_1(self):
        var_1 = pickle.load(open('test_saving_variable_var_1.pkl', 'rb'))
        self.assertEqual(var_1, 3)

    def test_value_of_var_2(self):
        var_2 = pickle.load(open('test_saving_variable_var_2.pkl', 'rb'))
        self.assertEqual(var_2, 5)

    def test_value_saved_var_names(self):
        variable_set = pickle.load(open('saved_var_names.pkl', 'rb'))
        self.assertEqual(
            variable_set,
            set(('test_saving_variable_var_1', 'test_saving_variable_var_2')),
        )


class WhenSavingVariableWithoutAutoLoad(_BaseSavingVariableTestCase):

    def execute(self):
        save_variable('test_saving_variable_var_1', 3, auto_load=False)
        save_variable('test_saving_variable_var_2', 5, auto_load=False)

    def test_saved_var_names_does_not_exist_on_disk(self):
        self.assertFalse(path.exists('saved_var_names.pkl'))

    def test_variable_1_exists_on_disk(self):
        self.assertTrue(path.exists('test_saving_variable_var_1.pkl'))

    def test_variable_2_exists_on_disk(self):
        self.assertTrue(path.exists('test_saving_variable_var_2.pkl'))


####
##
## load_all_variables
##
####

class _BaseLoadingAllVariablesTestCase(TestCase):

    def setUp(self):
        remove_all_pickle_files()
        self.configure()
        self.execute()


class WhenLoadingAllVariablesNoArgs(_BaseLoadingAllVariablesTestCase):

    def configure(self):
        pickle.dump(5, open('test_loading_variable_var_1.pkl', 'wb'))
        pickle.dump(
            set(['test_loading_variable_var_1']),
            open('saved_var_names.pkl', 'wb'),
        )

    def execute(self):
        load_all_variables()

    def tearDown(self):
        remove_all_pickle_files()
        del __builtins__['saved_var_names']

    def test_loads_var_1(self):
        self.assertEqual(test_loading_variable_var_1, 5)

    def test_loads_saved_var_names_into_builtins(self):
        self.assertTrue('saved_var_names' in __builtins__)

    def test_saved_var_names_has_correct_value(self):
        self.assertEqual(
            saved_var_names,
            set(['test_loading_variable_var_1']),
        )


class WhenLoadingAllVariablesWithArgs(_BaseLoadingAllVariablesTestCase):

    def configure(self):
        pickle.dump(5, open('test_loading_variable_var_1.pkl', 'wb'))
        pickle.dump(6, open('test_loading_variable_var_2.pkl', 'wb'))
        pickle.dump(
            set(['test_loading_variable_var_1']),
            open('saved_var_names.pkl', 'wb'),
        )

    def execute(self):
        load_all_variables(['test_loading_variable_var_1'])

    def tearDown(self):
        remove_all_pickle_files()

    def test_loads_var_1(self):
        self.assertEqual(test_loading_variable_var_1, 5)

    def test_loads_saved_var_names(self):
        self.assertFalse('saved_var_names' in __builtins__)

    def test_does_not_load_var_2(self):
        self.assertRaises(NameError, lambda: test_loading_variable_var_2)

    def test_var_2_not_in_builtins(self):
        self.assertFalse('test_loading_variable_var_2' in __builtins__)


class WhenLoadingAllVariablesNothingToLoad(_BaseLoadingAllVariablesTestCase):

    def configure(self):
        pass

    def execute(self):
        pass

    def tearDown(self):
        remove_all_pickle_files()

    def test_raises_IOError(self):
        self.assertRaises(IOError, load_all_variables)

####
##
## load_variables
##
####


class WhenLoadingVariables(WhenLoadingAllVariablesWithArgs):
    """Test is same as the parent class, but calls the more natural sounding
    name in this context.

    """
    def execute(self):
        load_variables(['test_loading_variable_var_1'])


if __name__ == '__main__':
    main()
