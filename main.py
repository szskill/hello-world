import sys


class ConsoleMessage:
    """Represents a console message that can be printed to the console (stdout by default)."""

    def __init__(self, text):
        """Initializes this console message."""

        self.text = text

    def print(self, newline=True):
        """Prints every character of `self.text` to the console."""

        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()

        if newline:
            sys.stdout.write('\n')

        sys.stdout.flush()


if __name__ == '__main__':
    ConsoleMessage('Hello, World!').print()
