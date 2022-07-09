"""
unit testing for floyds algorithm
"""
import sys
import unittest
# Maximum number possible for nodes with no direct path
NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]
MAX_LENGTH = len(graph[0])
V = MAX_LENGTH-1


# k = intermediate, i = startnode, j = endnode, distance = graph,
def floyd(k, i, j, distance):
    """
    start of algorithm and recursion
    """
    if i == j:
        distance[i][j] = 0
        # Finds all possible paths and returns the minimum
    distance[i][j] = min(distance[i][j],
                         distance[i][k] +
                         distance[k][j])
    if j < V:
        j += 1
        distance = floyd(k, i, j, distance)

    elif i < V:
        i += 1
        j = 0
        distance = floyd(k, i, j, distance)

    elif k < V:
        k += 1
        i = 0
        j = 0
        distance = floyd(k, i, j, distance)

    return distance
# End of recursion


print(floyd(0, 0, 0, graph))


class Tests(unittest.TestCase):
    """
    testing against a known correct answer from the imperative version
    """
    def test_1(self):
        """
        testing against a known correct answer from the imperative version
        """
        diagram = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        calculated_distances = floyd(0, 0, 0, diagram)
        correct_distances = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
            ]
        print("test_1_calculated_distances: ", calculated_distances)
        self.assertEqual(correct_distances, calculated_distances)

    def test_2(self):
        """
        testing a value in the final stage of recursion
        """
        diagram = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        calculated_distances = floyd(1, 0, 2, diagram)
        correct_distances = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
            ]
        print("test_2_calculated_distances: ", calculated_distances)
        self.assertEqual(correct_distances, calculated_distances)

    def test_3(self):
        """
        testing the  recursion with a non existent node
        """
        diagram = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        calculated_distances = floyd(0, 1, 4, diagram)
        correct_distances = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]
        print("test_3_calculated_distances: ", calculated_distances)
        self.assertEqual(correct_distances, calculated_distances)

    def test_4(self):
        """
        testing against the version on the website given
        """
        diagram = [
            [0, 5, NO_PATH, 10],
            [NO_PATH, 0, 3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        calculated_distances = floyd(0, 0, 0, diagram)
        correct_distances = [
            [0, 5, 8, 9],
            [NO_PATH, 0, 3, 4],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        print("test_4_calculated_distances: ", calculated_distances)
        self.assertEqual(correct_distances, calculated_distances)

    def test_5(self):
        """
        testing function will error by giving an invalid input
        """
        diagram = [
            [0, 7, 'length', 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
            ]
        calculated_distances = floyd(0, 0, 0, diagram)
        correct_distances = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
            ]
        print("test_5_calculated_distances: ", calculated_distances)
        self.assertEqual(correct_distances, calculated_distances)

if __name__ == '__main__':
    unittest.main()
