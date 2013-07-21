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

pygame.display.set_caption("PyTango")

gamewidth, gameheight =         400, 400
screenwidth, screenheight =     gamewidth + 50, gameheight + 50
blocksize =                     10
playing_grid =                  [gamewidth/10, gameheight/10]
grid_offset_x =                 25
grid_offset_y =                 25

grid = Grid((30,30), [ThingCollider(), WallCollider()])

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


# end background
# -------- Main Program Loop -----------
while not done:
    #print("LOOPING")
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("User pressed the 'w' key.")


    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT




    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit()