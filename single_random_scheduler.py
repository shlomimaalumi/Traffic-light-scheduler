import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Optional


class SingleRandomScheduler:

    @staticmethod
    def single_random_scheduler(intersection: Intersection) -> Optional[List[TrafficLight]]:
        """Decide which traffic light to switch on next based on a simple random selection.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light to switch on or None if no valid light is available.
        """
        light_traffics = intersection.get_all_traffic_lights()
        return [random.choice(light_traffics)]
