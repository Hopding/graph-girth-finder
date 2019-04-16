import unittest

from main import add

class TestAdd(unittest.TestCase):

  def test(self):
    actual = add(1, 2)
    expected = 3
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()