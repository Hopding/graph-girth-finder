import unittest

from textwrap import dedent
from inspect import isclass

from utils import parse_adjacency_matrix, InvalidMatrixCellError, InvalidMatrixShapeError, SelfLoopInMatrixError, NonsymmetricMatrixError

test_cases = [
  { 
    'matrix': dedent("""
      0 1 0
      1 0 1
      0 1 0
    """),
    'result': [
      [0, 1, 0],
      [1, 0, 1],
      [0, 1, 0],
    ]
  },
  { 
    'matrix': dedent("""
      1 0 x
      0 1 0
      1 0 1
    """),
    # 'result': InvalidMatrixCellError
    'result': InvalidMatrixShapeError
  }
]

class TestParseAdjacencyMatrix(unittest.TestCase):
  pass


def test_generator(matrix, result):
  def test(self):
    if isclass(result) and issubclass(result, Exception):
      self.assertRaises(result, parse_adjacency_matrix, matrix)
    else:
      actual = parse_adjacency_matrix(matrix)
      expected = result
      self.assertEqual(actual, expected)
  return test


if __name__ == '__main__':
  for (idx, test_case) in enumerate(test_cases):
    matrix = test_case['matrix']
    result = test_case['result']
    test_name = f'test_{idx}'
    test = test_generator(matrix, result)
    setattr(TestParseAdjacencyMatrix, test_name, test)
  unittest.main()