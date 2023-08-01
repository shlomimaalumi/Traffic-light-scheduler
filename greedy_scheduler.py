from intersection import Intersection
from traffic_light import TrafficLight
from typing import List, Optional


class GreedyScheduler:

    @staticmethod
    def greedy_scheduler(intersection: Intersection) -> Optional[List[TrafficLight]]:
        return

#
# from dataclasses import dataclass
# from enum import Enum
#
#
# class TrafficLightState(Enum):
#     RED = 0
#     GREEN = 1
#
#
# @dataclass(frozen=True)
# class TrafficLightData:
#     id: int
#     state: TrafficLightState = TrafficLightState.RED
#     jam: float = 0.0
#     remaining_green: float = 0.0
#     time_since_last_green: float = 0.0
#
#
# class TrafficLight:
#     def __init__(self, id) -> None:
#         ...
#
#     def get_immutable_data(self) -> TrafficLightData:
#         ...
#
#     def set_state(self, state: TrafficLightState) -> None:
#         ...
#
#
# @dataclass(frozen=True)
# class IntersectionData:
#     id: int
#     traffic_lights: "list[TrafficLightData]"
#
#
# class Intersection:
#     def __init__(self, id, traffic_lights) -> None:
#         ...
#
#     def get_immutable_data(self) -> IntersectionData:
#         ...
#
#
# class Controller:
#     def __init__(self, algo, intersections: Intersection, steps: 'int | None' = None) -> None:
#         self._steps = steps or float("inf")
#         self._current_step = 0
#
#         self._algo = algo
#         self._intersections = intersections
#
#     def run(self) -> None:
#         while self._current_step < self._steps:
#             self._current_step += 1
#             self.step()
#
#     def step(self) -> None:
#         action = self._algo.decide(self._intersections.get_immutable_data())
#         assert self.is_action_valid(action), "Got invalid action from algo"
#         self._apply_action(action)
#
#     def _apply_action(self, action) -> None:
#         ...
#
#     def is_action_valid(self, action):
#         ...
