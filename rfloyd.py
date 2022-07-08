import sys
NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


V=MAX_LENGTH-1   # because indices are 0,1,2,3 so top index is 3 for a 4 item list
def floyd(k, i, j, distance, V):
    if i == j:
        distance[i][j] = 0
        #Finds all possible paths and returns the minimum
    distance[i][j] = min(distance[i][j],
                        distance[i][k] +
                        distance[k][j])
    if j < V:
        j += 1
        distance = floyd(k, i, j,distance, V)

    elif i < V:
        i += 1
        j = 0
        distance = floyd(k, i, j,distance, V)
        
    elif k < V:
        k += 1
        i = 0
        j = 0
        distance= floyd(k, i, j,distance, V)
        
    return distance




print(floyd(0, 0, 0, graph, V))


    