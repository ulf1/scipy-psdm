import numpy as np

from .luriegold import approximate_correlation_matrix


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


def randcorr(
    n_obs: int, n_vars: int, rho: np.ndarray = None, random_state: int = None
) -> np.ndarray:
    """Generate correlated random numbers"""
    if random_state:
        np.random.seed(random_state)
    # Generate a random correlation matrix if no supplied
    if rho is None:
        mat = illmat(n_vars)
        rho = approximate_correlation_matrix(mat)
    # Generate N(0,1) distributed random numbers
    X = np.random.standard_normal(size=(n_obs, n_vars))
    # Cholesky trick
    X = np.dot(X, np.linalg.cholesky(rho).T)
    return X, rho
