import re 

def pretty_format_cycle(cycle):
  path_ids = [str(node.id) for node in cycle]
  extended_path_ids = path_ids + [path_ids[0]]
  arrow = ' -> '
  return arrow.join(extended_path_ids)

def safe_get(list, idx):
  try:
    return list[idx]
  except:
    return None
