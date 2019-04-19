import operator 
from functools import reduce 

from graph import Graph

def last_common_ancestor(path_a, path_b):
  ancestor = None
  for (step_a, step_b) in zip(path_a, path_b):
    if step_a == step_b:
      ancestor = step_a
    else:
      break
  return ancestor


def prev_path_to_node(path_to_node, all_paths):
  final_node = path_to_node[-1]
  all_other_paths = [path for path in all_paths if path != path_to_node]
  all_paths_to_node = [path for path in all_other_paths if path[-1] == final_node]
  all_prev_paths = [path for path in all_paths_to_node if len(path) <= len(path_to_node)]
  return max(all_prev_paths, key=len)


def find_all_paths_to_nodes(graph):
  assert isinstance(graph, Graph), 'graph must be instance of Graph'

  visitations = {}
  def visitor(node, parents):
    if node not in visitations:
      visitations[node] = []
    path = parents + [node]
    visitations[node].append(path)

  graph.breadth_first_search(visitor)

  return visitations


def find_all_paths_in_cycles(paths_by_node):
  # paths_in_cycles = []
  # for node in paths_by_node.keys():
    # paths = paths_by_node[node]
    # if len(paths) > 1:
      # unexpanded_paths = paths[1:]
      # paths_in_cycles.extend(unexpanded_paths)

  paths_in_cycles = []
  for paths in paths_by_node.values():
    if len(paths) > 1:
      unexpanded_paths = paths[1:]
      paths_in_cycles.extend(unexpanded_paths)


def find_all_cycles(graph):
  assert isinstance(graph, Graph), 'graph must be instance of Graph'

  # paths_by_node = find_all_paths_to_nodes(graph)

  # cycle_paths = []

  # for node in paths_by_node.keys():
  #   paths = paths_by_node[node]

  #   if len(paths) > 1:
  #     unexpanded_paths = paths[1:]

  #     for full_path in unexpanded_paths:
  #       prev_path = prev_path_to_node(full_path, paths)
  #       ancestor = last_common_ancestor(prev_path, full_path)

  #       fp_after_ancestor = full_path[full_path.index(ancestor):]
  #       pp_after_ancestor = prev_path[prev_path.index(ancestor):]

  #       cycle_path = fp_after_ancestor + pp_after_ancestor[1:-1]
  #       cycle_paths.append(cycle_path)

  paths_by_node = find_all_paths_to_nodes(graph)
  # all_paths = [path for paths_by_node.values()]
  all_paths = reduce(operator.concat, paths_by_node.values())

  for path in find_all_paths_in_cycles(paths_by_node):

    prev_path = prev_path_to_node(path, all_paths)
    ancestor = last_common_ancestor(prev_path, path)

    fp_after_ancestor = full_path[full_path.index(ancestor):]
    pp_after_ancestor = prev_path[prev_path.index(ancestor):]

    cycle_path = fp_after_ancestor + pp_after_ancestor[1:-1]
    cycle_paths.append(cycle_path)

  return cycle_paths