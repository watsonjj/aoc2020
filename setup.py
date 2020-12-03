from setuptools import setup, find_packages

setup(
    name="aoc2020",
    packages=find_packages(),
    version="1.0.0",
    description="Python solutions for Advent of Code 2020",
    license="MIT",
    install_requires=[
        "scipy",
        "numpy",
        "tqdm>=4.32",
        "numba>=0.50.1",
    ],
    python_requires="~=3.7",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    author="Jason J Watson",
    url="https://github.com/watsonjj/aoc2020",
)
