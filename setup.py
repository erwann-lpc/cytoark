from setuptools import setup, find_packages

setup(
    name="cisca",
    version="0.1.0",
    packages=find_packages(),     #include all packages with init
    include_package_data=True,     
)
