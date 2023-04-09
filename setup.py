from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    with open('requirements.txt','r') as f:
        lib_list= f.readlines()
    for lib in lib_list:
        requirement_list.append(lib.replace('\n',''))
    if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Ritik",
    author_email="abc@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)


