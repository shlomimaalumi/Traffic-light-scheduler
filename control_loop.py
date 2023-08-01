from intersection import Intersection  # Importing Intersection for type hinting
from scheduler import Scheduler  # Importing Scheduler for type hinting


class ControlLoop:
    def __init__(self, intersection: Intersection, scheduler: Scheduler, duration=3):
        """Initialize a MainRunning object.

        Args:
            intersection (Intersection): The intersection object to control the traffic lights.
            scheduler (Scheduler): The scheduler to decide the next traffic light.
        """
        self.intersection = intersection
        self.scheduler = scheduler
        self.duration = duration

    def run(self):
        """Start the traffic light control loop."""
        while True:
            if Scheduler.time_to_swap(self.intersection):
                next_lights = self.scheduler.decide_next_light(self.intersection)
                self.intersection.make_current_lighters_red()
                print(f"*******************iteration number {self.scheduler.get_step_number()}****************")
                self.intersection.greens_on_for(next_lights[1], next_lights[0], self.duration)
