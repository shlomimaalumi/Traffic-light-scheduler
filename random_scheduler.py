import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple


class RandomScheduler:

    @staticmethod
    def random_scheduler(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight]]:
        """
        Decide which traffic light to switch on next based on a simple random selection,
        and add some other traffic lights that don't intersect.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            Tuple[TrafficLight, List[TrafficLight]] or None: A tuple containing the main traffic light to make green
            and a list of other traffic lights that don't intersect with the main light. If no valid light is available,
            returns None.
        """

        light_traffics = intersection.get_copy_all_traffic_lights()
        main_traffic_light = random.choice(light_traffics)
        light_traffics.remove(main_traffic_light)
        if main_traffic_light.id==2:
            x=4
        return main_traffic_light, RandomScheduler.max_scheduling([main_traffic_light], light_traffics)

    @staticmethod
    def max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
        for lt in remaining_light_traffics:
            optional_addition = cur_light_traffics + [lt]
            if TrafficLight.can_work_together(optional_addition):
                remaining_light_traffics.remove(lt)
                return RandomScheduler.max_scheduling(optional_addition, remaining_light_traffics)
        return cur_light_traffics
