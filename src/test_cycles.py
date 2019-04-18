import unittest

from graph import Graph
from cycles import find_all_cycles

# Tool to help create ASCII graphs: http://asciiflow.com/
test_cases = [
  # # Visualization:
  # #
  # #    0---1---2
  # #
  # [[
  #   [0, 1, 0],
  #   [1, 0, 1],
  #   [0, 1, 0],
  # ], None, [
  #   (0, []),
  #   (1, [0]),
  #   (2, [0, 1])
  # ]],

  # # Visualization:
  # #
  # #    0---1---2
  # #        |   |
  # #        3   4
  # #
  # [[
  #   [0, 1, 0, 0, 0],
  #   [1, 0, 1, 1, 0],
  #   [0, 1, 0, 0, 1],
  #   [0, 1, 0, 0, 0],
  #   [0, 0, 1, 0, 0],
  # ], None, [
  #   (0, []),
  #   (1, [0]),
  #   (2, [0, 1]),
  #   (3, [0, 1]),
  #   (4, [0, 1, 2]),
  # ]],

  # # Visualization:
  # #
  # #    0---1  2
  # #           |
  # #       3---4
  # #
  # [[
  #   [0, 1, 0, 0, 0],
  #   [1, 0, 0, 0, 0],
  #   [0, 0, 0, 0, 1],
  #   [0, 0, 0, 0, 1],
  #   [0, 0, 1, 1, 0],
  # ], None, [
  #   (0, []),
  #   (1, [0]),
  #   (2, []),
  #   (4, [2]),
  #   (3, [2, 4]),
  # ]],

  # Visualization:
  #
  #   0---1   2---3
  #   |   | / | / |
  #   4   5---6---7
  #
  [[
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
  ], [
    [5, 6, 2],
    [5, 2, 6],
    [2, 3, 6],
    [5, 6, 3, 2],
    [5, 6, 7, 3, 2],
    [5, 2, 3, 7, 6]
  ]],


  # # Visualization:
  # #
  # #   --3--
  # #   |   |
  # #   0---1---2
  # #       |   |
  # #       --4--
  # #
  # [[
  #   [0, 1, 0, 1, 0],
  #   [1, 0, 1, 1, 1],
  #   [0, 1, 0, 0, 1],
  #   [1, 1, 0, 0, 0],
  #   [0, 1, 1, 0, 0],
  # ], None, [
  #   (0, []),
  #   (1, [0]),
  #   (3, [0]),

  #   (2, [0, 1]),
  #   (3, [0, 1]),

  #   (4, [0, 1]),
  #   (1, [0, 3]),
  #   (4, [0, 1, 2]),
  #   (2, [0, 1, 4]),
  # ]],
]

class TestFindAllCycles(unittest.TestCase):
  pass


def create_test(matrix, cycles):
  def test(self):
    graph = Graph.from_adjacency_matrix(matrix)

    raw_cycles = find_all_cycles(graph)
    pretty_cycles = [[node.id for node in cycle] for cycle in raw_cycles]

    actual = pretty_cycles
    expected = cycles

    self.assertEqual(actual, expected)
  return test


if __name__ == '__main__':
  for (idx, test_case) in enumerate(test_cases):
    matrix = test_case[0]
    cycles = test_case[1]

    test_name = f'test_{idx}'
    test = create_test(matrix, cycles)

    setattr(TestFindAllCycles, test_name, test)

  unittest.main()