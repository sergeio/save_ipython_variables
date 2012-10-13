#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='save_ipython_variables',
        version='0.0.3',
        description='A tool for saving your IPython variables to disk.',
        keywords = '',
        url='https://github.com/sergeio/save_ipython_variables',
        author='Sergei Orlov',
        author_email='pypi@sergeiorlov.com',
        license='BSD',
        packages=['save_ipython_variables'],
        install_requires=[''],
        test_suite='tests',
        long_description=read('README.md'),
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python',
        ],
    )

if __name__ == '__main__':
    run_setup()
