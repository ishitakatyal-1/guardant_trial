import os
from django.test import TestCase

# Create your tests here.
from arithmetic_operations.helper_functions import HelperClass

EMPTY_LIST_VALS = ['#', None, '', ' ', "", " ", [], {}]
BASE_DIR = os.getcwd()

test_file_dir = os.path.join(BASE_DIR, 'arithmetic_operations')
test_file = os.path.join(test_file_dir, 'test_cases.txt')


class AuxillaryTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_cases = []
        with open(test_file, 'r') as fopen:
            f_contents = fopen.read()

        for i in f_contents.split('\n'):
            if i not in EMPTY_LIST_VALS and i[0] != '#':
                cls.test_cases.append(i)

        cls.len_test_cases = len(cls.test_cases)
        cls.auxy_fn_cls = HelperClass()

    @classmethod
    def setup(cls):
        pass

    @classmethod
    def test_check_positional_elements(cls):

        for i in range(cls.len_test_cases):
            if i == 0:
                cls.assertEqual(cls.auxy_fn_cls.check_positional_elements(cls.test_cases[i]), {
                                'success': True, 'message': 'Positional elements are all ok.'})
            elif i < 3:
                cls.assertEqual(cls.auxy_fn_cls.check_positional_elements(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][0] + ' cannot be in first place.'})
            elif i < 5:
                cls.assertEqual(cls.auxy_fn_cls.check_positional_elements(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][-1] + ' cannot be in last place.'})
            elif i < 9:
                cls.assertEqual(cls.auxy_fn_cls.check_positional_elements(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][0] + ' cannot be in first place.'})
            else:
                cls.assertEqual(cls.auxy_fn_cls.check_positional_elements(cls.test_cases[i]), {
                                'success': True, 'message': 'Positional elements are all ok.'})

    @classmethod
    def test_check_simultaneous_occurrence(cls):

        for i in range(cls.len_test_cases-1):
            if i < 9:
                cls.assertEqual(cls.auxy_fn_cls.check_simultaneous_occurrences(cls.test_cases[i]), {
                                'success': True, 'message': 'Simultaneous occurrence for operation +/- check passed.'})
            elif i < 11:
                cls.assertEqual(cls.auxy_fn_cls.check_simultaneous_occurrences(cls.test_cases[i]), {
                                'success': False, 'message': 'Arithmetical operations: ' + cls.test_cases[i] + ' cannot occur simultaneously.'})
            elif i < 13:
                cls.assertEqual(cls.auxy_fn_cls.check_simultaneous_occurrences(cls.test_cases[i]), {
                                'success': False, 'message': 'Arithmetical operations: ' + cls.test_cases[i] + ' cannot occur simultaneously.'})

    @classmethod
    def test_check_for_valid_chars(cls):

        for i in range(cls.len_test_cases-1):
            if i < 15:
                cls.assertEqual(cls.auxy_fn_cls.check_for_valid_chars(cls.test_cases[i]), {
                                'success': True, 'message': 'All characters are valid.'})
            else:
                cls.assertEqual(cls.auxy_fn_cls.check_for_valid_chars(cls.test_cases[i]), {
                                'success': False, 'message': 'Invalid characters sent. Only +/- and digits 0-9 are allowed.'})

    @classmethod
    def test_valid_check(cls):

        len_test_cases = len(cls.test_cases)
        for i in range(len_test_cases):
            if i == 0:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': True, 'message': 'Valid input string.'})
            elif i < 3:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][0] + ' cannot be in first place.'})
            elif i < 5:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][-1] + ' cannot be in last place.'})
            elif i < 9:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': False, 'message': 'Operation of ' + cls.test_cases[i][0] + ' cannot be in first place.'})
            elif i in [9, 11, 13]:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': False, 'message': 'Arithmetical operations: ' + cls.test_cases[i] + ' cannot occur simultaneously.'})
            elif i in [10, 12, 14]:
                cls.assertEqual(cls.auxy_fn_cls.valid_check(cls.test_cases[i]), {
                                'success': False, 'message': 'Arithmetical operations: ' + cls.test_cases[i] + ' cannot occur simultaneously.'})
            else:
                cls.assertEqual(cls.auxy_fn_cls.check_for_valid_chars(cls.test_cases[i]), {
                                'success': False, 'message': 'Invalid characters sent. Only +/- and digits 0-9 are allowed.'})

    @classmethod
    def test_compute_result(cls):

        test_result = cls.auxy_fn_cls.compute_result(cls.test_cases[0])
        cls.assertEqual(test_result, 162)

    @classmethod
    def test_call(cls):

        test_call_result = cls.auxy_fn_cls.__call__(cls.test_cases[0])['value']
        cls.assertEqual(test_call_result, 162)
