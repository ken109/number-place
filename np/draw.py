import pygame
from pygame.locals import *
from time import time
import sys

from .solver import Solver


class NPDraw:
    def __init__(self, txt, delay=0.5, size=300):
        self.solver = Solver(txt)
        self.solver.solve()
        pygame.init()
        screen = pygame.display.set_mode((size, size))
        pygame.display.set_caption('Number Place Solver')

        b_size = size / 9

        font = pygame.font.SysFont(None, int(b_size))

        history = 0
        refresh = time()
        while True:
            screen.fill((255, 255, 255))

            for i in range(1, 9):
                pygame.draw.line(screen, (0, 0, 0), (i * b_size, 0), (i * b_size, size), 1 if i % 3 != 0 else 2)
                pygame.draw.line(screen, (0, 0, 0), (0, i * b_size), (size, i * b_size), 1 if i % 3 != 0 else 2)

            for i in range(9):
                for j in range(9):
                    if self.solver.history[history][j][i] != 0:
                        text = font.render(str(self.solver.history[history][j][i]), True, (0, 0, 0))
                        screen.blit(text, ((i + 0.3) * b_size, (j + 0.2) * b_size))

            if len(self.solver.history) - 1 > history and time() - refresh > delay:
                history += 1
                refresh = time()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
