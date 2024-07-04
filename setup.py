from setuptools import setup

setup(
    name='WebTesting',
    version='0.0.1',
    packages=['web_tests'],
    install_requires=[
        'pytest',
        'selenium',
        'webdriver-manager'
    ],
)
