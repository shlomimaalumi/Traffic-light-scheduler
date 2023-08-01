import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple


class SingleRandomScheduler:

    @staticmethod
    def decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight]]:
        """
        Decide which traffic light to switch on next based on a simple random selection.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            Tuple[TrafficLight, List[TrafficLight]] or None: A tuple containing the main traffic light to make green
            and a list with only the main traffic light. If no valid light is available, returns None.
        """
        light_traffics = intersection.get_all_traffic_lights()
        main_traffic_light = random.choice(light_traffics)
        return main_traffic_light, [main_traffic_light]
