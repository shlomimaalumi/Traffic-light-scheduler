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
