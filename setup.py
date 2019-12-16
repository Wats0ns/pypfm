from distutils.core import setup
from setuptools import find_packages, setup

setup(name='pypfm',
      version='1.4.1',
      description='Python pfm files reader',
      author='Wats0ns',
      author_email='Wats0ns@github.com',
      url='https://github.com/Wats0ns/pypfm',
      packages=['pypfm'],
      install_requires=['pyzfp', 'numpy'],
      include_package_data=True,
     )
