from control_loop import ControlLoop
from random_scheduler import SimpleScheduler
from intersection import Intersection
from traffic_light import TrafficLight

if __name__ == '__main__':
    t1 = TrafficLight([])  # Create a new instance of TrafficLight
    t2 = TrafficLight([])
    t3 = TrafficLight([])
    t4 = TrafficLight([])
    t5 = TrafficLight([])
    t6 = TrafficLight([])

    scheduler = SimpleScheduler()
    intersection = Intersection([t1, t2, t3, t4, t5, t6])
    run = ControlLoop(intersection, scheduler)
    run.run()
