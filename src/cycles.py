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
    all_paths_to_node = [
        path for path in all_other_paths if path[-1] == final_node]
    all_prev_paths = [path for path in all_paths_to_node if len(
        path) <= len(path_to_node)]
    return max(all_prev_paths, key=len)


def find_all_cycles(graph):
    assert isinstance(graph, Graph), 'graph must be instance of Graph'

    visitations = {}

    def visitor(node, parents):
        if node not in visitations:
            visitations[node] = []
        path = parents + [node]
        visitations[node].append(path)

    graph.breadth_first_search(visitor)

    cycle_paths = []

    for node in visitations.keys():
        paths = visitations[node]

        if len(paths) > 1:
            unexpanded_paths = paths[1:]

            for full_path in unexpanded_paths:
                prev_path = prev_path_to_node(full_path, paths)
                ancestor = last_common_ancestor(prev_path, full_path)

                fp_after_ancestor = full_path[full_path.index(ancestor):]
                pp_after_ancestor = prev_path[prev_path.index(ancestor):]

                cycle_path = fp_after_ancestor + pp_after_ancestor[1:-1]
                cycle_paths.append(cycle_path)

    return cycle_paths
