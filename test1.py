###
# Welcome to train express
###


import random
from collections import deque, namedtuple


print("helloWorld!")





"First, imports and data formats. The original implementations suggests using namedtuple for storing edge data. We'll " \
"do exactly that, but we'll add a default value to the cost argument. There are many ways to do that, find what suits " \
"you best "

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)

def split(word):
    return [char for char in word]




while True:
    firstLetter = str(input("Enter the departure point: "))
    firstLetter.lower()
    if (len(firstLetter)>1):
        print("please only input ONE letter")
        continue
    elif not firstLetter.isalpha() == True:
        print("Please enter a letter")
        continue
    else:
        break


while True:
    secondLetter = str(input("Enter the destination point: "))
    secondLetter.lower()
    if not (len(secondLetter)==1):
        print("please only input ONE letter")
        continue
    elif not secondLetter.isalpha() == True:
        print("Please enter a letter")
        continue
    else:
        break




# Data organisation
class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]




    # finding vertices

    @property
    def vertices(self):
        return set(
            # this piece of magic turns ([1,2], [3,4]) into [1, 2, 3, 4]
            # the set above makes it's elements unique.
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )




    # Adding and removing vertices

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))






    # Find neighbour for each node

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours




    # Dijkstra algorithm
    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'

        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            # 3. Select the unvisited node with the smallest distance,
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])

            # 6. Stop, if the smallest distance
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break

            # 4. Find unvisited neighbors for the current node
            # and calculate their distances through the current node.
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost

                # Compare the newly calculated distance to the assigned
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # 5. Mark the current node as visited
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


# list of stops

"""
        Different train routes:
A to B takes 3 minutes
B to A takes 3 minutes
A to D takes 6 minutes
B to C takes 7 minutes 
C to D takes 8 minutes 
D to E takes 9 minutes 
E to D takes 9 minutes 
D to C takes 9 minutes 
D to B takes 5 minutes 
C to E takes 3 minutes
"""

graph = Graph([
    ("a", "b", 3), ("b", "a", 3), ("a", "d", 6), ("b", "c", 7), ("c", "d", 8),
    ("d", "e", 9), ("e", "d", 9), ("d", "c", 9), ("d", "b", 5), ("c", "e", 3)])

# print(graph.dijkstra("a", "e"))
pathLetters = split(graph.dijkstra(firstLetter, secondLetter))
print(pathLetters)
print(len(pathLetters))

distanceDict = {
    "ab": 3,
    "ba": 3,
    "ad": 6,
    "bc": 7,
    "cd": 8,
    "de": 9,
    "ed": 9,
    "dc": 9,
    "db": 5,
    "ce": 3
}

pathlist = []
for item in pathLetters:
    pathlist.append(item)

print(pathlist[0])

count = 0

for item  in pathlist:
    letters = ''
    letters = pathlist[0] + pathlist[1]
    print(letters)
    pathlist.pop(0)
    print(pathlist)
    print("Hello")
    # print(pathlist)
    count += distanceDict[letters]

finalLetters = pathlist[0] + pathlist[1]
print("Final letters: "+finalLetters)
count += distanceDict[finalLetters]
print("count is " + str(count))

