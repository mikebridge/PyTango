from unittest import TestCase
from collider import *

from grid import Grid

__author__ = 'Mike Bridge'

class TestGrid(TestCase):

    def setUp(self):
        self.test_grid = self.create_grid(3,3)

    def test_new_grid_should_be_empty(self):
        self.assertFalse([v for k,v in self.test_grid.to_dict().items() if v != 0])

    def test_id_placed_on_grid(self):
        self.test_grid.place_new((1,1), 3)
        testdict = self.test_grid.to_dict()[(1,1)]
        self.assertEquals(testdict,3)

    def test_width(self):
        grid = self.create_grid(3,5)
        self.assertEquals(grid.width,3)

    def test_height(self):
        grid = self.create_grid(3,5)
        self.assertEquals(grid.height,5)


    def test_current_pos_is_initialized(self):
        self.test_grid.place_new((1,2), 3)
        pos = self.test_grid.current_pos(3)
        self.assertEquals(pos,(1,2))

    def test_move_left_returns_current_pos(self):
        self.place_center(3)
        new_pos = self.test_grid.move_left(3)
        self.assertEquals(new_pos,(0,1))

    def test_move_left_updates_current_pos(self):
        self.place_center(3)
        self.test_grid.move_left(3)
        new_pos = self.test_grid.current_pos(3)
        self.assertEquals(new_pos,(0,1))

    def test_move_right_updates_current_pos(self):
        self.place_center(3)
        self.test_grid.move_right(3)
        new_pos = self.test_grid.current_pos(3)
        self.assertEquals(new_pos,(2,1))

    def test_move_up_updates_current_pos(self):
        self.place_center(3)
        self.test_grid.move_up(3)
        new_pos = self.test_grid.current_pos(3)
        self.assertEquals(new_pos,(1,0))

    def test_move_down_updates_current_pos(self):
        self.place_center(3)
        self.test_grid.move_down(3)
        new_pos = self.test_grid.current_pos(3)
        self.assertEquals(new_pos,(1,2))

    def test_move_down_keeps_old_pos_too(self):
        self.place_center(3)
        self.test_grid.move_down(3)
        self.test_grid.current_pos(3)
        last_id = self.test_grid.id_at((1,1))
        self.assertEquals(3, last_id)

    def test_move_into_wall_results_in_collision(self):
        self.assertFalse(self.test_grid.was_collision())
        self.test_grid.place_new((0,0), 3)
        self.test_grid.move_left(3)
        self.assertTrue(self.test_grid.was_collision())

    def test_move_into_wall_registers_collision_by_id(self):
        self.test_grid.place_new((0,0), 3)
        self.test_grid.move_left(3)
        self.assertEquals(self.test_grid.who_collided(), {3})

    def test_same_place_will_result_in_collision(self):
        self.test_grid.place_new((2,1), 3)
        collision = self.test_grid.will_result_in_collision((2,1))
        self.assertTrue(collision)

    def test_different_place_will_not_result_in_collision(self):
        self.test_grid.place_new((2,1), 3)
        collision = self.test_grid.will_result_in_collision((2, 2))
        self.assertFalse(collision)

    def test_grid_move_or_collide_registers_collision(self):
        self.test_grid.place_new((2,1), 3)
        self.assertFalse(self.test_grid.was_collision())
        new_coord = self.test_grid.move_or_collide((2,2), (2,1), 3)
        self.assertTrue(self.test_grid.was_collision())
        self.assertEqual(new_coord, (2,2))

    def test_grid_move_or_collide_doesnt_register_non_collision(self):
        self.test_grid.place_new((2,1), 3)
        self.assertFalse(self.test_grid.was_collision())
        new_coord = self.test_grid.move_or_collide((1,2), (1,1), 3)
        self.assertFalse(self.test_grid.was_collision())
        self.assertEqual(new_coord, (1,1))

    def test_grid_can_tell_when_point_is_off_grid(self):
        is_on_board = self.test_grid.is_on_board((99,99))
        self.assertFalse(is_on_board)

    def test_grid_can_tell_when_point_is_on_grid(self):
        is_on_board = self.test_grid.is_on_board((0,0))
        self.assertTrue(is_on_board)

    def place_center(self, newid):
        self.test_grid.place_new((1,1), newid)

    def create_grid(self, width, height):
        colliders = [ThingCollider(), WallCollider()]
        return Grid([width, height], colliders)