import numpy as np

import scipy_psdm as psdm


def test_unit_diagonal():
    mat = [
        [1.000, -0.948, 0.099, -0.129],
        [-0.948, 1.000, -0.591, 0.239],
        [0.099, -0.591, 1.000, 0.058],
        [-0.129, 0.239, 0.058, 1.000],
    ]
    mat = np.array(mat)
    rho = psdm.approximate_correlation_matrix(mat)
    np.testing.assert_allclose(np.diag(rho), 1.0)


def test_symmetry():
    mat = [
        [1.000, -0.948, 0.099, -0.129],
        [-0.948, 1.000, -0.591, 0.239],
        [0.099, -0.591, 1.000, 0.058],
        [-0.129, 0.239, 0.058, 1.000],
    ]
    mat = np.array(mat)
    rho = psdm.approximate_correlation_matrix(mat)
    rhoT = np.transpose(rho)
    np.testing.assert_allclose(rho, rhoT)


def test_cholesky():
    mat = [
        [1.000, -0.948, 0.099, -0.129],
        [-0.948, 1.000, -0.591, 0.239],
        [0.099, -0.591, 1.000, 0.058],
        [-0.129, 0.239, 0.058, 1.000],
    ]
    mat = np.array(mat)
    rho = psdm.approximate_correlation_matrix(mat)
    # try to run cholesky decomposition.
    # numpy will throw an exception if the matrix is ill-conditioned
    try:
        np.linalg.cholesky(rho)
    except np.linalg.LinAlgError:
        assert False


def test_determinant_positive():
    mat = [
        [1.000, -0.948, 0.099, -0.129],
        [-0.948, 1.000, -0.591, 0.239],
        [0.099, -0.591, 1.000, 0.058],
        [-0.129, 0.239, 0.058, 1.000],
    ]
    mat = np.array(mat)
    rho = psdm.approximate_correlation_matrix(mat)
    # matrix determinant must be greater than 0
    assert np.linalg.det(rho) > 0.0


def test_integration():
    mat = psdm.illmat(n_dim=10, random_state=42)
    rho = psdm.approximate_correlation_matrix(mat)
    # test 1
    np.testing.assert_allclose(np.diag(rho), 1.0)
    # test 2
    rhoT = np.transpose(rho)
    np.testing.assert_allclose(rho, rhoT)
    # test 3
    try:
        np.linalg.cholesky(rho)
    except np.linalg.LinAlgError:
        assert False
    # test 4
    assert np.linalg.det(rho) > 0.0
