from enum import Enum


class TrafficLightState(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class SchedulerType(Enum):
    SINGLE_RANDOM_SCHEDULER = 1
    RANDOM_SCHEDULER = 2
    GREEDY_SCHEDULER = 3


class PassageJam(Enum):
    EXTREME_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    EXTREME_HIGH = 5
