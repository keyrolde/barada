from point import Point
from typing import List

class Rectangle:
    def __init__(self, point_list: List[Point] = None):
        self.point_list1 = point_list if point_list else [Point(), Point(), Point()]


    def get_point_list(self):
        result = []
        for dot in self.point_list1:
            result.append(dot.x)
            result.append(dot.y)
        return result
v = Rectangle()