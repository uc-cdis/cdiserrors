
from setuptools import setup, find_packages

setup(
    name="autherrors",
    version='0.0.1',
    description="The auth system for the gdcapi.",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'cdispyutils',
        'Flask==0.10.1',
        'Werkzeug==0.12.2',
    ],
    dependency_links=[
        'git+ssh://git@github.com/uc-cdis/cdis-python-utils.git@754173fe68a4a84f7c214b4444c8d365b54dfd56#egg=cdispyutils',
    ],
)
