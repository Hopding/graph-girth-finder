class Node:
  @staticmethod
  def with_id(id):
    return Node(id)

  def __init__(self, id):
    self.id = id
    self.connections = []

  def add_connection(self, connection):
    if connection not in self.connections:
      self.connections.append(connection)

  def breadth_first_search(self, visitor):
    queue = [(None, self)]
    for (parent, node) in queue:
      visitor(node)
      extension = [(node, conn) for conn in node.connections if conn != parent]
      queue.extend(extension)


class Graph:
  @staticmethod
  def from_adjacency_matrix(matrix):
    return Graph(matrix)

  def __init__(self, matrix):
    self.nodes = []

    for row_idx in range(len(matrix)):
      node = Node.with_id(row_idx)
      self.nodes.append(node)

    for (row_idx, row) in enumerate(matrix):
      node = self.find_node_by_id(row_idx)
      for (edge_idx, edge) in enumerate(row):
        if edge == 1:
          connection = self.find_node_by_id(edge_idx)
          node.add_connection(connection)

  def find_node_by_id(self, id):
    for node in self.nodes:
      if node.id == id:
        return node
    return None

  def breadth_first_search(self, visitor):
    visited_nodes = set()

    def visitor_wrapper(node):
      visited_nodes.add(node)
      visitor(node)

    for node in self.nodes:
      if node not in visited_nodes:
        node.breadth_first_search(visitor_wrapper)


