from utils import safe_get


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
        expanded_nodes = set()
        queue = [([], self)]

        for (parents, node) in queue:
            visitor(node, parents)
            parent = safe_get(parents, -1)

            if node not in expanded_nodes:
                new_parents = parents + [node]
                extension = [(new_parents, conn)
                             for conn in node.connections if conn != parent]
                queue.extend(extension)
                expanded_nodes.add(node)


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

    def breadth_first_search(self, visitor, roots=None):
        if roots == None:
            roots = range(len(self.nodes))

        visited_nodes = set()

        def visitor_wrapper(node, parents):
            visited_nodes.add(node)
            visitor(node, parents)

        root_nodes = [self.nodes[idx] for idx in roots]

        for node in root_nodes:
            if node not in visited_nodes:
                node.breadth_first_search(visitor_wrapper)
