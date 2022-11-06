from dbm.ndbm import library
from setuptools import find_packages,setup
from typing import List
import os

def get_requirements()->List[str]:

    """
    This function will return the list of requirements
    """
    
    requirement_list:List[str]=[]
    path = os.path.abspath('requirements.txt')

    with open(path) as file:
        libraries = file.readlines()

    for library in libraries:
        if library != '-e .' and library != '-e .\n':
            if library.endswith('\n'):
                requirement_list.append(library[:-1])
            else:
                requirement_list.append(library)

    return requirement_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "subhasish",
    author_email = "subhasishsaha007@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)

# python setup.py install