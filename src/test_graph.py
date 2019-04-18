import unittest

from graph import Graph

# Tool to help create ASCII graphs: http://asciiflow.com/
test_cases = [
  # Visualization:
  #
  #    0---1---2
  #
  [[
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
  ], None, [
    (0, []),
    (1, [0]),
    (2, [0, 1])
  ]],

  # Visualization:
  #
  #    0---1---2
  #        |   |
  #        3   4
  #
  [[
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
  ], None, [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1]),
    (4, [0, 1, 2]),
  ]],

  # Visualization:
  #
  #    0---1  2
  #           |
  #       3---4
  #
  [[
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0],
  ], None, [
    (0, []),
    (1, [0]),
    (2, []),
    (4, [2]),
    (3, [2, 4]),
  ]],

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
  ], [1], [
    (1, []),

    (0, [1]),
    (5, [1]),

    (4, [1, 0]),
    (2, [1, 5]),
    (6, [1, 5]),

    (3, [1, 5, 2]),
    (6, [1, 5, 2]),
    (2, [1, 5, 6]),
    (3, [1, 5, 6]),
    (7, [1, 5, 6]),

    (6, [1, 5, 2, 3]),
    (7, [1, 5, 2, 3]),
    (3, [1, 5, 6, 7]),
  ]],


  # Visualization:
  #
  #   --3--
  #   |   |
  #   0---1---2
  #       |   |
  #       --4--
  #
  [[
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
  ], None, [
    (0, []),
    (1, [0]),
    (3, [0]),

    (2, [0, 1]),
    (3, [0, 1]),

    (4, [0, 1]),
    (1, [0, 3]),
    (4, [0, 1, 2]),
    (2, [0, 1, 4]),
  ]],
]

class TestGraphBfs(unittest.TestCase):
  pass


def create_test(matrix, roots, bfs_order):
  def test(self):
    graph = Graph.from_adjacency_matrix(matrix)

    actual = []
    def visitor(node, parents): actual.append((node.id, [n.id for n in parents]))
    graph.breadth_first_search(visitor, roots=roots)

    expected = bfs_order

    self.assertEqual(actual, expected)
  return test


if __name__ == '__main__':
  for (idx, test_case) in enumerate(test_cases):
    matrix = test_case[0]
    roots = test_case[1]
    bfs_order = test_case[2]

    test_name = f'test_{idx}'
    test = create_test(matrix, roots, bfs_order)

    setattr(TestGraphBfs, test_name, test)

  unittest.main()