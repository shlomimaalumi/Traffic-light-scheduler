from intersection import Intersection  # Importing Intersection for type hinting
from scheduler import Scheduler  # Importing Scheduler for type hinting
import time


# import platform

# if platform.system() == "Windows":
#     import msvcrt
# import sys
# import select


class ControlLoop:
    def __init__(self, intersection: Intersection, scheduler: Scheduler, duration=0):
        """Initialize a MainRunning object.

        Args:
            intersection (Intersection): The intersection object to control the traffic lights.
            scheduler (Scheduler): The scheduler to decide the next traffic light.
        """
        self.intersection = intersection
        self.scheduler = scheduler
        self.duration = duration

    #
    #
    # def handle_user_input(self):
    #     # Check if input is available (Windows only)
    #     if sys.platform == "win32":
    #         if msvcrt.kbhit():
    #             key = msvcrt.getch().decode('utf-8')
    #             if key == 's':
    #                 passage_id = input("Please enter the passage ID: ")
    #                 if passage_id.isdigit():
    #                     self.call_function_with_passage_id(int(passage_id))
    #                 else:
    #                     print("Invalid passage ID. Please enter a valid number.")
    #     # For Unix-based systems, use input() function
    #     else:
    #         key = input("Please press 's' to continue: ")
    #         if key == 's':
    #             passage_id = input("Please enter the passage ID: ")
    #             if passage_id.isdigit():
    #                 self.call_function_with_passage_id(int(passage_id))
    #             else:
    #                 print("Invalid passage ID. Please enter a valid number.")

    # def call_function_with_passage_id(self, passage_id):
    #     # Replace this function with your desired logic to handle the passage ID
    #     print(f"Calling function with passage ID: {passage_id}")

    def run(self):
        """Start the traffic light control loop."""
        while True:
            # if self.intersection.passage_interupt():
            # self.handle_user_input()
            if Scheduler.time_to_swap(self.intersection):
                self.intersection.make_current_lighters_red()
                next_lights = self.scheduler.decide_next_light(self.intersection)
                print(f"*******iteration number {self.scheduler.get_step_number()} in time: {int(time.time())}********")
                duration = self.duration if next_lights[2] == 0 else next_lights[2]
                self.intersection.greens_on_for(next_lights[1], next_lights[0], duration)

