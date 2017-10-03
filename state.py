class State:

    board = None
    last_move = None
    parent = None
    goal = None
    distance = 0

    def __init__(self, board, goal=None, last_move=None, parent=None):
        self.board = board
        if goal:
            self.distance = self.get_distance(goal)
        self.last_move = last_move
        self.parent = parent
        self.goal = goal

    def get_next_states(self):
        result = [[[None for x in range(len(self.board[0]))] for y in range(len(self.board))] for i in range(4)]
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == 0:
                    if y > 0:
                        result[0][y][x] = self.board[y - 1][x]
                        result[0][y - 1][x] = 0
                    else:
                        result[0][y][x] = 0

                    if y < len(self.board) - 1:
                        result[1][y][x] = self.board[y + 1][x]
                        result[1][y + 1][x] = 0
                    else:
                        result[1][y][x] = 0

                    if x > 0:
                        result[2][y][x] = self.board[y][x - 1]
                        result[2][y][x - 1] = 0
                    else:
                        result[2][y][x] = 0

                    if x < len(self.board[y]) - 1:
                        result[3][y][x] = self.board[y][x + 1]
                        result[3][y][x + 1] = 0
                    else:
                        result[3][y][x] = 0

                else:
                    if result[0][y][x] == None: result[0][y][x] = self.board[y][x]
                    if result[1][y][x] == None: result[1][y][x] = self.board[y][x]
                    if result[2][y][x] == None: result[2][y][x] = self.board[y][x]
                    if result[3][y][x] == None: result[3][y][x] = self.board[y][x]

        # Remove results that are equal to current board
        result2 = []
        for i in range(len(result)):
            if result[i] != self.board:
                state = State(result[i], self.goal)
                if i == 0:
                    state.last_move = 'd'
                elif i == 1:
                    state.last_move = 'u'
                elif i == 2:
                    state.last_move = 'r'
                elif i == 3:
                    state.last_move = 'l'
                state.parent = self
                result2.append(state)

        return result2

    def get_distance(self, goal):
        distance = 0

        for y1 in range(len(self.board)):
            for x1 in range(len(self.board[0])):
                for y2 in range(len(self.board)):
                    for x2 in range(len(self.board[0])):
                        if self.board[y1][x1] == goal.board[y2][x2]:
                            distance += abs(x1 - x2) + abs(y1 - y2)

        return distance

    def print_board(self):
        print()
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                print(self.board[y][x], end='\t')
            print()
        print()

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.board == other.board
