from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Optional
from enums import SchedulerType
from single_random_scheduler import SingleRandomScheduler
from random_scheduler import RandomScheduler
from greedy_scheduler import GreedyScheduler


class Scheduler:
    """A class for managing traffic light scheduling based on different scheduler types."""

    navigate_scheduler = {
        SchedulerType.SINGLE_RANDOM_SCHEDULER: SingleRandomScheduler.single_random_scheduler,
        SchedulerType.RANDOM_SCHEDULER: RandomScheduler.random_scheduler,
        SchedulerType.GREEDY_SCHEDULER: GreedyScheduler.greedy_scheduler
    }

    def __init__(self, scheduler_type: SchedulerType):
        """
        Initialize a scheduler object.

        Args:
            scheduler_type (SchedulerType): The type of scheduler to use.
        """
        self.scheduler_type = scheduler_type

    def decide_next_light(self, intersection: Intersection) -> Optional[List[TrafficLight]]:
        """
        Decide which traffic light(s) to switch on next based on the selected scheduler.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light(s) to switch on or None if no valid light is available.
        """
        return Scheduler.navigate_scheduler[self.scheduler_type](intersection)

    @staticmethod
    def time_to_swap(intersection: Intersection) -> bool:
        """
        Check if it's time to swap to the next traffic light.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            bool: True if it's time to swap to the next traffic light, False otherwise.
        """
        return not intersection.get_remaining_time() or intersection.get_remaining_time() <= 0
