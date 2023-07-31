import unittest
from typing import Tuple
from passage import Passage
from traffic_light import TrafficLight


class TestTrafficLight(unittest.TestCase):
    def setUp(self):
        # Define some passages for testing
        self.passage1 = Passage((0, 0), (5, 0))
        self.passage2 = Passage((3, 2), (8, 2))
        self.passage3 = Passage((10, 0), (15, 0))
        self.passage4 = Passage((2, 2), (4, 2))
        self.passage5 = Passage((7, -1), (12, -1))
        self.passage6 = Passage((-2, -2), (-1, -1))
        self.passage7 = Passage((0, 0), (0, 5))
        self.passage8 = Passage((0, 0), (10, 10))  # Passage with the same slope and on the same line as passage1

        # Traffic lights with different passages
        self.traffic_light1 = TrafficLight([self.passage1, self.passage3, self.passage4])
        self.traffic_light2 = TrafficLight([self.passage2, self.passage4, self.passage5])
        self.traffic_light3 = TrafficLight([self.passage1, self.passage5])
        self.traffic_light4 = TrafficLight([self.passage1, self.passage2, self.passage3])
        self.traffic_light5 = TrafficLight([self.passage4])
        self.traffic_light6 = TrafficLight([self.passage6, self.passage7])
        self.traffic_light7 = TrafficLight([self.passage1, self.passage3, self.passage4])
        self.traffic_light8 = TrafficLight([self.passage1, self.passage2, self.passage3, self.passage8])

    def test_can_work_with_no_overlap(self):
        # Traffic light 1 and traffic light 6 have no overlapping passages,
        # so they should be able to work together
        self.assertTrue(self.traffic_light1.can_work_with(self.traffic_light6))

    def test_can_work_with_same_traffic_light(self):
        # Traffic light 1 should be able to work with itself
        self.assertTrue(self.traffic_light1.can_work_with(self.traffic_light1))

    def test_can_work_with_one_passage_overlap(self):
        # Traffic light 1 and traffic light 3 have one overlapping passage,
        # so they should still be able to work together
        self.assertTrue(self.traffic_light1.can_work_with(self.traffic_light3))

    def test_can_work_with_fully_contained_passage(self):
        # Traffic light 1 and traffic light 4 have fully contained passages,
        # so they should not be able to work together
        self.assertFalse(self.traffic_light1.can_work_with(self.traffic_light4))


    def test_can_work_with_complex_overlapping_passages(self):
        # Traffic light 2 and traffic light 3 have complex overlapping passages,
        # but they should still be able to work together
        self.assertTrue(self.traffic_light2.can_work_with(self.traffic_light3))

    def test_can_work_with_same_passages_different_points(self):
        # Traffic light 1 and traffic light 8 have the same passages with different points,
        # but they should not be able to work together because the passages have the same slope and are on the same line
        self.assertFalse(self.traffic_light1.can_work_with(self.traffic_light8))


if __name__ == '__main__':
    unittest.main()
