import argparse
import logging
import sys


def greet(name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main() -> None:
    """
    Entry point for the Hello World CLI.
    Parses command-line arguments and prints a greeting.
    """
    parser = argparse.ArgumentParser(
        description="Simple Hello World CLI."
    )
    parser.add_argument(
        "-n", "--name",
        type=str,
        default="World",
        help="Name to greet."
    )
    args = parser.parse_args()

    greeting = greet(args.name)
    print(greeting)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    try:
        main()
    except Exception:
        logging.exception("An unexpected error occurred.")
        sys.exit(1)
