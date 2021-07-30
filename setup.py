import setuptools
import subprocess

__version__ = subprocess.run(['git','describe','--tags'],stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
assert '.' in __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasierSQL",
    version=__version__,
    description="A wrapper for SQLite, Most of the queries wrapped into commands for ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/RefinedDev/EasierSQL',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
