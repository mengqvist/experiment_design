import numpy as np

def assert_matrix(matrix: np.ndarray) -> None:
    """
    Assert that the given matrix is a valid design matrix.
    
    Args:
        matrix (np.ndarray): The matrix to validate.
    """
    assert isinstance(matrix, np.ndarray), 'Input matrix must be a numpy array'
    assert matrix.ndim == 2, 'Input matrix must be 2D'
    assert np.issubdtype(matrix.dtype, np.integer), 'Input matrix must contain integers'
    assert np.all(np.isin(matrix, [-1, 1])), 'Input matrix must contain only -1 and 1'


def is_orthogonal(matrix: np.ndarray) -> bool:
    """
    Check if the given matrix is orthogonal.
    
    Args:
        matrix (np.ndarray): The matrix to check.
        
    Returns:
        bool: True if the matrix is orthogonal, False otherwise.
    """
    assert_matrix(matrix)
    num_columns = matrix.shape[1]
    
    for i in range(num_columns):
        for j in range(i + 1, num_columns):
            # Dot product of columns i and j
            dot_product = np.dot(matrix[:, i], matrix[:, j])
            if not np.isclose(dot_product, 0):
                return False
                
    return True


def is_balanced(matrix: np.ndarray) -> bool:
    """
    Check if the given matrix is balanced.
    
    Args:
        matrix (np.ndarray): The matrix to check.
        
    Returns:
        bool: True if the matrix is balanced, False otherwise.
    """
    assert_matrix(matrix)
    num_rows, num_columns = matrix.shape
    
    for j in range(num_columns):
        column = matrix[:, j]
        count_positive = np.sum(column == 1)
        count_negative = np.sum(column == -1)
        
        if count_positive != count_negative:
            return False

    return True


def calculate_co_occurrence(matrix: np.ndarray) -> np.ndarray:
    """
    Calculate the co-occurrence of each pair of factors in the design matrix.
    
    Args:
        matrix (np.ndarray): The design matrix.
        
    Returns:
        np.ndarray: A matrix representing the co-occurrence of each pair of factors.
    """
    assert_matrix(matrix)

    # Replace -1 with 0 so that the matrix is binary and we calculate the co-occurence of only the positive factors
    binary_matrix = np.where(matrix == -1, 0, matrix)

    num_columns = binary_matrix.shape[1]
    co_occurrence_matrix = np.zeros((num_columns, num_columns))
    
    for i in range(num_columns):
        for j in range(i, num_columns):
            # Dot product of columns i and j, including the diagonal
            dot_product = np.dot(binary_matrix[:, i], binary_matrix[:, j])
            co_occurrence_matrix[i, j] = dot_product
            co_occurrence_matrix[j, i] = dot_product
            
    return co_occurrence_matrix