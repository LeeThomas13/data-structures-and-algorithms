# Graphs
A graph is characterized by multiple nodes being connected for whatever reason you choose. The graph is characterized by having verticies and edges. Verticies are basically nodes and they hold the data. Edges are the lines that connects verticies.

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

AddNode()
Adds a new node to the graph
Takes in the value of that node
Returns the added node
AddEdge()
Adds a new edge between two nodes in the graph
Include the ability to have a “weight”
Takes in the two nodes to be connected by the edge
Both nodes should already be in the Graph
GetNodes()
Returns all of the nodes in the graph as a collection (set, list, or similar)
GetNeighbors()
Returns a collection of edges connected to the given node
Takes in a given node
Include the weight of the connection in the returned collection
Size()
Returns the total number of nodes in the graph

## Approach & Efficiency
The efficiency of graphs is O(n) space complexity and O(n) time complexity I beleive

## API
add_node() adds a new node to the graph
add_edge() adds an edge between two nodes
get_node() returns all of the nodes in the graph in a list
get_neighbors() returns a tuple of edges and their connected nodes
size() returns the length of the adjacency_list
