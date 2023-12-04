import unittest
from main import example_function

class TestExampleFunction(unittest.TestCase):
    def test_example_function(self):
        result = example_function()
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()