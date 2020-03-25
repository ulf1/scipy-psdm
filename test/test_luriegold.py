import scipy_psdm as psdm
import numpy as np


def test1():
    mat = [[1.000, -0.948, 0.099, -0.129],
           [-0.948, 1.000, -0.591, 0.239],
           [0.099, -0.591, 1.000, 0.058],
           [-0.129, 0.239, 0.058, 1.000]]
    mat = np.array(mat)
    rho = psdm.luriegold(mat)
    np.testing.assert_allclose(np.diag(rho), 1.0)


def test2():
    mat = [[1.000, -0.948, 0.099, -0.129],
           [-0.948, 1.000, -0.591, 0.239],
           [0.099, -0.591, 1.000, 0.058],
           [-0.129, 0.239, 0.058, 1.000]]
    mat = np.array(mat)
    rho = psdm.luriegold(mat)
    rhoT = np.transpose(rho)
    np.testing.assert_allclose(rho, rhoT)
