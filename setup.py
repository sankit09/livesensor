from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    requirements_list : List[str] = []

    return requirements_list


setup(
    name= 'sensor',
    version='0.0.1',
    author = 'Ankit Srivastava',
    author_email = "ankitksrivastava09@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()  #['pymongo']
)