# Creating a Python Module Using DevOps

[![Sort Lib](https://github.com/SamWaggoner/python_package_example/actions/workflows/main.yml/badge.svg)](https://github.com/SamWaggoner/python_package_example/actions/workflows/main.yml)
[![.github/workflows/.pre-commit-config.yaml](https://github.com/SamWaggoner/python_package_example/actions/workflows/.pre-commit-config.yaml/badge.svg)](https://github.com/SamWaggoner/python_package_example/actions/workflows/.pre-commit-config.yaml)

## Overview
This repository is designed to reflect the requirements proposed in assignment 6. It will reflect learning a DevOps workflow that will be described here.

## Pre-Commit File
A set of hooks has been specified with a .yml file added. This is known as a pre-commit as it triggers before a commit is made. Pre-commits are run locally before each commmit so it can catch errors faster and prevent them from being committed.
In this case the pre-commit ensures files commited are below a certain size, that the black and flake8 linters run and detects AWS credential prviate keys.
Normally we would require flake8-black, an open-source linter plugin for validating python code for flake8, a style guide enforcement plugin. It allows flake8 to use black, a command line code formatting tool. Normally black would not be able to be run within flake8. However, we avoid the need for this plugin and achieve the same effect by using a precommit instead.
Linters are important for ensuring clean code as they check for errors before they are commited. It is akin to removing mold from cheese before ingestion, it is altogether better to be removed before joining the main body.

## Sorting and Docstrings
This repository implements bubble, quick and inserstion sorting in python ensuring standard practices and is documented with the Google docstring style. This maximizes readability for any developer needing the coding.

## Testing
Pytest is implemented in this repository. Pytest is an open-source framework for creating small tests that can support complex fucntional testing for applications and libraries. Execution is easier with pytest as tests can be invoked quickly to return detailed information on fail.

## Version Accomodation
Additionally, the GitHub actions workflow has been altered to build to three diffferent operating systems: Windows, OSX and Linux for python versions 3.9 and 3.10. This was done using a build backend, in this case setuptools. Additionally we have Twine support. Twine can upload packages to the Python Pakcage index by passing program and metadata files to a web API. It is the official PyPI upload tool which means it can be relied on to be maintained, secure and reliable. Additionally, PyPI functionality has been added to enable Twine.

## Summary
These changes have been made to show the principles of DevOps, which ensure the project can be continued or expanded upon easily regardless of which developer or when the developer joins the project. Standard practices allow other developers to be able to work on existing code easily. Additionally, the use of a standardized docstring style helps with understanding the existing code. The implementation of modern linters allows for cleaner commits, which are critical for the long term heatlh of the project.








The demonstration read.me is included below for internal reference
# DevOps Exercise

This is a skeleton repository for your exercise. 
The goal of this exercise is to implement a Python package for sorting integer 
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Add .pre-commit-config.yml which:  
    1. Limits maximal file size.
    1. Runs the black and flake8 linters.
    1. Detect presence of aws credentials private keys.    
2. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).
3. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
4. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
5. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
6. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
7. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  


Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).



For testing of the sorting algorithms run: python -m pytest 
For linting review of the code run python -m flake8 ; 
To automate linting cleanup with flake 8 and black python -m black .
