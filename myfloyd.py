import sys
#for nodes with no direct path
NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8], 
    [NO_PATH, 0, 5, NO_PATH], 
    [NO_PATH, NO_PATH, 0, 2], 
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

MAX_LENGTH = len(graph[0])

#Items in a list minus 1. 4 itemed list would be represented by 3 since python counts 0,1,2,3
V=MAX_LENGTH-1   
def floyd(i, j, k, distance):
    if i == j:
        distance[i][j] = 0
        #Finds all possible paths and returns the minimum
        distance[i][j] = min(distance[i][j],
                        distance[i][k]
                        + distance[k][j])
    #start of the recursion 
    if i < V:
        i += 1
        distance = floyd(i, j, k, distance)

    elif j < V:
        j += 1
        i = 0
        distance = floyd(i, j, k, distance)

    elif k < V:
        k += 1
        i = 0
        j = 0
        distance = floyd(i, j, k, distance)

    return distance
#end of recursion

#print result
print(floyd(0, 0, 0, graph))
