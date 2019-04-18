import sys

# from utils import is_bit_str, parse_matrix, validate_cells, map_cells, validate_square, validate_no_self_loops, validate_symmetric

from utils import parse_adjacency_matrix

if len(sys.argv) < 2:
  print('No input file specified')
  print('Exiting.')
  exit(1)

input_file_path = sys.argv[1]

print('Reading input file:', input_file_path)
with open(input_file_path, 'r') as input_file:
  contents = input_file.read().strip()
  lines = contents.splitlines()
print()

print('Using the following input data as Adjacency Matrix:')
longest_line = max([len(line) for line in lines])
print('-' * longest_line)
print(contents)
print('-' * longest_line)
print()

print('Validating Adjacency Matrix...')
try:
  matrix = parse_adjacency_matrix(contents)
except Exception as e:
  print(e)
  print('Exiting.')
  exit(1)
print('Done.')
print()



