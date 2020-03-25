import numpy as np


def illmat(n_dim: int, random_state: int = None) -> np.ndarray:
    """Generate a <n_dim x n_dim> ill-conditioned correlation matrix
    with random coefficients

    Args:
        n_dim (int): Dimension of the matrix
        random_state (int): Seed for RNG

    Return:
        ndarray: <n_dim x n_dim> matrix with 1s as diagonal elements,
            and mirrored random numbers [-1, +1].
    """
    if random_state:
        np.random.seed(random_state)
    tmp = np.random.uniform(low=-1.0, high=1.0, size=(n_dim, n_dim))
    tmp = np.triu(tmp, k=1)
    return np.eye(n_dim) + tmp + tmp.T
