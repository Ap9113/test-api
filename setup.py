import setuptools
from pathlib import Path

# Package meta-data.
PACKAGE_NAME = "hello_world"
VERSION = "0.1.0"
AUTHOR = "Your Name"
AUTHOR_EMAIL = "you@example.com"
URL = "https://github.com/yourusername/hello_world"
LICENSE = "MIT"

# long description from README
here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A simple Hello World CLI tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "hello-world=hello_world.cli:main",
        ],
    },
    install_requires=[],
)
