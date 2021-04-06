from setuptools import setup, find_packages
from dnfo import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dnfo",
    version=__version__,
    author="Julia A M",
    author_email="jlearning@tuta.io",
    description="a cli tool to display information from the D&D 5e API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudo-julia/dnfo",
    package_dir={"": "dnfo"},
    packages=find_packages(),
    modules=["database_ops", "queries"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Terminals",
        "Typing :: Typed",
    ],
    install_requires=[
        "appdirs>=1.4.4",
        "requests>=2.25.1",
        "rich>=>=9.13.0",
        "pymongo>=3.11.3",
        "GitPython>=3.1.14",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["dnfo = dnfo.__main__:main"]},
    project_urls={
        "Bug Reports": "https://github.com/sudo-julia/dnfo/issues",
        "Source": "https://github.com/sudo-julia/dnfo/issues",
    },
)
