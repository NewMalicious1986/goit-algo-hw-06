# Graph Analysis Using DFS and BFS

## Overview
This project demonstrates how to analyze a graph and find paths between nodes using **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** algorithms. Additionally, the results of both algorithms are compared to understand their differences in finding paths.

## Graph Structure
The graph used for the analysis consists of nodes and edges:

```
Nodes: A, B, C, D, E
Edges:
  A -- B
  A -- C
  B -- D
  C -- D
  D -- E
```

## Results
### Paths Found
- **DFS Path**: `['A', 'B', 'D', 'E']`
- **BFS Path**: `['A', 'C', 'D', 'E']`

### Comparison
| Algorithm | Path            | Characteristics                       |
|-----------|-----------------|---------------------------------------|
| DFS       | A -> B -> D -> E | Prioritizes depth; may not be optimal |
| BFS       | A -> C -> D -> E | Explores breadth; guarantees shortest path |

### Explanation of Differences
- **DFS**:
  - Explores as far as possible along a branch before backtracking.
  - The path depends on the order of edge addition and exploration.
  - May not find the shortest path.

- **BFS**:
  - Explores all nodes at the current level before moving deeper.
  - Guarantees the shortest path (in terms of the number of nodes).
  - Requires more memory compared to DFS as it stores all nodes at the current level.
