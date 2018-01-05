
from setuptools import setup, find_packages

setup(
    name="autherrors",
    version='0.0.1',
    description="The auth system for the gdcapi.",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'cdisutils',
        'Flask==0.10.1',
        'Werkzeug==0.12.2',
    ],
    dependency_links=[
        'git+ssh://git@github.com/NCI-GDC/cdisutils.git@a79409a0ce5071a81c6997d4ed1549c3544fbdcd#egg=cdisutils',
    ],
)
