from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='llctools',
      version='0.1beta',
      description='Tool box for analyzing MITgcm Lat-Lon-Cube outputs',
      url='http://github.com/crocha700/llctools',
      author='Cesar B Rocha',
      author_email='crocha@ucsd.edu',
      license='MIT',
      packages=['llctools'],
      install_requires=[
          'numpy',
      ],
      test_suite = 'nose.collector',
      zip_safe=False)
