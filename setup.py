from setuptools import setup, find_packages
import os

requires = [
    'elasticsearch>=5.0.0,<6.0.0',
]

setup(
    name = 'es-test',
    version = '0.0.1',
    install_requires = requires,
)
