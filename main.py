from control_loop import ControlLoop
from scheduler import Scheduler
from intersection import Intersection
from traffic_light import TrafficLight
from enums import *
if __name__ == '__main__':
    t1 = TrafficLight([])  # Create a new instance of TrafficLight
    t2 = TrafficLight([])
    t3 = TrafficLight([])
    t4 = TrafficLight([])
    t5 = TrafficLight([])
    t6 = TrafficLight([])

    scheduler = Scheduler(SchedulerType.SINGLE_RANDOM_SCHEDULER)
    intersection = Intersection([t1, t2, t3, t4, t5, t6])
    run = ControlLoop(intersection, scheduler)
    run.run()
