# Graph Theory
* Branch of mathematics that studies the properties and applications of graphs.

## Graph:
* A graph is a collection of vertices (also called nodes) connected by edges (also called links). Graphs are used to model pairwise relations between objects, making them a powerful tool for representing and analyzing complex systems in various fields

### Bipartite Graph:
* A Bipartite Graph is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set.
* The two sets are usually called the parts of the graph.
* An important characteristic of a bipartite graph is that it cannot contain any odd-length cycles.

# Problem of matching blocks:
* Supposing the blocks of both documents can be defined as set A and set B, the goal is now to match the blocks from set A to the ones on set B based on a measure of similarity.

* Adapting the problem to graph theory:
  * Vertices:  Each block of text in both Set A and Set B can be represented as a vertex (or node) in the graph;
  * Edges: The measure of similarity between two blocks of text (one from Set A and one from Set B) can be represented as an edge connecting the two vertices. The weight of the edge can represent the degree of similarity;
  * Bipartite Graph: Since each edge connects a vertex in Set A to a vertex in Set B, and no two vertices within the same set are connected, this forms a Bipartite Graph.

    The problem is then defined as finding an optimal matching in this Bipartite Graph, which means maximizing the  sum of the weights (similarity measures) of the matched edges.

## The Hopcroft-Karp Algorithm:
