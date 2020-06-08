import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version_number = "0.0.4"

setuptools.setup(
    name="subutai-bazaar",
    version=version_number,
    author="crioto",
    author_email="msavochkin@optdyn.com",
    description="Library for Subutai Bazaar REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crioto/subutai-bazaar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
