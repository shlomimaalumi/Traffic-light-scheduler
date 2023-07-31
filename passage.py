from typing import Tuple
from shapely.geometry import LineString


class Passage:
    def __init__(self, source: Tuple[float, float], target: Tuple[float, float]):
        """Initialize a new Passage object representing a line segment between two points.

        Args:
            source (Tuple[float, float]): The coordinates of the source point (x, y).
            target (Tuple[float, float]): The coordinates of the target point (x, y).
        """
        self.source = source
        self.target = target
        self.line = line = LineString([source, target])
        self.x_min = min(source[0], target[0])
        self.x_max = max(source[0], target[0])

