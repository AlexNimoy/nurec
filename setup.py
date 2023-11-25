from setuptools import setup, find_packages

setup(
  name='nurec',
  version='0.1',
  description='Checking data recognition',
  author='Aleksandr Poliakov',
  author_email='backstabe@gmail.com',
  packages=find_packages(),
  install_requires=[line.strip() for line in open("requirements.txt").readlines()],
  package_data={
    'nurec': ['images/*']
  }
)
