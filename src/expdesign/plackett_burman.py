import numpy as np
from scipy.linalg import toeplitz, hankel

def generate_pbdesign(num_factors):
    """
    Generate a Plackett-Burman design matrix for the given number of factors.
    
    Args:
    num_factors (int): Number of factors to include in the design.
    
    Returns:
    numpy.ndarray: The Plackett-Burman design matrix.
    """
    if num_factors <= 0:
        raise ValueError('Number of factors must be a positive integer')
    
    # Calculate the number of rows needed
    num_rows = 4 * ((num_factors - 1) // 4 + 1)
    
    # Determine the appropriate base matrix
    if num_rows == 4:
        base_matrix = np.array([[1, 1], [1, -1]])
    elif num_rows == 8:
        base_matrix = np.array([
            [1,  1,  1,  1,  1,  1,  1],
            [1, -1,  1, -1, -1, -1,  1],
            [1,  1, -1,  1, -1, -1, -1],
            [1, -1, -1, -1,  1, -1,  1],
            [1,  1, -1, -1, -1,  1, -1],
            [1, -1,  1, -1,  1,  1, -1],
            [1,  1,  1,  1, -1,  1,  1]
        ])
    elif num_rows == 12:
        base_matrix = np.vstack((
            np.ones((1, 12)),
            np.hstack((
                np.ones((11, 1)),
                toeplitz(
                    [-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1],
                    [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1]
                )
            ))
        ))
    elif num_rows == 20:
        base_matrix = np.vstack((
            np.ones((1, 20)),
            np.hstack((
                np.ones((19, 1)),
                hankel(
                    [-1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1],
                    [1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1]
                )
            ))
        ))
    else:
        raise ValueError(f"Unsupported number of rows: {num_rows}. Must be 4, 8, 12, or 20.")
    
    # Expand the base matrix if necessary
    while base_matrix.shape[0] < num_rows:
        base_matrix = np.vstack((
            np.hstack((base_matrix, base_matrix)),
            np.hstack((base_matrix, -base_matrix))
        ))
    
    # Extract the required number of columns
    design_matrix = base_matrix[:num_rows, :num_factors]
    
    return design_matrix

# Example usage
if __name__ == "__main__":
    num_factors = 7
    pb_design = generate_pbdesign(num_factors)
    print(f"Plackett-Burman design for {num_factors} factors:")
    print(pb_design)