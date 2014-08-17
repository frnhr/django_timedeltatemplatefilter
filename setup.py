import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django_timedeltatemplatefilter",
    version = "0.1.2",
    author = "Fran Hrzenjak",
    author_email = "frnhr@changeset.hr",
    description = ("Format timedelta values nicely in your Django templates."),
    license = "The Unlicense",
    keywords = "django timedelta template filter",
    url = "http://packages.python.org/django_timedeltatemplatefilter",
    packages=find_packages(),
    #long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Utilities",
        "Framework :: Django",
        "License :: Public Domain",
    ],
)
