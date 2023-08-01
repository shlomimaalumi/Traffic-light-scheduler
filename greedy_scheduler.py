from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple


class GreedyScheduler:

    @staticmethod
    def decide_next_step(intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight], float]:
        traffic_lights = intersection.get_copy_all_traffic_lights()
        traffic_lights_sorted = sorted(traffic_lights, key=lambda tl: tl.get_traffic_light_jam(), reverse=True)
        main_traffic_light = traffic_lights_sorted.pop(0)

        next_lights = GreedyScheduler.max_scheduling([main_traffic_light], traffic_lights_sorted)
        # duration = main_traffic_light.average_jam_time()
        duration = GreedyScheduler.calculate_duration(traffic_lights_sorted)
        return main_traffic_light, next_lights, duration

    @staticmethod
    def calculate_duration( traffic_lights: List[TrafficLight]) -> float:
        lst = []
        val=0
        for index, tl in enumerate(traffic_lights):
            for p in tl.passages_allow:
                if p not in lst:
                    lst.append(p)
                    val += (len(traffic_lights)-index) * 0.5*p.rate.value
        return val

    @staticmethod
    def max_scheduling(cur_light_traffics: List[TrafficLight], remaining_light_traffics: List[TrafficLight]) -> List[TrafficLight]:
        for tl in remaining_light_traffics:
            optional_addition = cur_light_traffics + [tl]
            if TrafficLight.can_work_together(optional_addition):
                cur_light_traffics = optional_addition
        return cur_light_traffics
