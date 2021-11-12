class ConsoleMessage:
    """Represents a console message that can be printed to the console (stdout by default)."""

    def __init__(self, text):
        """Initializes this console message."""

        self.text = text

    def print(self, newline=True):
        """Prints every character of `self.text` to the console."""

        for char in self.text:
            print(char, end='', flush=True)

        if newline:
            print()


if __name__ == '__main__':
    ConsoleMessage('Hello, World!').print()
