from __future__ import annotations
from typing import List
from math import isclose


class Vector:
    def __init__(self, coordinates: List[float]) -> None:
        self._coordinates = coordinates

    def __getitem__(self, i: int) -> float:
        return self._coordinates[i]

    def __setitem__(self, i: int, value: float) -> None:
        self._coordinates[i] = value

    def __add__(self, other: Vector) -> Vector:
        assert len(self._coordinates) == len(other._coordinates)
        return Vector([self[i] + other[i] for i in range(len(self._coordinates))])

    def __sub__(self, other: Vector) -> Vector:
        assert len(self._coordinates) == len(other._coordinates)
        return Vector([self[i] - other[i] for i in range(len(self._coordinates))])


def test_vector_index_access() -> None:
    for index in [0, 1, 2, 3]:
        reference = [float(i) for i in range(4)]
        vector = Vector(reference)
        assert all(reference[i] == vector[i] for i in range(4))
        vector[index] = 42.0
        assert vector[index] == 42.0

        # Task A: make this test pass
        assert reference[index] != 42.0


def test_3d_vector_addition() -> None:
    v = Vector([1.0, 2.0, 3.0]) + Vector([1.1, 2.2, 3.3])
    assert isclose(v[0], 2.1)
    assert isclose(v[1], 4.2)
    assert isclose(v[2], 6.3)


def test_3d_vector_subtraction() -> None:
    # Task B: add a test for vector subtraction
    assert False
