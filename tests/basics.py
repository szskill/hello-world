import unittest
from io import StringIO
from contextlib import redirect_stdout

from main import ConsoleMessage


class Basics(unittest.TestCase):
    def test_constructor(self):
        """Test if the constructor actually works"""

        msg = ConsoleMessage('Test123!@')
        self.assertEqual(msg.text, 'Test123!@')

    def test_print(self):
        """Tests `print` against multiple unicode characters."""

        msg = ConsoleMessage('Test123@!¶§¨«²ÙÚÛÝ')

        stdout_buf = StringIO()
        with redirect_stdout(stdout_buf):
            msg.print()
            msg.print(newline=False)

        self.assertIn('Test123@!¶§¨«²ÙÚÛÝ\nTest123@!¶§¨«²ÙÚÛÝ', stdout_buf.getvalue())


if __name__ == '__main__':
    unittest.main()
