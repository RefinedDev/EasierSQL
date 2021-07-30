import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasierSQL",
    version='0.1.2',
    description="A wrapper for SQLite and MySQL, Most of the queries wrapped into commands for ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/RefinedDev/EasierSQL',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mysql-connector'
    ],
    python_requires='>=3.6',
)
