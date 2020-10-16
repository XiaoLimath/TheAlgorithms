import numpy as np

def euclidean_distance(v1, v2) -> double:
    """
    Calculate the distance between the two = endpoints of two vectors, v1 and v2.
    >>> euclidean_distance(np.array([0, 0]), np.array([2, 2]))
    2.8284271247461903
    >>> euclidean_distance(np.array([0, 0, 0]), np.array([2, 2, 2]))
    3.4641016151377544
    >>> euclidean_distance(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]))
    8.0
    """

    sumSquared = 0 
    for i in range(len(v1)):
        sumSquared += (v2[i] - v1[i]) ** 2
    return sumSquared ** (1 / 2)

if __name__ == "__main__":
    point = np.array([2, 2])
    point2 = np.array([0, 0])
    print(euclidean_distance(point, point2))
