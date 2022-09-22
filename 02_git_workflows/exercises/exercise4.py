from typing import Tuple, List, Callable
from math import sin, cos
from matplotlib.pyplot import pcolormesh, show, close

from exercise2 import Point2D
from exercise3 import Rectangle

# Task A: add missing documentation for the public functions of the `Raster` class
# Task B: add documentation for the `Raster` class itself

DataArray = List[List[float]]

class Raster:
    def __init__(self, frame: Rectangle, resolution: Tuple[int, int]) -> None:
        self._frame = frame
        self._resolution = resolution
        self._spacing = (
            (frame.upper_right.x - frame.lower_left.x)/resolution[0],
            (frame.upper_right.y - frame.lower_left.y)/resolution[1]
        )
        self._values = self._make_data_array()

    @property
    def resolution(self) -> Tuple[int, int]:
        """Return the raster resolution as (x_resolution, y_resolution)"""
        return self._resolution

    def set_at(self, index: Tuple[int, int], value: float) -> None:
        self._values[index[0]][index[1]] = value

    def set_from(self, function: Callable[[Point2D], float]) -> None:
        for i in range(self._x_resolution()):
            for j in range(self._y_resolution()):
                idx = (i, j)
                point = self._get_point(idx)
                self.set_at(idx, function(point))

    def show(self) -> None:
        pcolormesh(self._values)
        show()
        close()

    def _make_data_array(self) -> DataArray:
        return [
            [0.0 for _ in range(self._x_resolution())]
            for _ in range(self._y_resolution())
        ]

    def _x_resolution(self) -> int:
        return self._resolution[0]

    def _y_resolution(self) -> int:
        return self._resolution[1]

    def _get_point(self, index: Tuple[int, int]) -> Point2D:
        x = self._frame.lower_left.x + (index[0] + 0.5)*self._spacing[0]
        y = self._frame.lower_left.y + (index[1] + 0.5)*self._spacing[1]
        return Point2D(x, y)


def test_raster_construction() -> None:
    raster = Raster(
        Rectangle(Point2D(0.0, 0.0), 1.0, 1.0),
        resolution=(100, 150)
    )
    assert raster.resolution[0] == 100
    assert raster.resolution[1] == 150


def test_raster_construction_from_function() -> None:
    raster = Raster(
        Rectangle(Point2D(0.0, 0.0), 1.0, 1.0),
        resolution=(100, 100)
    )
    raster.set_from(lambda p: sin(p.x)*cos(p.y))


if __name__ == "__main__":
    raster = Raster(
        Rectangle(Point2D(0.0, 0.0), 1.0, 1.0),
        resolution=(100, 100)
    )
    raster.set_from(lambda p: sin(p.x)*cos(p.y))
    raster.show()
