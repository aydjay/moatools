from setuptools import setup

setup(name='moatools',
      version='0.1.0',
      packages=['moatools'],
      entry_points={
          'console_scripts': [
              'moatools = tools.__main__:main'
          ]
      },
      )
