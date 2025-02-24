#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='birdbrain-python-library-2',
    version='0.9.4',
    license='LGPL-3.0-only',
    description='Rewritten Python Library for Birdbrain Technologies Hummingbird Bit and Finch 2',
    long_description='{}\n{}'.format(
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')),
    ),
    author='Frank Morton',
    author_email='fmorton@base2inc.com',
    url='https://github.com/fmorton/BirdBrain-Python-Library-2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        #'Documentation': 'https://BirdBrain-Python-Library-2.readthedocs.io/',
        #'Changelog': 'https://BirdBrain-Python-Library-2.readthedocs.io/en/latest/changelog.html',
        #'Issue Tracker': 'https://github.com/fmorton/BirdBrain-Python-Library-2/issues',
        'Hummingbird Docs': 'https://learn.birdbraintechnologies.com/hummingbirdbit/python/library/',
        'Finch Docs': 'https://learn.birdbraintechnologies.com/finch/python/library/',
        'Source': 'https://github.com/fmorton/BirdBrain-Python-Library-2',
        'Issue Tracker': 'https://github.com/fmorton/BirdBrain-Python-Library-2/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.7',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'birdbrain-python-library-2 = birdbrain_python_library_2.cli:main',
        ]
    },
)
