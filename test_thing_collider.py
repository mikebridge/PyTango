from unittest import TestCase
from collider import ThingCollider
from grid import Grid

__author__ = 'Mike Bridge'


class TestThingCollider(TestCase):

    def setUp(self):
        self.fakegrid = Grid((3,3), [])
        self.collider = ThingCollider()

    def test_same_place_will_result_in_collision(self):
        coord = (2,2)
        self.fakegrid.place_new(coord, 1)
        collision = self.collider.will_result_in_collision(self.fakegrid, coord)
        self.assertTrue(collision)

    def test_different_place_will_not_result_in_collision(self):
        grid = Grid((3,3), [])
        grid.place_new((2,2), 1)
        collision = self.collider.will_result_in_collision(self.fakegrid, (1, 2))
        self.assertFalse(collision)

    def test_off_board_is_not_collision(self):
        self.fakegrid.place_new((2,2), 1)
        collision = self.collider.will_result_in_collision(self.fakegrid, (5,5))
        self.assertFalse(collision)
