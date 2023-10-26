from setuptools import setup, find_packages
from typing import List

def parse_requirements(filename: str) -> List[str]:
    """
    Parse package dependencies from a requirements file.

    Args:
        filename (str): The name of the requirements file.

    Returns:
        List[str]: A list of dependency strings.

    This function reads the given requirements file, strips whitespace, and
    comments (lines starting with '#'), and returns a list of package
    dependencies.

    Example requirements.txt format:
    ```
    package1>=1.0
    package2==2.3
    -e .
    ```
    """
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip() and not line.startswith('#')]
    
    # Check for and remove '-e .' if it exists
    if '-e .' in lines:
        lines.remove('-e .')
    
    return lines

# Package metadata
NAME = 'predictive_maintenance'
VERSION = '0.0.1'
DESCRIPTION = 'Predictive Maintenance of Machines before failure'
URL = 'https://github.com/sudo-deep/predictive_maintenance'
AUTHOR = 'Deepansh Goel'
AUTHOR_EMAIL = 'gl.deepansh@gmail.com'
LICENSE = 'No License'  # Please specify the actual license when you decide

# Read package dependencies from requirements.txt
REQUIREMENTS = parse_requirements('requirements.txt')

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(),
    install_requires=REQUIREMENTS,  # Use the parsed requirements
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',  # Update this when you choose a license
        'Programming Language :: Python :: 3',
    ],
)
