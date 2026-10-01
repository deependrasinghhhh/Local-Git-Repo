import unittest

from sample_module import add


class AddTests(unittest.TestCase):
    def test_adds_positive_numbers(self):
        self.assertEqual(add(4, 7), 11)

    def test_adds_negative_numbers(self):
        self.assertEqual(add(-4, -7), -11)

    def test_adds_strings(self):
        self.assertEqual(add("sample", " tests"), "sample tests")


if __name__ == "__main__":
    unittest.main()