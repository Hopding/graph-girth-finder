from graph import Graph

def find_all_cycles(graph):
  assert isinstance(graph, Graph), 'graph must be instance of Graph'

  visitations = {}

  def visitor(node, parents):
    if node.id not in visitations:
      visitations[node.id] = []
    visitations[node.id].append([p.id for p in parents])

  graph.breadth_first_search(visitor)

  print('Visitations:')
  print(visitations)