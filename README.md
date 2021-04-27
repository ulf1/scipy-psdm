[![PyPI version](https://badge.fury.io/py/scipy-psdm.svg)](https://badge.fury.io/py/scipy-psdm)
[![scipy-psdm](https://snyk.io/advisor/python/scipy-psdm/badge.svg)](https://snyk.io/advisor/python/scipy-psdm)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ulf1/scipy-psdm.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/scipy-psdm/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ulf1/scipy-psdm.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/scipy-psdm/context:python)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6InVsZjEiLCJyZXBvMSI6InNjaXB5LXBzZG0iLCJpbmNsdWRlTGludCI6ZmFsc2UsImF1dGhvcklkIjoyOTQ1MiwiaWF0IjoxNjE5NTQwMzgwfQ.dV5ygI4BnW7wvTwIJDNl_pMhS3iv00ydDbwmzxNf5o0)](https://www.deepcode.ai/app/gh/ulf1/scipy-psdm/_/dashboard?utm_content=gh%2Fulf1%2Fscipy-psdm)

# scipy-psdm
Transform an ill-conditioned quadratic matrix into a positive semi-definite matrix.

## Installation
The `scipy-psdm` [git repo](http://github.com/ulf1/scipy-psdm) is available as [PyPi package](https://pypi.org/project/scipy-psdm)

```bash
pip install scipy-psdm
```

## Usage
Lurie-Goldberg Algorithm to transform an ill-conditioned quadratic matrix into a positive semi-definite matrix.

```python
import scipy_psdm as psdm
import numpy as np

# A matrix with subjectively set correlations
mat = [[ 1.   , -0.948,  0.099, -0.129],
       [-0.948,  1.   , -0.591,  0.239],
       [ 0.099, -0.591,  1.   ,  0.058],
       [-0.129,  0.239,  0.058,  1.   ]]
mat = np.array(mat)

# Convert to a positive semi-definite matrix
rho = psdm.approximate_correlation_matrix(mat)
print(rho.round(3))
```

Generate correlated random numbers

```python
import scipy_psdm as psdm
X, rho = psdm.randcorr(n_obs=100, n_vars=5, random_state=42)

# compare
import numpy as np
print(rho.round(3))
print(np.corrcoef(X, rowvar=False).round(3))
```

Check the [examples](https://github.com/ulf1/scipy-psdm/tree/master/examples) folder for notebooks.


## Appendix

### Install a virtual environment

```bash
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
pip3 install -r requirements-demo.txt
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

### Python commands

* Start virtual env: `source .venv/bin/activate`
* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest -v`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Clean up 

```bash
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```

### Support
Please [open an issue](https://github.com/ulf1/scipy-psdm/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/scipy-psdm/compare/).

## Contributers
- [@KikeM Enrique Millán Valbuena](https://github.com/KikeM)
