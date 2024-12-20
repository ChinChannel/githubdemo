import pygame
import random


def draw_grid(screen,color):
    for x in range(GRID_WIDTH+1):
        pygame.draw.line(screen,color,(x*SQUARE_SIZE,0),(x*SQUARE_SIZE,GRID_HEIGHT*SQUARE_SIZE),1)
    for y in range(GRID_HEIGHT+1):
        pygame.draw.line(screen,color,(0,y*SQUARE_SIZE),(GRID_WIDTH*SQUARE_SIZE,y*SQUARE_SIZE),1)

def main():
    try:
        pygame.init()
        pygame.display.set_caption("WHACK-A-MOLE")

        mole = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((GRID_WIDTH*SQUARE_SIZE,GRID_HEIGHT*SQUARE_SIZE))
        clock = pygame.time.Clock()

        mole_start_x = 0
        mole_start_y = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x1 = x//SQUARE_SIZE
                    y1 = y//SQUARE_SIZE

                    if x1 == mole_start_x and y1 == mole_start_y:
                        mole_start_x = random.randrange(GRID_WIDTH)
                        mole_start_y = random.randrange(GRID_HEIGHT)
            screen.fill("yellow")
            draw_grid(screen,(0,0,0))

            screen.blit(mole,(mole_start_x*SQUARE_SIZE,mole_start_y*SQUARE_SIZE))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

#BOARD INFO
GRID_HEIGHT = 16
GRID_WIDTH = 20
SQUARE_SIZE = 32

if __name__ == "__main__":
    main()
