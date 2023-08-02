import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple


class RandomScheduler:
    """
    A class that implements a random traffic light scheduler with intersection-based constraints.

    The RandomScheduler class randomly selects one traffic light from the intersection
    to turn green at each iteration, while ensuring that the selected traffic light does not intersect
    with other traffic lights in the scheduling.


    Methods:
        decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight]]:
            Decide the next traffic light to turn green based on a simple random selection,
            and add some other traffic lights that don't intersect with the main light.

        max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
            Recursively find the maximum number of traffic lights that can be scheduled together
            without intersections.
    """

    @staticmethod
    def decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight]]:
        """
        Decide which traffic light to switch on next based on a simple random selection,
        and add some other traffic lights that don't intersect with the main light.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            Tuple[TrafficLight, List[TrafficLight]] or None:
                A tuple containing the main traffic light to make green and a list of other traffic lights
                that don't intersect with the main light. If no valid light is available, returns None.
        """

        light_traffics = intersection.get_copy_all_traffic_lights()
        main_traffic_light = random.choice(light_traffics)
        light_traffics.remove(main_traffic_light)

        return main_traffic_light, RandomScheduler.max_scheduling([main_traffic_light], light_traffics)

    @staticmethod
    def max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
        """
        Recursively find the maximum number of traffic lights that can be scheduled together without intersections.

        This method iterates through the remaining traffic lights and builds a set of traffic lights
        that can work together without overlapping.

        Args:
            cur_light_traffics (List[TrafficLight]): The list of traffic lights that have already been scheduled.
            remaining_light_traffics (List[TrafficLight]): The list of remaining traffic lights to consider.

        Returns:
            List[TrafficLight]: A list of traffic lights that can work together without conflicts.
        """

        for tl in remaining_light_traffics:
            optional_addition = cur_light_traffics + [tl]
            if TrafficLight.can_work_together(optional_addition):
                cur_light_traffics = optional_addition
        return cur_light_traffics
