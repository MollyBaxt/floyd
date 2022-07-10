"""
Floyds Algortihm using an imperative method
"""
import sys
import itertools

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(graph[0])


def floyd(dist):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in \
            itertools.product(range(MAX_LENGTH), range(MAX_LENGTH),
                              range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            dist[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        dist[start_node][end_node] = min(dist[start_node][end_node],
                                         dist[start_node][intermediate] +
                                         dist[intermediate][end_node])
        # Any value that have sys.maxsize has no path
    return dist


print(floyd(graph))

