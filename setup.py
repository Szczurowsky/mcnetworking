from setuptools import setup
from mcnetworking import __version__

setup(
    name='mcnetworking',
    url='https://github.com/Szczurowsky/mcnetworking/tree/master',
    author='Kamil Szczurowski',
    author_email='kamil@szczurowsky.pl',
    packages=['mcnetworking'],
    version=__version__,
    license='MPL-2.0',
    description='Minecraft Networking Tools - Python implementations of common Minecraft protocols and packets.',
    long_description=open('README.txt').read(),
)