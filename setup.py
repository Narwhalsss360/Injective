from setuptools import setup, find_packages

setup(
    name='injective',
    version='0.1.0',
    packages=find_packages(
        where='injective',
        exclude=['*.test.*']
    )
)
