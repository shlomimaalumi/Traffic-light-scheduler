from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple


class GreedyScheduler:
    """
    A class that implements a greedy traffic light scheduling algorithm.

    The GreedyScheduler class decides the next traffic light to turn green using a greedy approach
    that maximizes the expected impact on traffic flow while avoiding conflicts.


    Methods:
        decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight], float]:
            Decide the next traffic light to turn green and calculate the duration for which it will remain green.

        calculate_duration(traffic_lights: List[TrafficLight]) -> float:
            Calculate the duration for which the main traffic light should remain green based on jam values.

        max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
            Find the set of traffic lights that can work together without conflicts.
    """

    @staticmethod
    def decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight], float]:
        """
        Decide the next traffic light to turn green and calculate the duration for which it will remain green.

        This method uses a greedy approach to select the main traffic light to turn green and calculates
        the duration based on jam values of traffic lights.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            Tuple[TrafficLight, List[TrafficLight], float]:
                A tuple containing:
                - The main traffic light to make green.
                - A list of other traffic lights that can work together without conflicts.
                - The duration for which the main traffic light should remain green.
        """
        traffic_lights = intersection.get_all_traffic_lights()[:]
        traffic_lights_sorted = sorted(traffic_lights, key=lambda tl: tl.get_traffic_light_jam(), reverse=True)
        main_traffic_light = traffic_lights_sorted.pop(0)

        next_lights = GreedyScheduler.max_scheduling([main_traffic_light], traffic_lights_sorted)
        duration = GreedyScheduler.calculate_duration(traffic_lights_sorted)
        return main_traffic_light, next_lights, duration

    @staticmethod
    def calculate_duration(traffic_lights: List[TrafficLight]) -> float:
        """
        Calculate the duration for which the main traffic light should remain green based on jam values.

        The duration is calculated based on the sum of jam values of passages in the traffic lights.

        Args:
            traffic_lights (List[TrafficLight]): A list of traffic lights.

        Returns:
            float: The duration for which the main traffic light should remain green.
        """
        lst = []
        val = 0
        for index, tl in enumerate(traffic_lights):
            for p in tl.passages_allow:
                if p not in lst:
                    lst.append(p)
                    val += (len(traffic_lights) - index) * 0.5 * p.rate.value
        return val

    @staticmethod
    def max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
        """
        Find the set of traffic lights that can work together without conflicts.

        This method iterates through the remaining traffic lights and builds a set of traffic lights
        that can work together without overlapping.

        Args:
            cur_light_traffics (List[TrafficLight]): The list of traffic lights that can currently work together.
            remaining_light_traffics (List[TrafficLight]): The list of remaining traffic lights to consider.

        Returns:
            List[TrafficLight]: A list of traffic lights that can work together without conflicts.
        """
        for tl in remaining_light_traffics:
            optional_addition = cur_light_traffics + [tl]
            if TrafficLight.can_work_together(optional_addition):
                cur_light_traffics = optional_addition
        return cur_light_traffics

