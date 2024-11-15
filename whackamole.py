import pygame
import random

def main():
    try:
        pygame.init()

        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        mole_image = pygame.image.load("mole.png")

        grid_width= 32
        grid_height = 32
        rows = 16
        cols = 20

        mole_x = 0
        mole_y = 0
        mole_position = (mole_x, mole_y)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_position[0] <= event.pos[0] <= mole_position[0] + grid_width and \
                       mole_position[1] <= event.pos[1] <= mole_position[1] + grid_height:
                        mole_x = random.randint(0, cols - 1) * grid_width
                        mole_y = random.randint(0, rows - 1) * grid_height
                        mole_position = (mole_x, mole_y)

            screen.fill("light green")

            for i in range(1, cols):
                pygame.draw.line(screen, "black", (grid_width * i, 0), (grid_width * i, 512))
            for i in range(1, rows):
                pygame.draw.line(screen, "black", (0, grid_height * i), (640, grid_height * i))

            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()
            clock.tick(60)
    except:
        pygame.quit()
if __name__ == "__main__":
    main()
