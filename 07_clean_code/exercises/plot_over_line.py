# TODO: refactor & clean up this code.
#  1. Copy this file into some new folder
#  2. Initialize a git repo with `git init`
#  3. Commit the file in this current state
#  4. refactor:
#     - Reuse the RasterGrid class from the previous example
#     - Allow for separate generation of the plot data and actual plotting
#     - Allow plotting of any type of function that is callable with a point.
#     -> To this end, you can think about how to turn a discrete function into a callable
from typing import Tuple, List
from dataclasses import dataclass
from math import nan, sqrt, sin, cos, pi
from matplotlib.pyplot import plot, show, close


@dataclass
class Point:
    x: float
    y: float


DataArray = List[List[float]]

@dataclass
class RasterData:
    p0: Point
    dx: Tuple[float, float]
    n: Tuple[float, float]
    values: DataArray


def plot_over_line(raster_data: RasterData,
                   p0: Point,
                   p1: Point,
                   n: int = 1000) -> None:
    current = Point(p0.x, p0.y)
    dp = (
        (p1.x - p0.x)/(n - 1),
        (p1.y - p0.y)/(n - 1)
    )

    x = []
    y = []
    for i in range(n):
        current.x += dp[0]
        current.y += dp[1]
        ix = int((current.x - raster_data.p0.x)/raster_data.dx[0])
        iy = int((current.x - raster_data.p0.x)/raster_data.dx[1])

        x.append(sqrt(dp[0]*dp[0]*i*i + dp[1]*dp[1]*i*i))
        if ix < 0 or ix >= raster_data.n[0] or iy < 0 or iy > raster_data.n[1]:
            y.append(nan)
        else:
            y.append(raster_data.values[ix][iy])

    plot(x, y)
    show()
    close()


if __name__ == "__main__":
    n = (100, 100)
    dx = (0.01, 0.01)
    values = [
        [sin(2.0*pi*(float(i) + 0.5)*dx[0])*cos(2.0*pi*(float(j) + 0.5)*dx[1]) for i in range(n[0])]
        for j in range(n[1])
    ]

    data = RasterData(p0=Point(0., 0.), dx=dx, n=n, values=values)
    plot_over_line(
        data,
        Point(0.0, 0.0),
        Point(1.0, 1.0),
        n=2000
    )
