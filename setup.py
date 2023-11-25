from setuptools import setup, Extension
from Cython.Build import cythonize

# Define extensions
extensions = [
    # Extension for the pure Cython implementation
    Extension(
        "utils",
        sources=["utils.pyx"],
    ),
    # Extension for the C implementation with Cython interface
    Extension(
        "utils_interface",
        sources=["utils_interface.pyx", "src/utils.c"],
    ),
]

setup(
    name='Sorting Extensions',
    ext_modules=cythonize(extensions)
)
