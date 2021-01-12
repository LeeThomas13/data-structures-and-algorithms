from collections import deque

class Vertex:
    #vertexes are the points on a graph
    def __init__(self, value):
        self.value = value


class Edge:
    #edges are the link between vertexes
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)



class Graph:

    def __init__(self):
        self._adjacency_list = {}
        self.total_vertices = 0

    def add_node(self, value):
        self.total_vertices += 1
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in graph")

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def size(self):
        return len(self._adjacency_list)

    def breadth_first(self, start_vertex):
        start_vertex.setDistance(0)
        start_vertex.setPred(None)
        breadth = Queue()
        breadth.enqueue(start_vertex)

        while (breadth.size() > 0):
            front = breadth.dequeue()
            for i in front.get_neighbor_nodes():
                if (i.getColor() == 'white'):
                    i.setColor('gray')
                    i.setDistance(front.getDistance() + 1)
                    i.setPred(front)
                    breadth.enqueue(i)
            front.setColor('black')

    # def breadth_first(self, start_vertex):
    #     nodes = []
    #     breadth = Queue()
    #     breadth.enqueue(start_vertex)

    #     while(breadth):
    #         front = breadth.dequeue()
    #         nodes.append(front)

    #         #DANGER get neighbors returns the edge not the vertices, fix that
    #         children = self.get_neighbors(front)

    #         for child in children:
    #             if not child.visited:
    #                 child.visited = True
    #             breadth.enqueue(child)


