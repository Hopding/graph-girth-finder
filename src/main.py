import sys

from utils import parse_adjacency_matrix
from graph import Graph

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

try:
  matrix = parse_adjacency_matrix(contents, log=True)
except Exception as e:
  print()
  print(e)
  print('Exiting.')
  exit(1)
print()

print('Constructing graph from adjacency matrix...')
graph = Graph.from_adjacency_matrix(matrix)



