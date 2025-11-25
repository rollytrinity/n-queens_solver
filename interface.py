import pygame
import sys
from solver import solveNQueens


def run_viewer(n=8):
    pygame.init()
    CELL = 60
    MARGIN = 40
    SIZE = n * CELL
    screen = pygame.display.set_mode((SIZE, SIZE + MARGIN))
    pygame.display.set_caption(f"{n}-Queens Viewer")

    font = pygame.font.SysFont("arial", 24)

    solutions = solveNQueens(n)
    index = 0

    def draw_board(solution):
        screen.fill((0, 0, 0))

        for r in range(n):
            for c in range(n):
                color = (238, 238, 210) if (r + c) % 2 == 0 else (118, 150, 86)
                pygame.draw.rect(screen, color, (c * CELL, r * CELL, CELL, CELL))

        for (r, c) in solution:
            pygame.draw.circle(
                screen, (200, 50, 50),
                (c * CELL + CELL // 2, r * CELL + CELL // 2),
                CELL // 3
            )

        label = font.render(
            f"Solution {index + 1} / {len(solutions)}", True, (255, 255, 255)
        )
        screen.blit(label, (10, SIZE + 5))

        pygame.display.flip()


    draw_board(solutions[index])

  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(solutions)
                    draw_board(solutions[index])

                if event.key == pygame.K_LEFT:
                    index = (index - 1) % len(solutions)
                    draw_board(solutions[index])


if __name__ == "__main__":
    args = sys.argv
    n = args[1] if int(args[1]) > 0 else 8
    run_viewer(int(n))
