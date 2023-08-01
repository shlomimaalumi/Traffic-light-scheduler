import copy
from traffic_light import TrafficLight  # Importing TrafficLight for type hinting
from typing import List, Optional
from enums import TrafficLightState
from passage import Passage
from shapely.geometry import LineString


class Intersection:
    def __init__(self, traffic_lights: List[TrafficLight]):
        """Initialize an Intersection object with a list of traffic lights.

        Args:
            traffic_lights (list[TrafficLight]): A list of TrafficLight objects representing the traffic lights at the intersection.
        """
        self.traffic_lights = traffic_lights
        self.currennt_green_traffic_lighters = []
        self.currennt_main_traffic_light = None

    def get_current_green_light(self) -> Optional[TrafficLight]:
        """Get the currently active green traffic light.

        Returns:
            TrafficLight or None: The currently active green traffic light or None if there is no active green light.
        """
        return self.currennt_main_traffic_light

    def set_state_to_traffic_light(self, light_traffic: TrafficLight, state: TrafficLightState):
        """Set the state of a specific traffic light.

        Args:
            light_traffic (TrafficLight): The traffic light to change the state of.
            state (TrafficLightState): The new state for the traffic light.
        """
        if light_traffic not in self.traffic_lights:
            raise ValueError('Not a valid traffic light to switch to red.')
        light_traffic.set_state(state)

    def greens_on_for(self, lights_to_green: List[TrafficLight], main_light_traffic: TrafficLight, duration: float):
        """Set a list of traffic lights to green for a specified duration.

        Args:
            lights_to_green (List[TrafficLight]): The list of traffic lights to switch to green.
            main_light_traffic (TrafficLight): The main traffic light to be switched to green.
            duration (float): The duration for which the traffic lights will remain green (in seconds).
        """
        self.make_current_lighters_red()
        self.currennt_main_traffic_light = main_light_traffic
        for light in lights_to_green:
            light.green_on_for(duration)
            self.currennt_green_traffic_lighters.append(light)

    def make_current_lighters_red(self):
        """Set the currently active green traffic light and its associated traffic lights to red."""
        for light in self.currennt_green_traffic_lighters:
            light.red_on()
        self.currennt_green_traffic_lighters = []

    def red_on(self, light_traffic: TrafficLight):
        """Set a traffic light to red.

        Args:
            light_traffic (TrafficLight): The traffic light to switch to red.
        """
        if light_traffic not in self.traffic_lights:
            raise ValueError('Not a valid traffic light to switch to red.')
        light_traffic.red_on()
        # self.set_state_to_traffic_light(light_traffic, TrafficLightState.RED)

    def make_currnet_traffic_light_red(self):
        """Set the currently active green traffic light to red."""
        if self.currennt_main_traffic_light:
            self.red_on(self.currennt_main_traffic_light)

    def add_traffic_light(self, traffic_light: TrafficLight):
        """Add a traffic light to the intersection.

        Args:
            traffic_light (TrafficLight): The traffic light to add to the intersection.
        """
        self.traffic_lights.append(traffic_light)

    def add_traffic_lights(self, traffic_lights: List[TrafficLight]):
        """Add multiple traffic lights to the intersection.

        Args:
            traffic_lights (list[TrafficLight]): A list of TrafficLight objects to add to the intersection.
        """
        for t in traffic_lights:
            self.add_traffic_light(t)

    def get_all_traffic_lights(self) -> List[TrafficLight]:
        """Get a list of all traffic lights at the intersection.

        Returns:
            list[TrafficLight]: A list containing all the TrafficLight objects at the intersection.
        """
        return self.traffic_lights

    def get_copy_all_traffic_lights(self) -> List[TrafficLight]:
        """Get a deep copy list of all traffic lights at the intersection.

        Returns:
            list[TrafficLight]: A list containing all the TrafficLight objects at the intersection.
        """
        return copy.deepcopy(self.traffic_lights)

    def get_remaining_time(self) -> Optional[float]:
        """Get the remaining time for the current green traffic light.

        Returns:
            float: The remaining time (in seconds) for the current green traffic light.
            Returns negative infinity if there's no current green light.
        """
        if not self.currennt_main_traffic_light:
            return
        return self.currennt_main_traffic_light.get_remaining_duration()

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
    def can_work_together(list1: List[Passage], list2: List[Passage]) -> bool:
        """
        Check if two lists of passages can work together without any overlapping.

        Args:
            list1 (List[Passage]): The first list of passages.
            list2 (List[Passage]): The second list of passages.

        Returns:
            bool: True if the two lists can work together without overlapping, False otherwise.
        """

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
                if Intersection.do_lines_intersect_in_x_range(line1, line2, start_x, end_x):
                    return False
        return True

    @staticmethod
    def is_action_valid(action: List[Passage]) -> bool:
        """
        Check if a list of passages can form a valid action without any overlapping.

        Args:
            action (List[Passage]): The list of passages representing the action.

        Returns:
            bool: True if the action is valid (no overlapping passages), False otherwise.
        """
        for p1 in action:
            for p2 in action:
                if p2 != p1 and not Intersection.can_work_together([p1], [p2]):
                    return False
        return True
