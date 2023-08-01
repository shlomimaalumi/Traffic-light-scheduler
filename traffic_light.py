import time
from enums import TrafficLightState
from passage import Passage
from typing import List
from functools import reduce
# from intersection import Intersection


class TrafficLight:
    counter = 1

    def __init__(self, passages: List[Passage]):
        """Initialize a new TrafficLight object."""
        self.id = TrafficLight.counter
        self.passages_allow = passages
        TrafficLight.counter += 1
        self.state = TrafficLightState.RED
        self.traffic_jam = 0
        self.begin_time = time.time()
        self.duration = 0
        self.last_time_green = 0

    def set_state(self, state: TrafficLightState):
        """Set the state of the TrafficLight.

        Args:
            state (TrafficLightState): The new state of the TrafficLight.
        """
        self.state = state

    def green_on_for(self, duration: float):
        """Turn the TrafficLight green for a specified duration.

        Args:
            duration (float): The duration for which the TrafficLight will remain green (in seconds).
        """
        print(f"traffic light number: {self.id} being green")
        self.set_state(TrafficLightState.GREEN)
        self.begin_time = time.time()
        self.duration = duration

    def red_on(self):
        """Turn the TrafficLight red.

        This method is called when the TrafficLight changes from green to red.
        """
        if self.state == TrafficLightState.GREEN:
            print(f"traffic light number: {self.id} being red")
            self.set_state(TrafficLightState.RED)
            self.last_time_green = time.time()

    def get_traffic_jam(self) -> int:
        """Get the traffic jam status of the TrafficLight.

        Returns:
            int: The traffic jam status, if applicable.
        """
        return self.traffic_jam

    def get_state(self) -> TrafficLightState:
        """Get the current state of the TrafficLight.

        Returns:
            TrafficLightState: The current state of the TrafficLight.
        """
        return self.state

    def get_remaining_duration(self) -> float:
        """Get the remaining duration of the green light.

        Returns:
            float: The remaining duration of the green light (in seconds).
        """
        return self.duration - self.get_current_duration()

    def get_current_duration(self) -> float:
        """Get the current duration of the green light.

        Returns:
            float: The current duration of the green light (in seconds).
        """
        return time.time() - self.begin_time

    def get_passages(self) -> List[Passage]:
        return self.passages_allow

    def get_id(self) -> int:
        """Get the ID of the TrafficLight.

        Returns:
            int: The ID of the TrafficLight.
        """
        return self.id

    @staticmethod
    def passages_from_traffic_lights(traffic_lights: List['TrafficLight']) -> List[Passage]:
        """
        Get a list of passages from a list of traffic lights and merge them into a single list.

        Args:
            traffic_lights (List['TrafficLight']): A list of TrafficLight objects.

        Returns:
            List[Passage]: A list containing all the passages obtained from the traffic lights without duplicates.
        """
        passages = []
        for tl in traffic_lights:
            passages.append(tl.get_passages())
        # Use reduce and set.union to merge all the sets into one list and remove duplicates
        return list(reduce(set.union, map(set, passages)))



    @staticmethod
    def can_work_together(traffic_lights: List['TrafficLight']) -> bool:
        """
        Check if the traffic lights can work together without any overlapping passages.

        Args:
            traffic_lights (List[TrafficLight]): A list of TrafficLight objects.

        Returns:
            bool: True if the traffic lights can work together without overlapping passages, False otherwise.
        """
        passges_allowed = TrafficLight.passages_from_traffic_lights(traffic_lights)
        return Passage.is_action_valid(passges_allowed)

    # def can_work_with(self, other: 'TrafficLight') -> bool:
    #     """Check if this TrafficLight can work with another TrafficLight.
    #
    #     Args:
    #         other (TrafficLight): The other TrafficLight to check compatibility with.
    #
    #     Returns:
    #         bool: True if the two traffic lights can work together, False otherwise.
    #     """
    #
    #     def do_lines_intersect_in_x_range(line1: LineString, line2: LineString, x_min: float, x_max: float) -> bool:
    #         """
    #         Check if two lines intersect within a specific range of the x-axis.
    #
    #         Args:
    #             line1 (LineString): The first line.
    #             line2 (LineString): The second line.
    #             x_min (float): The minimum x-coordinate value of the range.
    #             x_max (float): The maximum x-coordinate value of the range.
    #
    #         Returns:
    #             bool: True if the lines intersect within the specified x-axis range, False otherwise.
    #         """
    #         # Check if the bounding boxes of the lines intersect in the x-axis range
    #         if line1 != line2 and line1.bounds[0] <= x_max and line1.bounds[2] >= x_min \
    #                 and line2.bounds[0] <= x_max and line2.bounds[2] >= x_min:
    #             # Perform an intersection check between the lines
    #             return line1.intersects(line2)
    #         return False
    #
    #     epsilon = 0.1
    #
    #     for passage1 in self.passages_allow:
    #         for passage2 in other.get_passages():
    #             line1, line2 = passage1.line, passage2.line
    #             x_min = min(passage1.x_min, passage2.x_min) + epsilon
    #             x_max = max(passage1.x_max, passage2.x_max) - epsilon
    #
    #             if you do_lines_intersect_in_x_range(line1, line2, x_min, x_max):
    #                 return False
    #     return True
