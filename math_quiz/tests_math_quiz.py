import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        # Test if function_C correctly computes the arithmetic operation
        result = function_B(2, 3)
        self.assertEqual(result, 5)  # Assert that the result should be 5 for inputs 2 and 3

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (8, 4, '-', '8 - 4', 4),  # Test subtraction
                (3, 5, '*', '3 * 5', 15),  # Test multiplication
                (10, 2, '/', '10 / 2', 5),  # Test division
            ]
            
            
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
              problem, answer = function_C(num1, num2, operator)
              self.assertEqual(problem, expected_problem)  # Assert that the generated problem is as expected
              self.assertEqual(answer, expected_answer)  # Assert that the computed answer is as expected

if __name__ == "__main__":
    unittest.main()
