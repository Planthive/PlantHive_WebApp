import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PlantHiveWebApp",
    version = "3.0.1",
    author = "PlantHive",
    author_email = "tino.dornbusch@mail.com",
    description = ("PlantHive Web Interface"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "https://github.com/Planthive/PlantHive_WebApp",
    # package_dir = {'bin/modules/'},include_package_data=True,
    install_requires=[
            'mongodb',
            'django',
            'djongo',
            'djangorestframework',
            'markdown',
            'django-filter',
            'matplotlib'],
    packages=find_packages(include=['webide']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
