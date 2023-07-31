import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Optional


class RandomScheduler:

    @staticmethod
    def random_scheduler(intersection: Intersection) -> Optional[List[TrafficLight]]:
        """Decide which traffic light to switch on next based on a simple random selection,
        and add some other traffic lights taht doesn't intersect.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light to switch on or None if no valid light is available.
        """
        return

