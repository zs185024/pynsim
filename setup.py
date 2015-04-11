import os
from setuptools import setup
from setuptools import find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "PyNSim",
        version = "0.0.1",
        author = "Stephen Knox",
        author_email = "stephen.knox@manchester.ac.uk",
        description = ("An generic simulator for water resources."),
        license = "GPL v3",
        keywords = "water hydraplatform",
        url = "http://packages.python.org/pynsim",
        packages=find_packages(),
        long_description=read('README'),
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Operating System :: OS Independent',
            'Natural Language :: English',
            'Development Status :: 3 - Alfa',
            'Intended Audience :: Developers',
            "License :: OSI Approved :: GPL v3",
        ],
)
