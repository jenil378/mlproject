from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters from each requirement
        requirements = [req.strip() for req in requirements]
        # Remove '-e .' if it exists
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Jenil',
    author_email='vekariyajenil23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)
