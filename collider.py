class ThingCollider:

    def will_result_in_collision(self, grid, new_coord):
        if not grid.is_on_board(new_coord):
            return False
        else:
            return grid.id_at(new_coord) != 0

class WallCollider:

    def will_result_in_collision(self, grid, new_coord):
        return not grid.is_on_board(new_coord)

