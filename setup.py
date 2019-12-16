from distutils.core import setup
from setuptools import find_packages, setup
import pypandoc

output = pypandoc.convert_file('README.md', 'rst')
print(output)
setup(name='pypfm',
      version='1.4.3',
      long_description=output,
      description='Python pfm files reader',
      author='Wats0ns',
      author_email='Wats0ns@github.com',
      url='https://github.com/Wats0ns/pypfm',
      packages=['pypfm'],
      license='MIT',
      install_requires=['pyzfp', 'numpy'],
      # include_package_data=True,

     )
