from copy import deepcopy

from .board import Board


class Solver:
    def __init__(self, txt):
        board = Board(txt)
        self.question = board.question
        self.solving = board.solving
        self.board = board.board
        self.history = board.history

    def solve(self, x=0, y=0, history=True):
        if y > 8:
            return True
        elif self.solving[y][x] != 0:
            if x == 8:
                if self.solve(0, y + 1, history):
                    return True
            else:
                if self.solve(x + 1, y, history):
                    return True
        else:
            for i in self.board[y][x]:
                if self.check(x, y, i):
                    self.solving[y][x] = i
                    if history:
                        self.history.append(deepcopy(self.solving))
                    if x == 8:
                        if self.solve(0, y + 1, history):
                            return True
                    else:
                        if self.solve(x + 1, y, history):
                            return True
            self.solving[y][x] = 0
            return False

    def check(self, x, y, i):
        return self.row(y, i) and self.column(x, i) and self.block(x, y, i)

    def row(self, y, i):
        return all(i != self.solving[y][_x] for _x in range(9))

    def column(self, x, i):
        return all(i != self.solving[_y][x] for _y in range(9))

    def block(self, x, y, i):
        return all(i != self.solving[_y][_x]
                   for _y in range((y // 3) * 3, (y // 3) * 3 + 3)
                   for _x in range((x // 3) * 3, (x // 3) * 3 + 3))
