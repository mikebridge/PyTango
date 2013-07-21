from unittest import TestCase
from grid import Grid
from collider import WallCollider

__author__ = 'Mike Bridge'


class TestWallCollider(TestCase):

    def setUp(self):
        self.fakegrid = Grid((3,3), [])
        self.collider = WallCollider()

    def test_origin_will_not_result_in_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (0, 0))
        self.assertFalse(result)

    def test_off_left_will_result_in_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (-1, 0))
        self.assertTrue(result)

    def test_off_top_will_result_in_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (0, -1))
        self.assertTrue(result)

    def test_off_bottom_will_result_in_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (0, 3))
        self.assertTrue(result)

    def test_off_right_will_result_in_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (3, 0))
        self.assertTrue(result)

    def test_on_right_border_is_not_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (2, 0))
        self.assertFalse(result)

    def test_on_bottom_border_is_not_collision(self):
        result = self.collider.will_result_in_collision(self.fakegrid, (0, 2))
        self.assertFalse(result)