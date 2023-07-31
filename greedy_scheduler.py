import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Optional


class GreedyScheduler:

    @staticmethod
    def greedy_scheduler(intersection: Intersection) -> Optional[List[TrafficLight]]:
        return