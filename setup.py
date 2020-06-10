from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pykeyboard',
    version='0.1.0',
    author='PyMaster',
    author_email='',
    description='Best Keyboard and Pagination for the Pyrogram Library.',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='telegram pyrogram keyboard bot userbot',
    url='https://github.com/pystorage/pykeyboard',
    packages=['pykeyboard'],
    install_requires=['pyrogram', 'tgcrypto'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
