from setuptools import find_packages,setup
from typing import List, list

def get_requirements()->List[str]:

    """
    This function will return the list of requirements
    """

    requirement_list:List[str]=[]

    """
    Write code to read requirements.txt file and append each requirements in requirement_list variable.
    """

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