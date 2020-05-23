from copy import deepcopy


class Board:
    def __init__(self, txt):
        self.question = []
        self.solving = []
        self.before_solving = []
        self.board = []
        self.history = []
        self.read_question(txt)
        self.solving = deepcopy(self.question)
        self.make_board()

    def read_question(self, txt):
        with open(txt, 'r') as f:
            for i in f.readlines():
                self.question.append([int(j) for j in list(i.replace('\n', ''))])

    def make_board(self):
        self.board = []
        for i in range(9):
            self.board.append([])
            for j in range(9):
                if self.solving[i][j] == 0:
                    self.board[i].append(
                        {i for i in range(1, 10)} - self.row(i) - self.column(j) - self.block(j, i))
                else:
                    self.board[i].append({self.solving[i][j]})
        self.before_solving = self.solving
        self.solving = []
        for i in range(9):
            self.solving.append([])
            for j in range(9):
                if len(self.board[i][j]) == 1:
                    self.solving[i].append(list(self.board[i][j])[0])
                else:
                    self.solving[i].append(0)
        if self.before_solving != self.solving:
            self.history.append(self.before_solving)
            self.make_board()

    def row(self, y):
        return {self.solving[y][_x] for _x in range(9) if self.solving[y][_x] != 0}

    def column(self, x):
        return {self.solving[_y][x] for _y in range(9) if self.solving[_y][x] != 0}

    def block(self, x, y):
        return {self.solving[_y][_x]
                for _y in range((y // 3) * 3, (y // 3) * 3 + 3)
                for _x in range((x // 3) * 3, (x // 3) * 3 + 3)
                if self.solving[_y][_x] != 0}
