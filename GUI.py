from AStar import Location, Node, GridProblem, best_first_search
import pygame

WINDOW_SIZE = [600, 600]
NUM_CELLS = 50




screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
                pygame.display.quit()
                quit()
                


if __name__ == "__main__":
    main()