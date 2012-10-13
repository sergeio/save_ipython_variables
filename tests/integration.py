from os import remove, path
from glob import glob
from unittest import TestCase, main
import pickle

from save_ipython_variables import save_variable, load_all_variables


def remove_all_pickle_files():
    pkl_files = glob('*.pkl')
    for f in pkl_files:
        remove(f)

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
        save_variable('saving_variable_test_var_1', 3)
        save_variable('saving_variable_test_var_2', 5)

    def test_variable_1_exists_on_disk(self):
        self.assertTrue(path.exists('saving_variable_test_var_1.pkl'))

    def test_variable_2_exists_on_disk(self):
        self.assertTrue(path.exists('saving_variable_test_var_2.pkl'))


    def test_auto_load_var_names_exists_on_disk(self):
        self.assertTrue(path.exists('auto_load_var_names.pkl'))

    def test_variable_3_does_not_exist_on_disk(self):
        self.assertFalse(path.exists('saving_variable_test_var_3.pkl'))

    def test_value_of_var_1(self):
        var_1 = pickle.load(open('saving_variable_test_var_1.pkl', 'rb'))
        self.assertEqual(var_1, 3)

    def test_value_of_var_2(self):
        var_2 = pickle.load(open('saving_variable_test_var_2.pkl', 'rb'))
        self.assertEqual(var_2, 5)

    def test_value_auto_load_var_names(self):
        variable_set = pickle.load(open('auto_load_var_names.pkl', 'rb'))
        self.assertEqual(
            variable_set,
            set(('saving_variable_test_var_1', 'saving_variable_test_var_2')),
        )


class WhenSavingVariableWithoutAutoLoad(_BaseSavingVariableTestCase):

    def execute(self):
        save_variable('saving_variable_test_var_1', 3, auto_load=False)
        save_variable('saving_variable_test_var_2', 5, auto_load=False)

    def test_auto_load_var_names_does_not_exist_on_disk(self):
        self.assertFalse(path.exists('auto_load_var_names.pkl'))

    def test_variable_1_exists_on_disk(self):
        self.assertTrue(path.exists('saving_variable_test_var_1.pkl'))

    def test_variable_2_exists_on_disk(self):
        self.assertTrue(path.exists('saving_variable_test_var_2.pkl'))


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
        pickle.dump(5, open('loading_variable_test_var_1.pkl', 'wb'))
        pickle.dump(
            set(['loading_variable_test_var_1']),
            open('auto_load_var_names.pkl', 'wb'),
        )

    def execute(self):
        load_all_variables()

    def tearDown(self):
        remove_all_pickle_files()
        del __builtins__['auto_load_var_names']

    def test_loads_var_1(self):
        self.assertEqual(loading_variable_test_var_1, 5)

    def test_loads_auto_load_var_names_into_builtins(self):
        self.assertTrue('auto_load_var_names' in __builtins__)

    def test_auto_load_var_names_has_correct_value(self):
        self.assertEqual(
            auto_load_var_names,
            set(['loading_variable_test_var_1']),
        )


class WhenLoadingAllVariablesWithArgs(_BaseLoadingAllVariablesTestCase):

    def configure(self):
        pickle.dump(5, open('loading_variable_test_var_1.pkl', 'wb'))
        pickle.dump(6, open('loading_variable_test_var_2.pkl', 'wb'))
        pickle.dump(
            set(['loading_variable_test_var_1']),
            open('auto_load_var_names.pkl', 'wb'),
        )

    def execute(self):
        load_all_variables(['loading_variable_test_var_1'])

    def tearDown(self):
        remove_all_pickle_files()

    def test_loads_var_1(self):
        self.assertEqual(loading_variable_test_var_1, 5)

    def test_loads_auto_load_var_names(self):
        self.assertFalse('auto_load_var_names' in __builtins__)

    def test_does_not_load_var_2(self):
        self.assertRaises(NameError, lambda: loading_variable_test_var_2)

    def test_var_2_not_in_builtins(self):
        self.assertFalse('loading_variable_test_var_2' in __builtins__)


class WhenLoadingAllVariablesNothingToLoad(_BaseLoadingAllVariablesTestCase):

    def configure(self):
        pass

    def execute(self):
        pass

    def tearDown(self):
        remove_all_pickle_files()

    def test_raises_IOError(self):
        self.assertRaises(IOError, load_all_variables)


if __name__ == '__main__':
    main()
