import setuptools


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name='scraping_toolkit',
    version='1.0',
    author='IzumiSatoshi',
    packages=_requires_from_file('requirements.txt')
)
