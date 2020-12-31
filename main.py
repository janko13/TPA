from math import sqrt
from copy import copy


class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @staticmethod
    def make_point(lst):
        return Point(lst[0], lst[1], lst[2])

    def print(self):
        print(self.x, self.y, self.z)


def findComponents(V, E):
    for i in range(len(V)):
        V[i] = list([V[i]])
    for e in E:
        first = None
        delete = []
        for i, v in enumerate(V):
            if e[0] in v or e[1] in v:
                if first is None:
                    first = i
                else:
                    V[first] += v
                    delete.append(i)
                    break
        for d in delete:
            V.pop(d)
    return V


if __name__ == "__main__":
    f = open("A_sensors_data.txt", "r")
    points = list()
    for point in f.read()[2:-3].split("},{"):
        points.append(Point.make_point(point.split(",")))

    point_distances = sorted([(((pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2 + (pointA.z - pointB.z) ** 2), i, j)
                      for i, pointA in enumerate(points)
                      for j, pointB in enumerate(points)
                      if i < j])

    point_indexes = list(range(len(points)))

    smallest_possible_r = point_distances[-1][0]

    for i in range(len(points), len(point_distances)+1):
        edges = [(edge[1], edge[2]) for edge in point_distances[:i]]  # use first i edges with the smallest distances
        point_indexes_tmp = copy(point_indexes)
        if len(findComponents(point_indexes_tmp, edges)) == 1:
            smallest_possible_r = point_distances[i-1][0]
            break
    print(sqrt(smallest_possible_r))
