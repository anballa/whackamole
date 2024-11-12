import pygame
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 512
GRID_SIZE = 32

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_image = pygame.image.load("mole.png")
        mole_x = 0 
        mole_y = 0
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))
                if mole_rect.collidepoint(mouse_x, mouse_y):
                    mole_x = random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
                    mole_y = random.randrange(0, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE
            
                                              
            screen.fill("light green")
            
            #horizontal lines
            for x in range(1, 20):
                pygame.draw.line(screen, "black", (0,x*32), (640,x*32), 2)
            
            #vertical lines
            for y in range(1, 40):
                pygame.draw.line(screen, "black", (y*32, 0), (y*32, 512), 2)
            
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
