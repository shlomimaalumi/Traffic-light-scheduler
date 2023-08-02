from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Tuple
from enums import SchedulerType
from single_random_scheduler import SingleRandomScheduler
from random_scheduler import RandomScheduler
from greedy_scheduler import GreedyScheduler


class Scheduler:
    """A class for managing traffic light scheduling based on different scheduler types."""

    navigate_scheduler = {
        SchedulerType.SINGLE_RANDOM_SCHEDULER: SingleRandomScheduler,
        SchedulerType.RANDOM_SCHEDULER: RandomScheduler,
        SchedulerType.GREEDY_SCHEDULER: GreedyScheduler
    }

    def __init__(self, scheduler_type: SchedulerType):
        """
        Initialize a scheduler object.

        Args:
            scheduler_type (SchedulerType): The type of scheduler to use.
        """
        self.step = 0
        self.scheduler_type = scheduler_type

    def decide_next_light(self, intersection: Intersection) -> Tuple[TrafficLight, List[TrafficLight], float]:
        """
        Decide which traffic light(s) to switch on next based on the selected scheduler.

        Args:
            intersection (Intersection): The intersection where the traffic lights are located.

        Returns:
            Tuple[TrafficLight, List[TrafficLight]] or None: A tuple containing the main traffic light to make green
            and a list of other traffic lights to make green together. If no valid light is available, returns None.
        """
        self.step += 1
        result = Scheduler.navigate_scheduler[self.scheduler_type].decide_next_step(intersection)
        if len(result) == 2:
            return result + (0,)  # the duration decided on the init of the system
        return result

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

    def get_step_number(self) -> int:
        """Get the step coutner of the scheduler.

            Returns:
                int: The number of the steps."""
        return self.step

