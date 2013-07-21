class ThingCollider:

    def will_result_in_collision(self, grid, new_coord):
        return grid.id_at(new_coord) != 0

class WallCollider:

    def will_result_in_collision(self, grid, new_coord):
        x = new_coord[0]
        y = new_coord[1]
        return x < 0 or y < 0 or x >= grid.width or y >= grid.height

