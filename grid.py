import numpy

# see: http://eli.thegreenplace.net/2009/01/09/writing-a-game-in-python-with-pygame-part-iii/

class Grid:

    def __init__(self, size, colliders):
        self.__colliders__ = colliders
        self.__grid__ = numpy.zeros(size, dtype = numpy.int32 )
        self.__collisions_detected_by_id__ = set()
        self.__currentpos_id_to_coord__ = dict()

    def get_grid(self):
        return self.__grid__

    def place_new(self, coord, id):
        self.__currentpos_id_to_coord__[id] = coord;
        self.__grid__[coord[0],coord[1]] = id
        return coord

    def id_at(self, coord):
        return self.__grid__[coord]

    def move_left(self, id):
        old_coord = self.current_pos(id)
        return self.move_or_collide(old_coord, (old_coord[0] - 1, old_coord[1]), id)

    def move_right(self, id):
        old_coord = self.current_pos(id)
        return self.move_or_collide(old_coord, (old_coord[0] + 1, old_coord[1]), id)

    def move_up(self, id):
        old_coord = self.current_pos(id)
        return self.move_or_collide(old_coord, (old_coord[0], old_coord[1] - 1), id)

    def move_down(self, id):
        old_coord = self.current_pos(id)
        return self.move_or_collide(old_coord, (old_coord[0], old_coord[1] + 1), id)

    def current_pos(self, id):
        return self.__currentpos_id_to_coord__[id]

    def to_dict(self):
        return {k:v for k,v in numpy.ndenumerate(self.__grid__)}

    # collision detection
    def was_collision(self):
        return len(self.__collisions_detected_by_id__) > 0

    def who_collided(self):
        return self.__collisions_detected_by_id__

    # move to a new space, or else register a collision.
    # return old_coord if collision, return new_coord if not.
    def move_or_collide(self, old_coord, new_coord, id):
        if self.will_result_in_collision(new_coord):
            self.register_collision(id)
            return old_coord
        else:
            return self.place_new(new_coord, id)

    def will_result_in_collision(self, new_coord):
        # todo: rewrite as .any
        for c in self.__colliders__:
            if c.will_result_in_collision(self, new_coord):
                return True
        return False

    def register_collision(self, id):
        self.__collisions_detected_by_id__.update({id})

    @property
    def width(self):
        return self.__grid__.shape[0]

    @property
    def height(self):
        return self.__grid__.shape[1]