

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecoaliface",
    version="0.3.0",
    author="Mateusz Korniak",    
    author_email="matkor@github",
    description="Interface to eSterownik.pl eCoal water boiler controller.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matkor/ecoaliface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
)
