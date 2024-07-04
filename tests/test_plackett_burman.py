import unittest
import numpy as np
from expdesign import generate_pbdesign

class TestPlackettBurmanDesign(unittest.TestCase):

    def test_valid_inputs(self):
        """Test the function with valid inputs."""
        test_cases = [
            (2, (4, 2)),   # 2 factors result in a 4x2 matrix (next multiple of 4 greater than 2 is 4
            (3, (4, 3)),   # 3 factors result in a 4x3 matrix
            (4, (8, 4)),   # 4 factors result in a 8x4 matrix
            (5, (8, 5)),   # 5 factors result in an 8x5 matrix (next multiple of 4 greater than 5 is 8
            (6, (8, 6)),   # 6 factors result in an 8x6 matrix (next multiple of 4 greater than 6 is 8
            (7, (8, 7)),   # 7 factors result in an 8x7 matrix
            (8, (12, 8)),  # 8 factors result in a 12x8 matrix (next multiple of 4 greater than 8 is 12
            (9, (12, 9)),  # 9 factors result in a 12x9 matrix 
            (10, (12, 10)), # 10 factors result in a 12x10 matrix (next multiple of 4 greater than 10 is 12
            (11, (12, 11)), # 11 factors result in a 12x11 matrix
            (12, (16, 12)), # 12 factors result in a 16x12 matrix (next multiple of 4 greater than 12 is 16
            (13, (16, 13)), # 13 factors result in a 16x13 matrix
            (14, (16, 14)), # 14 factors result in a 16x14 matrix
            (15, (16, 15)), # 15 factors result in a 16x15 matrix
            (16, (20, 16)), # 16 factors result in a 20x16 matrix (next multiple of 4 greater than 16 is 20
            (17, (20, 17)), # 17 factors result in a 20x17 matrix
            (18, (20, 18)), # 18 factors result in a 20x18 matrix (next multiple of 4 greater than 18 is 20
            (19, (20, 19)), # 19 factors result in a 20x19 matrix
            (20, (24, 20)), # 20 factors result in a 24x20 matrix (next multiple of 4 greater than 20 is 24
            (21, (24, 21)), # 21 factors result in a 24x21 matrix
            (22, (24, 22)), # 22 factors result in a 24x22 matrix (next multiple of 4 greater than 22 is 24
            (23, (24, 23)), # 23 factors result in a 24x23 matrix
            (24, (28, 24)), # 24 factors result in a 28x24 matrix (next multiple of 4 greater than 24 is 28
        ]
        for num_factors, expected_shape in test_cases:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                self.assertEqual(design.shape, expected_shape)
                self.assertTrue(np.all(np.isin(design, [-1, 1])))

    def test_first_row_all_ones(self):
        """Test that the first row of the design is always all ones."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                self.assertTrue(np.all(design[0, :] == 1))

    def test_orthogonality(self):
        """Test that columns are orthogonal to each other."""
        for num_factors in [3, 7, 11, 19]:
            with self.subTest(num_factors=num_factors):
                design = generate_pbdesign(num_factors)
                for i in range(num_factors):
                    for j in range(i+1, num_factors):
                        dot_product = np.dot(design[:, i], design[:, j])
                        self.assertEqual(dot_product, 0)

    def test_balance(self):
        """Test that each column (except the first) has an equal number of 1s and -1s."""
        for num_factors in [2, 3, 6, 7, 10, 11, 18, 19]:
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
        num_factors = 16
        design = generate_pbdesign(num_factors)
        expected_rows = 4 * ((num_factors - 1) // 4 + 1)
        self.assertEqual(design.shape, (expected_rows, num_factors))

    def test_reproducibility(self):
        """Test that the function produces the same output for the same input."""
        for num_factors in [3, 7, 11, 19, 23]:
            with self.subTest(num_factors=num_factors):
                design1 = generate_pbdesign(num_factors)
                design2 = generate_pbdesign(num_factors)
                np.testing.assert_array_equal(design1, design2)

    # def test_generate_pbdesign_12_run_11_factors(self):
    #     expected_matrix = np.array([[ 1, -1,  1,  1,  1, -1, -1, -1,  1, -1, -1],
    #                             [-1,  1,  1,  1, -1, -1, -1,  1, -1, -1,  1],
    #                             [ 1,  1,  1, -1, -1, -1,  1, -1, -1,  1, -1],
    #                             [ 1,  1, -1, -1, -1,  1, -1, -1,  1, -1,  1],
    #                             [ 1, -1, -1, -1,  1, -1, -1,  1, -1,  1,  1],
    #                             [-1, -1, -1,  1, -1, -1,  1, -1,  1,  1,  1],
    #                             [-1, -1,  1, -1, -1,  1, -1,  1,  1,  1, -1],
    #                             [-1,  1, -1, -1,  1, -1,  1,  1,  1, -1, -1],
    #                             [ 1, -1, -1,  1, -1,  1,  1,  1, -1, -1, -1],
    #                             [-1, -1,  1, -1,  1,  1,  1, -1, -1, -1,  1],
    #                             [-1,  1, -1,  1,  1,  1, -1, -1, -1,  1, -1],
    #                             [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]])
        
    #     result = generate_pbdesign(11)
    #     np.testing.assert_array_equal(result, expected_matrix)

    # def test_generate_pbdesign_20_run_19_factors(self):
    #     expected_matrix = np.array([[ 1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1],
    #                                 [-1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1],
    #                                 [-1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1],
    #                                 [ 1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1],
    #                                 [ 1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1],
    #                                 [ 1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1],
    #                                 [ 1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1],
    #                                 [-1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1],
    #                                 [ 1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1],
    #                                 [-1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1],
    #                                 [ 1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1],
    #                                 [-1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1],
    #                                 [-1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1],
    #                                 [-1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1],
    #                                 [-1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1],
    #                                 [ 1,  1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1],
    #                                 [ 1, -1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1],
    #                                 [-1, -1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1],
    #                                 [-1,  1, -1, -1,  1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,  1, -1],
    #                                 [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]])
        
    #     result = generate_pbdesign(19)
    #     np.testing.assert_array_equal(result, expected_matrix)

if __name__ == '__main__':
    unittest.main()