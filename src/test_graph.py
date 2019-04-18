import unittest

from graph import Graph

test_cases = [
  # Visualization:
  #
  #    0---1---2
  #
  [[
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
  ], [
    0, 1, 2
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
  ], [
    0, 1, 2, 3, 4
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
  ], [
    0, 1, 2, 4, 3
  ]],


  # # Visualization:
  # #   0---1---2
  # #     |   |
  # #     3   4
  # [[
  #   [0, 1, 0, 1, 0],
  #   [1, 0, 1, 1, 1],
  #   [0, 1, 0, 0, 1],
  #   [1, 1, 0, 0, 0],
  #   [0, 1, 1, 0, 0],
  # ], [
  #   0, 1, 3, 2, 4
  # ]],
]


class TestGraphBfs(unittest.TestCase):
  pass


def create_test(matrix, bfs_order):
  def test(self):
    graph = Graph.from_adjacency_matrix(matrix)

    actual = []
    def visitor(node): actual.append(node.id)
    graph.breadth_first_search(visitor)

    expected = bfs_order

    self.assertEqual(actual, expected)
  return test


if __name__ == '__main__':
  for (idx, test_case) in enumerate(test_cases):
    matrix = test_case[0]
    bfs_order = test_case[1]

    test_name = f'test_{idx}'
    test = create_test(matrix, bfs_order)

    setattr(TestGraphBfs, test_name, test)

  unittest.main()