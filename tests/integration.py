from os import remove, path
from glob import glob
from unittest import TestCase, main
import pickle

from save_ipython_variables import save_variable, load_all_variables


####
##
## save_variable
##
####

class _BaseSavingVariableTestCase(TestCase):

    def setUp(self):
        self.remove_all_pickle_files()
        self.execute()

    def tearDown(self):
        self.remove_all_pickle_files()

    def remove_all_pickle_files(cls):
        pkl_files = glob('*.pkl')
        for f in pkl_files:
            remove(f)


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


if __name__ == '__main__':
    main()
