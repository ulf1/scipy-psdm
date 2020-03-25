import numpy as np
import scipy.optimize
import warnings


def luriegold(R: np.ndarray,
              debug: bool = False) -> (np.ndarray, np.ndarray, dict):
    """Lurie-Goldberg Algorithm to adjust a correlation
    matrix to be semipositive definite

    Philip M. Lurie and Matthew S. Goldberg (1998), An Approximate Method
       for Sampling Correlated Random Variables from Partially-Specified
       Distributions, Management Science, Vol 44, No. 2, February 1998, pp
       203-218, URL: http://www.jstor.org/stable/2634496
    """

    # subfunctions
    def xtotril(x: np.ndarray,
                idx: np.ndarray,
                mat: np.ndarray) -> np.ndarray:
        """Create 'L' lower triangular matrix."""
        mat[idx] = x
        return mat

    def xtocorr(x: np.ndarray,
                idx: np.ndarray,
                mat: np.ndarray) -> (np.ndarray, np.ndarray):
        L = xtotril(x, idx, mat)
        C = np.dot(L, L.T)
        return C, L

    def objectivefunc(x: np.ndarray,
                      R: np.ndarray,
                      idx: np.ndarray,
                      mat: np.ndarray) -> float:
        C, _ = xtocorr(x, idx, mat)
        f = np.sum((R - C)**2)
        return f

    def nlcon_diagone(x: np.ndarray,
                      idx: np.ndarray,
                      mat: np.ndarray) -> np.ndarray:
        C, _ = xtocorr(x, idx, mat)
        return np.diag(C) - 1

    # dimension of the correlation matrix
    d = R.shape[0]
    n = int((d**2 + d) / 2.)

    # other arguments
    mat = np.zeros((d, d))  # the lower triangular matrix without values
    idx = np.tril(np.ones((d, d)), k=0) > 0  # boolean matrix
    # idx = np.tril_indices(d,k=0); #row/col ids (same result)

    # start values of the optimization are Ones
    x0 = np.ones(shape=(n, )) / n

    # for each of the k factors, the sum of its d absolute params
    # values has to be less than 1
    condiag = {'type': 'eq', 'args': (idx, mat), 'fun': nlcon_diagone}

    # optimization
    algorithm = 'SLSQP'
    opt = {'disp': False}

    # run the optimization
    results = scipy.optimize.minimize(
        objectivefunc, x0,
        args=(R, idx, mat),
        constraints=[condiag],
        method=algorithm,
        options=opt)

    # Compute Correlation Matrix
    C, L = xtocorr(results.x, idx, mat)

    # Adjust diagonals
    arr_diags = np.diag(C)
    if np.any(arr_diags != 1.0):
        warnings.warn(
            "Some diagonals are not 1.0 and are automatically adjusted.")
        #C[np.diag_indices(len(arr_diags), ndim=2)] = 1.0

    # done
    if debug:
        return C, L, results
    else:
        return C
