from setuptools import setup
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="scipy-psdm",
    version=get_version("scipy_psdm/__init__.py"),
    description=(
        "transform an ill-conditioned quadratic matrix to "
        "a positive semidefinite matrix"
    ),
    long_description=read('README.rst'),
    url="http://github.com/ulf1/scipy-psdm",
    author="Ulf Hamster",
    author_email="554c46@gmail.com",
    license="MIT",
    packages=["scipy_psdm"],
    install_requires=[
        "setuptools>=40.0.0",
        "numpy>=1.19.5,<2",
        "scipy>=1.5.4,<2"
    ],
    python_requires=">=3.6",
    zip_safe=True)
