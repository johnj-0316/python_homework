# Task 5
from math import sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def getDistance(self, point: Point) -> int | float:
        dx = self.x - point.x
        dy = self.y - point.y
        return sqrt((dx ** 2) + (dy ** 2))
        
    def __eq__(self, value: Point) -> bool:
        return self.x == value.x and self.y == value.y
    
    def __str__(self) -> str:
        return f"POINT --> x: {self.x}\ny:{self.y}"
    
class Vector(Point):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        
    def __str__(self) -> str:
        return f"VECTOR --> x: {self.x}\ny:{self.y}"
    
    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)


# Tests
def test_point_coordinates():
    point = Point(3, -4)

    assert point.x == 3
    assert point.y == -4


def test_point_distance():
    point1 = Point(0, 0)
    point2 = Point(3, 4)

    assert point1.getDistance(point2) == 5
    assert point2.getDistance(point1) == 5


def test_point_equality():
    assert Point(2, 7) == Point(2, 7)
    assert Point(2, 7) != Point(7, 2)


def test_point_string():
    assert str(Point(3, 4)) == "POINT --> x: 3\ny:4"


def test_vector_is_a_point():
    assert isinstance(Vector(1, 2), Point)


def test_vector_string():
    assert str(Vector(3, 4)) == "VECTOR --> x: 3\ny:4"


def test_add_vectors():
    vector1 = Vector(2, 3)
    vector2 = Vector(-5, 7)

    result = vector1 + vector2

    assert isinstance(result, Vector)
    assert result == Vector(-3, 10)

    
    
