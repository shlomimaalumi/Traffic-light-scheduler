import random
from intersection import Intersection  # Importing Intersection for type hinting
from traffic_light import TrafficLight  # Importing TrafficLight for type hinting
from typing import List


class SimpleScheduler:
    def __init__(self):
        """Initialize a SimpleScheduler object."""
        pass

    @staticmethod
    def decide_next_light(intersection: Intersection) -> List[TrafficLight] or None:
        """Decide which traffic light to switch on next based on a simple random selection.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            TrafficLight or None: The next traffic light to switch on or None if no valid light is available.
        """
        light_traffics = intersection.get_all_traffic_lights()
        return [random.choice(light_traffics)]

    @staticmethod
    def time_to_swap(intersection: Intersection) -> bool:
        """Check if it's time to swap to the next traffic light.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            bool: True if it's time to swap to the next traffic light, False otherwise.
        """
        return not intersection.get_remaining_time() or intersection.get_remaining_time() <= 0
