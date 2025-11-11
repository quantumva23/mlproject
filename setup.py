from setuptools import find_packages, setup
from setuptools import find_packages, setup


from typing import List


def get_requirements(file_path: str) -> List[str]:
    """Return the list of requirements parsed from a requirements file."""
    requirements: List[str] = []
    with open(file_path) as file_obj:
        # strip lines and ignore empty ones
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]

    # editable/install-from-local entries are not needed for pip install
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements


setup(
    name="ml_project",
    version="0.1.0",
    packages=find_packages(),
    author="Vishal Agrahari",
    author_email="va203015@gmail.com",
    install_requires=get_requirements('requirements.txt'),
)