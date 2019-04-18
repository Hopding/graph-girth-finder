class Node:
  @staticmethod
  def with_name(name):
    return Node(name)

  def __init__(self, name):
    self.name = name
    self.connections = []

  def add_connection(self, connection):
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
      node = Node.with_name(row_idx)
      self.nodes.append(node)

    for (row_idx, row) in enumerate(matrix):
      node = self.find_node_by_name(row_idx)
      for (edge_idx, edge) in enumerate(row):
        if edge == 1:
          connection = self.find_node_by_name(edge_idx)
          node.add_connection(connection)

  def find_node_by_name(self, name):
    for node in self.nodes:
      if node.name == name:
        return node
    return None

  def breadth_first_search(self, visitor):
    if len(self.nodes) == 0: return
    root_node = self.nodes[0]
    # other_nodes = self.nodes[1:]

    # TODO: Handle disconnected graphs...
    root_node.breadth_first_search(visitor)

