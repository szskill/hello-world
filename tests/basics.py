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
        """
        Test if the print method actually works.

        Redirects stdout temporarily and asserts its value.
        """

        msg = ConsoleMessage('Test123!@')

        stdout_buf = StringIO()
        with redirect_stdout(stdout_buf):
            msg.print()
            msg.print(newline=False)

        self.assertIn('Test123!@\nTest123!@', stdout_buf.getvalue())


if __name__ == '__main__':
    unittest.main()
