from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(name='csvtsdb',
    version='0.1.1',
    description='CSV-backed timeseries database usable standalone or as a Twisted resource',
    long_description=readme,
    url='http://github.com/anotherkamila/csvtsdb',
    author='Kamila Součková',
    author_email='kamisouckova@gmail.com',
    license='MIT',
    packages=['csvtsdb'],
    install_requires=[
        'twisted',
        'klein',
    ]
)
