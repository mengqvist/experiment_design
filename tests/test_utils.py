import unittest
import numpy as np
from src.expdesign.utils import is_orthogonal, is_balanced, calculate_co_occurrence, assert_matrix

class TestUtils(unittest.TestCase):

    def test_is_orthogonal_true(self):
        matrix = np.array([
            [1,  1,  1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1]
        ])
        self.assertTrue(is_orthogonal(matrix))

    def test_is_orthogonal_false(self):
        matrix = np.array([
            [1,  1, -1],
            [-1, 1, -1],
            [-1, -1, 1]
        ])
        self.assertFalse(is_orthogonal(matrix))

    def test_is_balanced_true(self):
        matrix = np.array([
            [1, -1, 1, -1],
            [-1, 1, -1, 1],
            [1, -1, 1, -1],
            [-1, 1, -1, 1]
        ])
        self.assertTrue(is_balanced(matrix))

    def test_is_balanced_false(self):
        matrix = np.array([
            [1, 1, 1, -1],
            [1, -1, -1, 1],
            [1, -1, 1, 1],
            [-1, 1, -1, 1]
        ])
        self.assertFalse(is_balanced(matrix))

    def test_calculate_co_occurrence(self):
        matrix = np.array([
            [1, -1, 1],
            [-1, 1, -1],
            [1, -1, 1],
            [-1, 1, -1]
        ])
        expected_co_occurrence = np.array([
            [2, 0, 2],
            [0, 2, 0],
            [2, 0, 2]
        ])
        np.testing.assert_array_equal(calculate_co_occurrence(matrix), expected_co_occurrence)

    def test_calculate_co_occurrence_non_symmetric(self):
        matrix = np.array([
            [1, 1, -1],
            [1, -1, 1],
            [1, -1, -1],
            [1, 1, 1]
        ])
        expected_co_occurrence = np.array([
            [4, 2, 2],
            [2, 2, 1],
            [2, 1, 2]
        ])
        np.testing.assert_array_equal(calculate_co_occurrence(matrix), expected_co_occurrence)

    def test_assert_matrix_valid(self):
        matrix = np.array([
            [1, -1, 1],
            [-1, 1, -1],
            [1, -1, 1],
            [-1, 1, -1]
        ])
        try:
            assert_matrix(matrix)
        except AssertionError:
            self.fail("assert_matrix() raised AssertionError unexpectedly!")

    def test_assert_matrix_invalid_type(self):
        matrix = [[1, -1, 1], [-1, 1, -1], [1, -1, 1], [-1, 1, -1]]
        with self.assertRaises(ValueError):
            assert_matrix(matrix)

    def test_assert_matrix_invalid_dimensions(self):
        matrix = np.array([1, -1, 1, -1])
        with self.assertRaises(ValueError):
            assert_matrix(matrix)

    def test_assert_matrix_invalid_dtype(self):
        matrix = np.array([
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0]
        ])
        with self.assertRaises(ValueError):
            assert_matrix(matrix)

    def test_assert_matrix_invalid_values(self):
        matrix = np.array([
            [1, 0, 1],
            [-1, 1, -1],
            [1, 2, 1],
            [-1, 1, -1]
        ])
        with self.assertRaises(ValueError):
            assert_matrix(matrix)


if __name__ == '__main__':
    unittest.main()
