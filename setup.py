"""Library installer."""

from __future__ import absolute_import, unicode_literals
from os.path import isfile
from sys import version_info

from setuptools import find_packages
from setuptools import setup


def requirements_for(version=None):
    suffix = '-py%s' % version if version is not None else ''
    pip_path = 'requirements%s.pip' % suffix

    if not isfile(pip_path):
        return set(), set()

    requirements = set()
    links = set()
    with open(pip_path) as pip_file:
        for line in pip_file:
            line = line.strip()
            if '#egg=' in line:
                requirement_parts = line.split('#egg=')[-1].split('-')
                version = requirement_parts[-1]
                library = '-'.join(requirement_parts[:-1])
                requirement = '%s==%s' % (library, version)
                requirements.add(requirement)
                links.add(line)
            else:
                requirements.add(line)
    return requirements, links


requirements_general, links_general = requirements_for()
requirements_version, links_version = requirements_for(version_info.major)
install_requires = requirements_general | requirements_version
dependency_links = links_general | links_version

setup(
    name='Gutenberg',
    version='0.5.0',
    author='Clemens Wolff',
    author_email='clemens.wolff+pypi@gmail.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/c-w/Gutenberg',
    download_url='http://pypi.python.org/pypi/Gutenberg',
    license='LICENSE.txt',
    description='Library to interface with Project Gutenberg',
    long_description=open('README.rst').read(),
    dependency_links=dependency_links,
    install_requires=install_requires)
