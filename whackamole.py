import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
            #horizontal lines
            for x in range(1, 20):
                pygame.draw.line(screen, "black", (0,x*32), (640,x*32), 2)
            #vertical lines
            for y in range(1, 40):
                pygame.draw.line(screen, "black", (y*32, 0), (y*32, 512), 2)

            pygame.display.flip()
            clock.tick(1)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
