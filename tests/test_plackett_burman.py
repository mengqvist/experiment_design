import unittest
import numpy as np
from plackett_burman import generate_pbdesign

class TestPlackettBurmanDesign(unittest.TestCase):

    def test_valid_inputs(self):
        """Test the function with valid inputs."""
        test_cases = [
            (3, (4, 3)),   # 3 factors result in a 4x3 matrix
            (7, (8, 7)),   # 7 factors result in an 8x7 matrix
            (11, (12, 11)), # 11 factors result in a 12x11 matrix
            (19, (20, 19)), # 19 factors result in a 20x19 matrix
            (23, (24, 23)), # 23 factors result in a 24x23 matrix
        ]
        for num_factors, expected_shape in test_cases:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                self.assertEqual(design.shape, expected_shape)
                self.assertTrue(np.all(np.isin(design, [-1, 1])))

    def test_first_column_all_ones(self):
        """Test that the first column of the design is always all ones."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                self.assertTrue(np.all(design[:, 0] == 1))

    def test_orthogonality(self):
        """Test that columns are orthogonal to each other."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                for i in range(num_factors):
                    for j in range(i+1, num_factors):
                        dot_product = np.dot(design[:, i], design[:, j])
                        self.assertEqual(dot_product, 0)

    def test_balance(self):
        """Test that each column (except the first) has an equal number of 1s and -1s."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                for col in design[:, 1:].T:  # Skip the first column
                    num_ones = np.sum(col == 1)
                    num_minus_ones = np.sum(col == -1)
                    self.assertEqual(num_ones, num_minus_ones)

    def test_invalid_inputs(self):
        """Test the function with invalid inputs."""
        invalid_inputs = [0, -1, 1.5, 'a', None]
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(ValueError):
                    generate_pbdesign(invalid_input)

    def test_large_input(self):
        """Test the function with a large input."""
        num_factors = 100
        design = generate_pbdesign(num_factors)
        expected_rows = 4 * ((num_factors - 1) // 4 + 1)
        self.assertEqual(design.shape, (expected_rows, num_factors))

    def test_edge_cases(self):
        """Test edge cases."""
        # Test with 1 factor
        design = generate_pbdesign(1)
        self.assertEqual(design.shape, (4, 1))
        self.assertTrue(np.all(design == 1))

        # Test with 2 factors
        design = generate_pbdesign(2)
        self.assertEqual(design.shape, (4, 2))
        self.assertTrue(np.all(design[:, 0] == 1))
        self.assertTrue(np.array_equal(design[:, 1], [1, -1, 1, -1]))

    def test_reproducibility(self):
        """Test that the function produces the same output for the same input."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design1 = generate_pbdesign(num_factors)
                design2 = generate_pbdesign(num_factors)
                self.assertTrue(np.array_equal(design1, design2))

    def test_generate_pbdesign_3_factors():
        expected_matrix = np.array([
            [-1., -1.,  1.],
            [ 1., -1., -1.],
            [-1.,  1., -1.],
            [ 1.,  1.,  1.]
        ])
        result = generate_pbdesign(3)
        np.testing.assert_array_equal(result, expected_matrix)

    def test_generate_pbdesign_5_factors():
        expected_matrix = np.array([
            [-1., -1.,  1., -1.,  1.],
            [ 1., -1., -1., -1., -1.],
            [-1.,  1., -1., -1.,  1.],
            [ 1.,  1.,  1., -1., -1.],
            [-1., -1.,  1.,  1., -1.],
            [ 1., -1., -1.,  1.,  1.],
            [-1.,  1., -1.,  1., -1.],
            [ 1.,  1.,  1.,  1.,  1.]
        ])
        result = generate_pbdesign(5)
        np.testing.assert_array_equal(result, expected_matrix)

    def test_generate_pbdesign_12_run_11_factors():
        expected_matrix = np.array([
            [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [-1,  1, -1,  1,  1,  1, -1, -1, -1,  1, -1],
            [-1, -1,  1, -1,  1,  1,  1, -1, -1, -1,  1],
            [ 1, -1, -1,  1, -1,  1,  1,  1, -1, -1, -1],
            [-1,  1, -1, -1,  1, -1,  1,  1,  1, -1, -1],
            [-1, -1,  1, -1, -1,  1, -1,  1,  1,  1, -1],
            [-1, -1, -1,  1, -1, -1,  1, -1,  1,  1,  1],
            [ 1, -1, -1, -1,  1, -1, -1,  1, -1,  1,  1],
            [ 1,  1, -1, -1, -1,  1, -1, -1,  1, -1,  1],
            [ 1,  1,  1, -1, -1, -1,  1, -1, -1,  1, -1],
            [-1,  1,  1,  1, -1, -1, -1,  1, -1, -1,  1],
            [ 1, -1,  1,  1,  1, -1, -1, -1,  1, -1, -1]
        ])
        result = generate_pbdesign(11)
        np.testing.assert_array_equal(result, expected_matrix)

    def test_generate_pbdesign_20_run_19_factors():
        expected_matrix = np.array([
            [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [-1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1],
            [-1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1],
            [ 1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1],
            [ 1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1],
            [-1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1],
            [-1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1],
            [-1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1],
            [-1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1],
            [ 1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1],
            [-1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1],
            [ 1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1],
            [-1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1],
            [ 1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1],
            [ 1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1],
            [ 1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1],
            [ 1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1],
            [-1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1],
            [-1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1],
            [ 1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1]
        ])
        result = generate_pbdesign(19)
        np.testing.assert_array_equal(result, expected_matrix)

if __name__ == '__main__':
    unittest.main()