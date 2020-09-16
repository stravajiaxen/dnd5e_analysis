from setuptools import setup, find_packages

setup(
    name="cbs_survey",
    version="1.0",
    packages=find_packages(),
    requires=["pandas", "matplotlib", "xlrd"]
)
