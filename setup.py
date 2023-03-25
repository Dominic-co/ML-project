from setuptools import find_packages,setup
from typing import List

HYOEN_E_DOT = 'e'
def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","")for req in requirement]

        if HYOEN_E_DOT in requirement:
           requirement.remove(HYOEN_E_DOT)

setup(
    name='ML-Project',
    version='0.0.1',
    author='Aniket',
    author_email='aniket9890patil@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirement.txt')
)