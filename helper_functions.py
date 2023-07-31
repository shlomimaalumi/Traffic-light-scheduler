from passage import Passage
from typing import List
from shapely.geometry import LineString


def can_work_together(list1: List[Passage], list2: List[Passage]) -> bool:
    """
    Check if two lists of passages can work together without any overlapping.

    Args:
        list1 (List[Passage]): The first list of passages.
        list2 (List[Passage]): The second list of passages.

    Returns:
        bool: True if the two lists can work together without overlapping, False otherwise.
    """

    def do_lines_intersect_in_x_range(line1: LineString, line2: LineString, x_min: float, x_max: float) -> bool:
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

    # A small epsilon value used to prevent floating-point inaccuracies
    epsilon = 0.0001

    # Iterate over all combinations of passages from list1 and list2
    for passage1 in list1:
        for passage2 in list2:
            line1, line2 = passage1.line, passage2.line
            # Calculate the start and end x-values for the intersection check
            start_x = max(passage1.x_min, passage2.x_min) + epsilon
            end_x = min(passage1.x_max, passage2.x_max) - epsilon

            # If the lines intersect within the x-axis range, they cannot work together
            if do_lines_intersect_in_x_range(line1, line2, start_x, end_x):
                return False
    return True
