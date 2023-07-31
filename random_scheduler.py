import random
from intersection import Intersection
from traffic_light import TrafficLight
from typing import List
from enums import SchedulerType


class SimpleScheduler:
    # nevigate_scheduler = {
    #     SchedulerType.RANDOM_SCHEDULER: SimpleScheduler.random_scheduler,
    #     SchedulerType.GREEDY_SCHEDULER: SimpleScheduler.greedy_scheduler
    # }

    def __init__(self, scheduler_type: SchedulerType):
        """Initialize a scheduler object."""
        self.scheduler_type = scheduler_type

    def decide_next_light(self, intersection: Intersection) -> List[TrafficLight] or None:
        """Decide which traffic light to switch on next based on the selected scheduler type.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light to switch on or None if no valid light is available.
        """
        return self._get_scheduler_function().get(self.scheduler_type)(intersection)

    @staticmethod
    def _get_scheduler_map():
        """Return the scheduler function based on the selected scheduler type."""
        return {
            SchedulerType.SINGLE_RANDOM_SCHEDULER: SimpleScheduler.single_random_scheduler,
            SchedulerType.RANDOM_SCHEDULER: SimpleScheduler.random_scheduler,
            SchedulerType.GREEDY_SCHEDULER: SimpleScheduler.greedy_scheduler
        }

    @staticmethod
    def single_random_scheduler(intersection: Intersection) -> List[TrafficLight] or None:
        """Decide which traffic light to switch on next based on a simple random selection.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light to switch on or None if no valid light is available.
        """
        light_traffics = intersection.get_all_traffic_lights()
        return [random.choice(light_traffics)]

    @staticmethod
    def random_scheduler(intersection: Intersection) -> List[TrafficLight] or None:
        """Decide which traffic lights to switch on next based on a simple random selection and the lighters
         that should work at the same time.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            List[TrafficLight] or None: The next traffic light to switch on or None if no valid light is available.
        """
        light_traffics = intersection.get_all_traffic_lights()
        return [random.choice(light_traffics)]

    @staticmethod
    def greedy_scheduler(intersection: Intersection) -> List[TrafficLight] or None:
        pass

    @staticmethod
    def time_to_swap(intersection: Intersection) -> bool:
        """Check if it's time to swap to the next traffic light.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            bool: True if it's time to swap to the next traffic light, False otherwise.
        """
        return not intersection.get_remaining_time() or intersection.get_remaining_time() <= 0
