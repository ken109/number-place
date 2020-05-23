import pygame
from pygame.locals import *
import sys
from concurrent import futures
from time import time

from .solver import Solver


class Drawer(Solver):
    def __init__(self, txt, delay=0, size=300):
        super().__init__(txt)
        pygame.init()
        screen = pygame.display.set_mode((size, size))
        pygame.display.set_caption('Number Place Solver')

        b_size = size / 9

        font = pygame.font.SysFont(None, int(b_size))

        executor = futures.ThreadPoolExecutor(max_workers=1)
        executor.submit(self.solve, history=False if delay <= 0 else True)

        history = 0
        refresh = time()
        while True:
            screen.fill((255, 255, 255))

            for i in range(1, 9):
                pygame.draw.line(screen, (0, 0, 0), (i * b_size, 0), (i * b_size, size), 1 if i % 3 != 0 else 2)
                pygame.draw.line(screen, (0, 0, 0), (0, i * b_size), (size, i * b_size), 1 if i % 3 != 0 else 2)

            for i in range(9):
                for j in range(9):
                    if self.solving[j][i] if delay <= 0 else self.history[history][j][i] != 0:
                        text = font.render(str(self.solving[j][i] if delay <= 0 else self.history[history][j][i]), True,
                                           (0, 0, 0) if self.question[j][i] == 0 else (255, 0, 0))
                        screen.blit(text, ((i + 0.3) * b_size, (j + 0.2) * b_size))

            if 0 < delay < time() - refresh and len(self.history) - 1 > history:
                self.history.pop(history)
                history += 1
                refresh = time()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
