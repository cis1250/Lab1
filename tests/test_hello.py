import io
import sys
import unittest
from hello import main

class TestHello(unittest.TestCase):
    def test_output_contains_hello(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        # Flexible: student can add more prints
        self.assertIn("Hello", output)

if __name__ == "__main__":
    unittest.main()
