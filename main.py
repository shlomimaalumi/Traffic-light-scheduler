from control_loop import ControlLoop
from scheduler import Scheduler
from intersection import Intersection
from traffic_light import TrafficLight
from enums import *
from passage import Passage

if __name__ == '__main__':
    p1 = Passage((14, 8), (16, 10), PassageJam.MEDIUM)  # from Hashisha Asar right to Neve Yaakov
    p2 = Passage((14, 8), (10, 14), PassageJam.MEDIUM)  # from hashisha asar left to moshe dayan
    p3 = Passage((16, 13), (12, 8), PassageJam.MEDIUM)  # from neve yaakov left to hashisa asar
    p4 = Passage((16, 14), (10, 14), PassageJam.MEDIUM)  # from neve yaakov straight to moshe dayan
    p5 = Passage((10, 10), (12, 8), PassageJam.MEDIUM)  # from moshe dayan right to hashisa asar
    p6 = Passage((10, 10), (16, 10), PassageJam.MEDIUM)  # from moshe dayan straight to neve yaakov

    t1 = TrafficLight([p1, p2])
    t2 = TrafficLight([p5, p6])
    t3 = TrafficLight([p4])
    t4 = TrafficLight([p3])

    scheduler = Scheduler(SchedulerType.GREEDY_SCHEDULER)
    intersection = Intersection([t1, t2, t3, t4])
    run = ControlLoop(intersection, scheduler, 3)
    run.run()

