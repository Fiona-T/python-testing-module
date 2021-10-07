# file must start with the word test
import unittest
# import function to test
from evens import even_number_of_evens


# test case, extending from unittest
class TestEvens(unittest.TestCase):
    def test_throws_error_if_value_passed_in_is_not_list(self):
        # should raise TypeError calling function with value of 4
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        # should return false if function called with empty list
        self.assertEqual(even_number_of_evens([]), False)
        # should return True if fn called with even list of even numbers
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # should return false if fn called with only one even number
        self.assertEqual(even_number_of_evens([2]), False)
        # should return false if fn called with odd number of odd numbers
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

    # def test_function_returns_True(self):
    #     # testing if calling function with empty list returns True
    #     self.assertTrue(even_number_of_evens([]))


if __name__ == "__main__":
    unittest.main()
