import unittest
from traffic_light import TrafficLight, Passage
from intersection import Intersection
from scheduler import Scheduler
from control_loop import ControlLoop
from enums import TrafficLightState


class TestTrafficLightSystem(unittest.TestCase):
    def setUp(self):
        self.passage1 = Passage((0, 0), (5, 0))
        self.passage2 = Passage((5, 0), (5, 5))
        self.passage3 = Passage((5, 5), (0, 5))
        self.passage4 = Passage((0, 5), (0, 0))
        self.traffic_light1 = TrafficLight([self.passage1, self.passage4])
        self.traffic_light2 = TrafficLight([self.passage2, self.passage3])
        self.intersection = Intersection([self.traffic_light1, self.traffic_light2])
        self.scheduler = Scheduler()
        self.control_loop = ControlLoop(self.intersection, self.scheduler)

    def test_traffic_light_states(self):
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)
        self.assertEqual(self.traffic_light2.get_state(), TrafficLightState.RED)

        self.intersection.greens_on_for([self.traffic_light1], self.traffic_light1, 2.5)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.GREEN)
        self.assertEqual(self.traffic_light2.get_state(), TrafficLightState.RED)

        self.intersection.greens_on_for([self.traffic_light2], self.traffic_light2, 2.5)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)
        self.assertEqual(self.traffic_light2.get_state(), TrafficLightState.GREEN)

        # Check traffic light state transitions
        self.traffic_light1.red_on()
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)
        self.traffic_light1.green_on_for(3.0)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.GREEN)
        self.traffic_light1.red_on()
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

    def test_scheduler(self):
        next_lights = self.scheduler.decide_next_light(self.intersection)
        self.assertIn(next_lights[0], [self.traffic_light1, self.traffic_light2])

    def test_intersection_add_traffic_light(self):
        new_traffic_light = TrafficLight([self.passage1, self.passage2])
        self.intersection.add_traffic_light(new_traffic_light)
        self.assertIn(new_traffic_light, self.intersection.get_all_traffic_lights())

    def test_intersection_add_traffic_lights(self):
        new_traffic_light1 = TrafficLight([self.passage1, self.passage2])
        new_traffic_light2 = TrafficLight([self.passage3, self.passage4])
        self.intersection.add_traffic_lights([new_traffic_light1, new_traffic_light2])
        self.assertIn(new_traffic_light1, self.intersection.get_all_traffic_lights())
        self.assertIn(new_traffic_light2, self.intersection.get_all_traffic_lights())

    def test_intersection_get_remaining_time(self):
        self.assertIsNone(self.intersection.get_remaining_time())

        # Make traffic_light1 green for 3 seconds
        self.intersection.greens_on_for([self.traffic_light1], self.traffic_light1, 3.0)
        self.assertGreaterEqual(self.intersection.get_remaining_time(), 0.0)
        self.assertLessEqual(self.intersection.get_remaining_time(), 3.0)

        # Make traffic_light2 green for 2 seconds
        self.intersection.greens_on_for([self.traffic_light2], self.traffic_light2, 2.0)
        self.assertGreaterEqual(self.intersection.get_remaining_time(), 0.0)
        self.assertLessEqual(self.intersection.get_remaining_time(), 2.0)

    # def test_control_loop(self):
    #     # Test if the control loop runs without errors for 3 iterations
    #     for _ in range(3):
    #         self.control_loop.run()

    # def test_intersection_intersection(self):
    #     # Test if the traffic lights in the intersection can work together
    #     self.assertTrue(self.traffic_light1.can_work_with(self.traffic_light2))
    #
    #     # Make traffic_light1 green for 3 seconds
    #     self.intersection.greens_on_for([self.traffic_light1], self.traffic_light1, 3.0)
    #
    #
    #     # Make traffic_light2 green for 2 seconds
    #     self.intersection.greens_on_for([self.traffic_light2], self.traffic_light2, 2.0)
    #
    #     # Now, traffic_light1 should work with traffic_light2 again
    #     self.assertTrue(self.traffic_light1.can_work_with(self.traffic_light2))

    def test_intersection_get_current_green_light(self):
        # Initially, no green light
        self.assertIsNone(self.intersection.get_current_green_light())

        # Make traffic_light1 green for 3 seconds
        self.intersection.greens_on_for([self.traffic_light1], self.traffic_light1, 3.0)
        self.assertEqual(self.intersection.get_current_green_light(), self.traffic_light1)

        # Make traffic_light2 green for 2 seconds
        self.intersection.greens_on_for([self.traffic_light2], self.traffic_light2, 2.0)
        self.assertEqual(self.intersection.get_current_green_light(), self.traffic_light2)

    def test_intersection_set_state_to_traffic_light(self):
        # Initially, traffic_light1 is RED
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

        # Change traffic_light1 state to GREEN
        self.intersection.set_state_to_traffic_light(self.traffic_light1, TrafficLightState.GREEN)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.GREEN)

        # Change traffic_light1 state back to RED
        self.intersection.set_state_to_traffic_light(self.traffic_light1, TrafficLightState.RED)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

    def test_intersection_make_current_lighters_red(self):
        # Initially, no green light
        self.assertIsNone(self.intersection.get_current_green_light())

        # Make traffic_light1 green for 3 seconds
        self.intersection.greens_on_for([self.traffic_light1], self.traffic_light1, 3.0)
        self.assertEqual(self.intersection.get_current_green_light(), self.traffic_light1)

        # Make all current lighters red
        self.intersection.make_current_lighters_red()
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

    def test_traffic_light_green_on_for(self):
        # Initially, traffic_light1 is RED
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

        # Make traffic_light1 green for 3 seconds
        self.traffic_light1.green_on_for(3.0)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.GREEN)

        # Check if the remaining duration is approximately 3 seconds
        self.assertAlmostEqual(self.traffic_light1.get_remaining_duration(), 3.0, delta=0.1)

    def test_traffic_light_red_on(self):
        # Initially, traffic_light1 is RED
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

        # Make traffic_light1 green for 3 seconds
        self.traffic_light1.green_on_for(3.0)
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.GREEN)

        # Make traffic_light1 red
        self.traffic_light1.red_on()
        self.assertEqual(self.traffic_light1.get_state(), TrafficLightState.RED)

    def test_traffic_light_get_traffic_jam(self):
        # Initially, no traffic jam
        self.assertEqual(self.traffic_light1.get_traffic_jam(), 0)

        # Increase traffic jam count to 5
        self.traffic_light1.traffic_jam = 5
        self.assertEqual(self.traffic_light1.get_traffic_jam(), 5)

    def test_traffic_light_get_id(self):
        # Check if traffic_light1 has a valid ID (greater than 0)
        self.assertGreater(self.traffic_light1.get_id(), 0)

    def test_passage(self):
        # Check passage coordinates
        self.assertEqual(self.passage1.source, (0, 0))
        self.assertEqual(self.passage1.target, (5, 0))

        # Check passage line
        self.assertEqual(self.passage1.line.coords[:], [(0, 0), (5, 0)])

        # Check x and y ranges of the passage
        self.assertEqual(self.passage1.x_min, 0)
        self.assertEqual(self.passage1.x_max, 5)



if __name__ == '__main__':
    unittest.main()
