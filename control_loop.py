from intersection import Intersection  # Importing Intersection for type hinting
from scheduler import Scheduler  # Importing Scheduler for type hinting


class ControlLoop:
    def __init__(self, intersection: Intersection, scheduler: Scheduler):
        """Initialize a MainRunning object.

        Args:
            intersection (Intersection): The intersection object to control the traffic lights.
            scheduler (Scheduler): The scheduler to decide the next traffic light.
        """
        self.intersection = intersection
        # intersection.add_traffic_lights()
        self.scheduler = scheduler

    def run(self):
        """Start the traffic light control loop."""
        while True:
            if Scheduler.time_to_swap(self.intersection):
                next_lights = self.scheduler.decide_next_light(self.intersection)
                self.intersection.make_currnet_traffic_light_red()
                self.intersection.greens_on_for(next_lights, next_lights[0], 2.5)
