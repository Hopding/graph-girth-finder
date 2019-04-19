# UMSL CS5130 Project 2

This program fulfills the requirements for CS5130 Project 2. It takes the adjacency matrix for an undirected graph as input, and outputs the graph's girth along with all cycles whose length is equal to the girth.

## Program Outline

When processing an input file, the following steps are performed:

1. **Input** - The input file is read, and split into rows based on newlines. Each row is split into cells based on spaces. The result is a matrix.
2. **Validation** - The matrix is validated as follows. If any of these validations fail, the program will notify the user and exit.

   - **Square Matrix** - The matrix must have the same number of rows and columns.
   - **Bit Value Entries** - Each cell in the matrix must be `0` or `1`.
   - **No Self-Loops** - The diagonal cells (from top left to bottom right) must all be `0`.
   - **Undirected Graph** - The adjacency matrix must be symmetric over the diagonal (from top left to bottom right).
   - **At Least 1 Cycle** - The matrix must contain at least one cycle.

3. **Find all Cycles** - The matrix is converted into a graph. All cycles in this graph are identified via a modified version of breadth first search.
4. **Find the Girth** - The length of the shortest cycles in the graph are identified. This is the Girth.
5. **Output Results** - The girth is output to the console, along with all cycles whose length is equal to the girth.

## Requirements

To run this program, you must have Python 3.7 installed on your machine. Older and newer versions may work, but only 3.7 has been tested.

## Running

- You can use the included `run` script:
  ```
  ./run data/test8.matrix
  ```
- Alternatively, you can run the `main.py` script directly:
  ```
  python3.7 src/main.py data/test8.matrix
  ```

## Unit Tests

- You can use the included `test` script:
  ```
  ./test
  ```
- Alternatively, you can run the `test_*.py` files directly:
  ```
  python3.7 src/test_adjacency_matrix.py
  python3.7 src/test_graph.py
  python3.7 src/test_cycles.py
  ```

## Output For `data/*.matrix` Files

```
$ ./run data/test1.matrix
Reading input file: data/test1.matrix

Using the following input data as Adjacency Matrix:
-----
0 1 0
1 0 1
0 1 0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Finding all cycles in graph...
Graph contains no cycles.
Exiting.
```

```
$ ./run data/test2.matrix
Reading input file: data/test2.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 x
0 1 0
1 0 1
-----

Parsing matrix...
Validating matrix cells are 0 or 1...

Found invalid matrix cell: "x"
Exiting.
```

```
$ ./run data/test3.matrix
Reading input file: data/test3.matrix

Using the following input data as Adjacency Matrix:
-------
1 0 1
0 1 0 0
1 0 1
-------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...

Matrix is not square.
Exiting.
```

```
$ ./run data/test4.matrix
Reading input file: data/test4.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 1
0 1 0
1 0 1
0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...

Matrix is not square.
Exiting.
```

```
$ ./run data/test5.matrix
Reading input file: data/test5.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 1
0 1 0
1 0 1
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...

Found self loop on vertex 0
Exiting.
```

```
$ ./run data/test6.matrix
Reading input file: data/test6.matrix

Using the following input data as Adjacency Matrix:
-----
0 1 0
0 0 1
0 1 0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found nonsymmetric cell in matrix: row=0 col=1
Exiting.
```

```
$ ./run data/test7.matrix
Reading input file: data/test7.matrix

Using the following input data as Adjacency Matrix:
---------------
0 1 0 0 1 0 0 0
1 0 0 0 0 1 0 0
0 0 0 1 0 1 1 0
0 0 1 0 0 0 1 1
1 0 0 0 0 0 0 0
0 1 1 0 0 0 1 0
0 0 1 1 0 1 0 1
0 0 0 1 0 0 1 0
---------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Finding all cycles in graph...
• Found cycle: 5 -> 6 -> 2 -> 5
• Found cycle: 5 -> 2 -> 6 -> 5
• Found cycle: 2 -> 3 -> 6 -> 2
• Found cycle: 5 -> 6 -> 3 -> 2 -> 5
• Found cycle: 5 -> 6 -> 7 -> 3 -> 2 -> 5
• Found cycle: 5 -> 2 -> 3 -> 7 -> 6 -> 5

Finding girth of graph...
• Found girth: 3

Finding all cycles whose length equals the girth...
• Found girth cycle: 5 -> 6 -> 2 -> 5
• Found girth cycle: 5 -> 2 -> 6 -> 5
• Found girth cycle: 2 -> 3 -> 6 -> 2
```

```
$ ./run data/test8.matrix
Reading input file: data/test8.matrix

Using the following input data as Adjacency Matrix:
---------
0 1 0 1 0
1 0 1 1 1
0 1 0 0 1
1 1 0 0 0
0 1 1 0 0
---------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Finding all cycles in graph...
• Found cycle: 0 -> 3 -> 1 -> 0
• Found cycle: 0 -> 1 -> 3 -> 0
• Found cycle: 1 -> 4 -> 2 -> 1
• Found cycle: 1 -> 2 -> 4 -> 1

Finding girth of graph...
• Found girth: 3

Finding all cycles whose length equals the girth...
• Found girth cycle: 0 -> 3 -> 1 -> 0
• Found girth cycle: 0 -> 1 -> 3 -> 0
• Found girth cycle: 1 -> 4 -> 2 -> 1
• Found girth cycle: 1 -> 2 -> 4 -> 1
```

```
$ ./run data/test9.matrix
Reading input file: data/test9.matrix

Using the following input data as Adjacency Matrix:
-------------
0 1 0 0 0 0 1
1 0 1 1 1 0 0
0 1 0 1 0 0 1
0 1 1 0 1 1 1
0 1 0 1 0 0 0
0 0 0 1 0 0 0
1 0 1 1 0 0 0
-------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Finding all cycles in graph...
• Found cycle: 1 -> 2 -> 6 -> 3 -> 1
• Found cycle: 1 -> 3 -> 6 -> 2 -> 1
• Found cycle: 0 -> 6 -> 2 -> 1 -> 0
• Found cycle: 1 -> 3 -> 2 -> 1
• Found cycle: 0 -> 6 -> 3 -> 1 -> 0
• Found cycle: 1 -> 2 -> 3 -> 4 -> 1
• Found cycle: 1 -> 4 -> 3 -> 2 -> 1
• Found cycle: 1 -> 3 -> 4 -> 1

Finding girth of graph...
• Found girth: 3

Finding all cycles whose length equals the girth...
• Found girth cycle: 1 -> 3 -> 2 -> 1
• Found girth cycle: 1 -> 3 -> 4 -> 1
```
