from copy import deepcopy

DEPTH = 20
TARGET_STATE = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]]
INITIAL_STATE = []
EXPERIMENTAL_STATE = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 0, 12],
                      [13, 14, 11, 15]]


class Step:
    def __init__(self, parent, previous_move, all_moves, board):
        self.parent = parent
        self.previous_move = previous_move
        self.all_moves = all_moves
        self.board = board
        self.all_moves.append(previous_move)

    def create_next_step(self, move, new_board):
        next_step = Step(self, move, self.all_moves, new_board)

    def move_step(self, move, board_state, x, y):
        new_arr = board_state
        if move == 'U':
            new_arr[x - 1][y] = row[x][y]
            new_arr[x][y] = row[x - 1][y]
            self.create_next_step(move, new_arr)
            x = x - 1
        elif move == 'D':
            new_arr[x + 1][y] = row[x][y]
            new_arr[x][y] = row[x + 1][y]
            self.create_next_step(move, new_arr)
            x = x + 1
        elif move == 'R':
            new_arr[x][y + 1] = row[x][y]
            new_arr[x][y] = row[x][y + 1]
            self.create_next_step(move, new_arr)
            y = y + 1
        elif move == 'L':
            new_arr[x][y - 1] = row[x][y]
            new_arr[x][y] = row[x][y - 1]
            self.create_next_step(move, new_arr)
            y = y - 1
        return x, y


def find_zero(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                x = row
                y = column
    return x, y


def bfs():
    print("bfs")


def dfs():
    print("dfs")
    step = Step(None, None, [], INITIAL_STATE)
    open_list = []
    closed_list = {}
    zero_pos_x, zero_pos_y = find_zero(INITIAL_STATE)
    while step.board != TARGET_STATE:
        print("hi")


def a_star():
    print('A*')


def print_board(board):
    for row in board:
        print(row)
    print()


def createNeighborStates(step):
    x, y = find_zero(step.board)
    size_x, size_y = len(step.board[0]), len(step.board)

    step_U = deepcopy(step.board)
    step_R = deepcopy(step.board)
    step_D = deepcopy(step.board)
    step_L = deepcopy(step.board)

    # CORNERS
    # top left corner
    if x == 0 and y == 0:
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        step_D[x][y], step_D[x][y + 1] = step_D[x][y + 1], step_D[x][y]
        return "RD", step_R, step_D

    # top right corner
    elif x == size_x - 1 and y == 0:
        step_D[x][y], step_D[x][y + 1] = step_D[x][y + 1], step_D[x][y]
        step_L[x][y], step_L[x - 1][y] = step_L[x - 1][y], step_L[x][y]
        return "DL", step_D, step_L

    # bottom right corner
    elif x == size_x - 1 and y == size_y - 1:
        step_L[x][y], step_L[x][y - 1] = step_L[x][y - 1], step_L[x][y]
        step_U[x][y], step_U[x - 1][y] = step_U[x - 1][y], step_U[x][y]
        return "LU", step_L, step_U

    # bottom left corner
    elif x == 0 and y == size_y - 1:
        step_U[x][y], step_U[x][y - 1] = step_U[x][y - 1], step_U[x][y]
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        return "UR", step_U, step_R

    # EDGES
    # top edge
    elif y == 0:
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        step_D[x][y], step_D[x][y + 1] = step_D[x][y + 1], step_D[x][y]
        step_L[x][y], step_L[x - 1][y] = step_L[x - 1][y], step_L[x][y]
        return "RDL", step_R, step_D, step_L

    # right edge
    elif x == size_x - 1:
        step_D[x][y], step_D[x][y + 1] = step_D[x][y + 1], step_D[x][y]
        step_L[x][y], step_L[x - 1][y] = step_L[x - 1][y], step_L[x][y]
        step_U[x][y], step_U[x][y - 1] = step_U[x][y - 1], step_U[x][y]
        return "DLU", step_D, step_L, step_U

    # bottom edge
    elif y == size_y - 1:
        step_L[x][y], step_L[x - 1][y] = step_L[x - 1][y], step_L[x][y]
        step_U[x][y], step_U[x][y - 1] = step_U[x][y - 1], step_U[x][y]
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        return "LUR", step_L, step_U, step_R

    # left edge
    elif x == 0:
        step_U[x][y], step_U[x][y - 1] = step_U[x][y - 1], step_U[x][y]
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        step_D[x][y], step_D[x][y + 1] = step_D[x][y + 1], step_D[x][y]
        return "URD", step_U, step_R, step_D

    # MIDDLE
    else:
        step_U[x][y], step_U[x][y + 1] = step_U[x][y + 1], step_U[x][y]
        step_R[x][y], step_R[x + 1][y] = step_R[x + 1][y], step_R[x][y]
        step_D[x][y], step_D[x][y - 1] = step_D[x][y - 1], step_D[x][y]
        step_L[x][y], step_L[x - 1][y] = step_L[x - 1][y], step_L[x][y]
        return "URDL", step_U, step_R, step_D, step_L


if __name__ == '__main__':
    moves = [0]
    step_t = Step(None, None, moves, TARGET_STATE)
    step_e = Step(None, None, moves, EXPERIMENTAL_STATE)

    print(createNeighborStates(step_t)[0])
    print_board(createNeighborStates(step_t)[1])
    print_board(createNeighborStates(step_t)[2])
    print()
    print(createNeighborStates(step_e)[0])
    print_board(createNeighborStates(step_e)[1])
    print_board(createNeighborStates(step_e)[2])
    print_board(createNeighborStates(step_e)[3])
    print_board(createNeighborStates(step_e)[4])

