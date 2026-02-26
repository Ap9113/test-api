import pytest
from hello_world.cli import greet


def test_greet_default():
    assert greet("World") == "Hello, World!"


def test_greet_custom():
    name = "Alice"
    assert greet(name) == f"Hello, {name}!"

# You can add more tests here as needed
