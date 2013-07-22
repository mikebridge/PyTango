import sys, pygame
from grid import Grid
from collider import *

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
GRAY =  (127, 127, 127)
RED =   (255,   0,   0)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

player_colour=dict()
player_colour[1] = RED
player_colour[2] = BLUE
player_direction = dict()
player_direction[1] = RIGHT
player_direction[2] = LEFT

pygame.display.set_caption("PyTango")

grid_width, grid_height =       12, 12
blocksize =                     30
grid_offset_x, grid_offset_y =  25, 25 # the margin
gamewidth, gameheight =         blocksize * grid_width, blocksize * grid_height
screenwidth, screenheight =     gamewidth + grid_offset_x * 2, gameheight + grid_offset_y * 2

grid = Grid((grid_width,grid_height), [ThingCollider(), WallCollider()])

screen = pygame.display.set_mode([screenwidth, screenheight])

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

currentx = 0
currenty = 0
# draw the background
screen.fill(GRAY)
rect = [grid_offset_x, grid_offset_y, gamewidth, gameheight]

pygame.draw.rect(screen, WHITE, rect, 0)

grid.place_new((0,0), 1)
grid.place_new((11,11), 2)

def draw_block(id, coords):
    start_x = grid_offset_x + coords[0] * blocksize
    start_y = grid_offset_y + coords[1] * blocksize
    pygame.draw.rect(screen, player_colour[id], [start_x, start_y, blocksize, blocksize], 0)


def move_to_new_coord(id, new_coord):
    draw_block(id, new_coord)

# end background
# -------- Main Program Loop -----------

draw_block(1, (0,0))
draw_block(2, (11,11))

while not done:
    #print("LOOPING")
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                player_direction[1] = UP

            if event.key == pygame.K_a:
                player_direction[1] = LEFT

            if event.key == pygame.K_s:
                player_direction[1] = DOWN

            if event.key == pygame.K_d:
                player_direction[1] = RIGHT

            if event.key == pygame.K_UP:
                player_direction[2] = UP

            if event.key == pygame.K_DOWN:
                player_direction[2] = DOWN

            if event.key == pygame.K_LEFT:
                 player_direction[2] = LEFT

            if event.key == pygame.K_RIGHT:
                 player_direction[2] = RIGHT

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    next_coord = dict()

    for playerid in range(1,3):
        if player_direction[playerid] == UP:
            next_coord[playerid] = grid.move_up(playerid)
        elif player_direction[playerid] == DOWN:
            next_coord[playerid] = grid.move_down(playerid)
        elif player_direction[playerid] == RIGHT:
            next_coord[playerid] = grid.move_right(playerid)
        elif player_direction[playerid] == LEFT:
            next_coord[playerid] = grid.move_left(playerid)

    if grid.was_collision():
        print("COLLISION! AARGH! ")
        collisions = grid.who_collided()
        for user in collisions:
            print ("IT WAS USER: ")
            print (user)
    else:
        for playerid, coord in next_coord.items():
            move_to_new_coord(playerid, coord)

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT




    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit()