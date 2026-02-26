# Hello World Python Project

A simple Python CLI tool that prints "Hello, World!" by default or greets a specified name.

## Features

- Prints "Hello, World!" by default.
- Allows customizing the greeting name via command-line options.
- Clean code structure with proper packaging for easy installation.
- Includes unit tests using pytest.

## Installation

```bash
git clone https://github.com/yourusername/hello_world.git
cd hello_world
pip install .
```

Or install directly from PyPI (once published):

```bash
pip install hello_world
```

## Usage

After installation, use the `hello-world` command:

```bash
hello-world
# Output: Hello, World!

hello-world --name Alice
# Output: Hello, Alice!
```

Alternatively, run as a module:

```bash
python -m hello_world --name Bob
# Output: Hello, Bob!
```

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

## License

This project is licensed under the MIT License.
