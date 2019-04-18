import re 

class InvalidMatrixCellError(Exception): pass
class InvalidMatrixShapeError(Exception): pass
class SelfLoopInMatrixError(Exception): pass
class NonsymmetricMatrixError(Exception): pass


def parse_adjacency_matrix(matrix_str, log=False):
  if log: print('Parsing matrix...')
  lines = matrix_str.strip().splitlines()
  raw_matrix = parse_matrix(lines)

  if log: print('Validating matrix cells are 0 or 1...')
  validate_cells(raw_matrix, is_bit_str)
  matrix = map_cells(raw_matrix, int)

  if log: print('Validating matrix is square...')
  validate_square(matrix)

  if log: print('Validating matrix contains no self loops...')
  validate_no_self_loops(matrix)

  if log: print('Validating matrix is symmetric...')
  validate_symmetric(matrix)

  return matrix

def is_bit_str(n_str):
  return n_str in {'0', '1'}

def is_bit(n):
  return n in {0, 1}

def parse_matrix(matrix_lines):
  rows = []
  for line in matrix_lines:
    row = re.split(' ', line)
    rows.append(row)
  return rows
      
def map_cells(matrix, mapper):
  new_matrix = []
  for row in matrix:
    new_row = []
    for cell in row:
      new_cell = mapper(cell)
      new_row.append(new_cell)
    new_matrix.append(new_row)
  return new_matrix

def validate_cells(matrix, predicate):
  for row in matrix:
    for cell in row:
      if not predicate(cell):
        raise InvalidMatrixCellError(f'Found invalid matrix cell: "{cell}"')

def validate_square(matrix):
  target_length = len(matrix[0])

  any_mismatch = False
  for row in matrix:
    if len(row) != target_length:
      any_mismatch = True

  if any_mismatch or target_length != len(matrix):
    raise InvalidMatrixShapeError('Matrix is not square.')

def validate_no_self_loops(matrix):
  for (left_offset, row) in enumerate(matrix):
    cell = row[left_offset]
    if cell == 1:
      raise SelfLoopInMatrixError(f'Found self loop on vertex {left_offset}')

def validate_symmetric(matrix):
  """Ensures matrix represents an undirected graph"""

  matrix_height = len(matrix)
  matrix_width  = len(matrix[0])

  for from_top in range(matrix_height):
    for from_left in range(matrix_width):
      if matrix[from_top][from_left] != matrix[from_left][from_top]:
        msg = f'Found nonsymmetric cell in matrix: row={from_top} col={from_left}'
        raise NonsymmetricMatrixError(msg)
