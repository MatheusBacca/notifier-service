from setuptools import setup, find_packages

setup(
    name="notifier",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "configobj"],
)
