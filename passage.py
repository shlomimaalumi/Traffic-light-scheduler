from typing import Tuple, List
from shapely.geometry import LineString
from enums import PassageJam
from time import time


class Passage:
    def __init__(self, source: Tuple[float, float], target: Tuple[float, float], rate=PassageJam.MEDIUM):
        """Initialize a new Passage object representing a line segment between two points.

        Args:
            source (Tuple[float, float]): The coordinates of the source point (x, y).
            target (Tuple[float, float]): The coordinates of the target point (x, y).
            rate: the importance of this passage.
        """
        self.source = source
        self.target = target
        self.rate = rate
        self.line = line = LineString([source, target])
        self.x_min = min(source[0], target[0])
        self.x_max = max(source[0], target[0])
        self.last_open = time()

    def update_time(self):
        """
        Update the last_open attribute with the current timestamp.

        This method is called to record the current time as the last time the traffic light was opened.
        It updates the last_open attribute with the current timestamp using the time() function from the time module.
        """
        self.last_open = time()

    def time_from_last_open(self):
        """
        Calculate the time elapsed since the traffic light was last opened.

        Returns:
            float: The time elapsed (in seconds) since the traffic light was last opened.
        """
        return time() - self.last_open

    @classmethod
    def do_lines_intersect_in_x_range(cls, line1: LineString, line2: LineString, x_min: float, x_max: float) -> bool:
        """
        Check if two lines intersect within a specific range of the x-axis.

        Args:
            line1 (LineString): The first line.
            line2 (LineString): The second line.
            x_min (float): The minimum x-coordinate value of the range.
            x_max (float): The maximum x-coordinate value of the range.

        Returns:
            bool: True if the lines intersect within the specified x-axis range, False otherwise.
        """
        # Check if the bounding boxes of the lines intersect in the x-axis range
        if line1 != line2 and line1.bounds[0] <= x_max and line1.bounds[2] >= x_min \
                and line2.bounds[0] <= x_max and line2.bounds[2] >= x_min:
            # Perform an intersection check between the lines
            return line1.intersects(line2)
        return False

    @staticmethod
    def can_work_together(list1: List['Passage'], list2: List['Passage']) -> bool:
        """
        Check if two lists of passages can work together without any overlapping.

        Args:
            list1 (List[Passage]): The first list of passages.
            list2 (List[Passage]): The second list of passages.

        Returns:
            bool: True if the two lists can work together without overlapping, False otherwise.
        """

        # A small epsilon value used to prevent floating-point inaccuracies
        # epsilon = 0.0001

        # Iterate over all combinations of passages from list1 and list2
        for passage1 in list1:
            for passage2 in list2:
                line1, line2 = passage1.line, passage2.line
                # Calculate the start and end x-values for the intersection check
                start_x = max(passage1.x_min, passage2.x_min)  # + epsilon
                end_x = min(passage1.x_max, passage2.x_max)  # - epsilon

                # If the lines intersect within the x-axis range, they cannot work together
                if Passage.do_lines_intersect_in_x_range(line1, line2, start_x, end_x):
                    return False
        return True

    @staticmethod
    def is_action_valid(action: List['Passage']) -> bool:
        """
        Check if a list of passages can form a valid action without any overlapping.

        Args:
            action (List[Passage]): The list of passages representing the action.

        Returns:
            bool: True if the action is valid (no overlapping passages), False otherwise.
        """
        for p1 in action:
            for p2 in action:
                if p2.source != p1.source and not Passage.can_work_together([p1], [p2]):
                    return False
        return True
