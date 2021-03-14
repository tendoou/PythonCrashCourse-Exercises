import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Create a new employee to test in all methods."""
        self.diego = Employee('diego', 'bletran', 100000)

    def test_give_default_raise(self):
        """Test that a default raise work correctly."""
        self.diego.give_raise()
        self.assertEqual(self.diego.salary, 105000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.diego.give_raise(10000)
        self.assertEqual(self.diego.salary, 110000)


if __name__ == '__main__':
    unittest.main()
