import re 

class InvalidMatrixCellError(Exception): pass
class InvalidMatrixShapeError(Exception): pass
class SelfLoopInMatrixError(Exception): pass
class NonsymmetricMatrixError(Exception): pass


def parse_adjacency_matrix(matrix_str):
  lines = matrix_str.strip().splitlines()
  raw_matrix = parse_matrix(lines)
  validate_cells(raw_matrix, is_bit_str)
  matrix = map_cells(raw_matrix, int)
  validate_square(matrix)
  validate_no_self_loops(matrix)
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

  for from_top in range(len(matrix)):
    row = matrix[from_top]

    for from_left in range(len(row)):
      from_bottom = (len(matrix) - 1) - from_top
      from_right = (len(row) - 1) - from_left

      if matrix[from_top][from_left] != matrix[from_bottom][from_right]:
        raise NonsymmetricMatrixError(f'Found nonsymmetric cell in matrix: row={from_top} col={from_left}')