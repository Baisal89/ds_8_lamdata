"""
lambdata - a collection of data science helper functions for lambda school
"""

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="lamdata-DS8",
    version = "0.1.1",
    author = "Baisal",
    description = "a collection of data science helpre functions",
    long_description = LONG_DESCRIPTION,
    long_descrioption_content_type="text/markdown",
    url="https://lambdaschool.com/courses/data-science",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires = REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Aproved :: MIT License",
    "Operating System :: OS Independent ",
    ]
    )
