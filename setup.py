"""
参考
https://deepblue-ts.co.jp/python/pypi-oss-package/
"""
import setuptools
from os import path

version = '1.2'
package_name = "scraping_toolkit"
root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]


setuptools.setup(
    name='scraping_toolkit',
    version=version,
    author='IzumiSatoshi',
    install_requires=_requirements(),
    packages=[package_name]
)
