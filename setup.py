
from setuptools import setup, find_packages

setup(
    name="cdiserrors",
    version='0.0.1',
    description="The auth system for the gdcapi.",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'cdislogging',
        'Flask==0.10.1',
        'Werkzeug==0.12.2',
    ],
    dependency_links=[
        'git+https://git@github.com/uc-cdis/cdislogging.git@0.0.2#egg=cdislogging',
    ],
)
