import unittest

from textwrap import dedent
from inspect import isclass

from matrix import parse_adjacency_matrix, InvalidMatrixCellError, InvalidMatrixShapeError, SelfLoopInMatrixError, NonsymmetricMatrixError

test_cases = [
    [dedent("""
      0 1 0
      1 0 1
      0 1 0
    """), [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]],

    [dedent("""
      0 1 0 0 1 0 0 0
      1 0 0 0 0 1 0 0
      0 0 0 1 0 1 1 0
      0 0 1 0 0 0 1 1
      1 0 0 0 0 0 0 0
      0 1 1 0 0 0 1 0
      0 0 1 1 0 1 0 1
      0 0 0 1 0 0 1 0
    """), [
        [0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0]
    ]],

    [dedent("""
      1 0 x
      0 1 0
      1 0 1
    """), InvalidMatrixCellError
     ],

    [dedent("""
      1 0 1
      0 1 0 0
      1 0 1
    """), InvalidMatrixShapeError
     ],

    [dedent("""
      1 0 1
      0 1 0
      1 0 1
      0
    """), InvalidMatrixShapeError
     ],

    [dedent("""
      1 0 1
      0 1 0
      1 0 1
    """), SelfLoopInMatrixError
     ],

    [dedent("""
      1
    """), SelfLoopInMatrixError
     ],

    [dedent("""
      0 1 0
      0 0 1
      0 1 0
    """), NonsymmetricMatrixError
     ],
]


class TestParseAdjacencyMatrix(unittest.TestCase):
    pass


def create_success_test(matrix, result):
    def test(self):
        actual = parse_adjacency_matrix(matrix)
        expected = result
        self.assertEqual(actual, expected)
    return test


def create_error_test(matrix, result):
    def test(self):
        self.assertRaises(result, parse_adjacency_matrix, matrix)
    return test


if __name__ == '__main__':
    for (idx, test_case) in enumerate(test_cases):
        matrix = test_case[0]
        result = test_case[1]
        is_error_test = isclass(result) and issubclass(result, Exception)

        if is_error_test:
            test_name = f'test_{result.__name__}_{idx}'
            test = create_error_test(matrix, result)
        else:
            test_name = f'test_{idx}'
            test = create_success_test(matrix, result)

        setattr(TestParseAdjacencyMatrix, test_name, test)

    unittest.main()
