from copy import deepcopy

DEPTH = 20
TARGET_STATE = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]]
INITIAL_STATE = []
ORDER = "LURD"
EXPERIMENTAL_STATE = [[8, 15, 3, 0],
                      [5, 6, 4, 11],
                      [2, 9, 10, 12],
                      [1, 14, 7, 13]]


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

    def is_child(self, other_step, dir):
        copystep = deepcopy(other_step)
        x, y = find_zero(copystep)
        copystep.move_step(dir, copystep.board, temp_x, temp_y)
        if self.board == other_step.board:
            return true
        return false


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
    open_list = [step]
    closed_list = {}
    zero_pos_x, zero_pos_y = find_zero(INITIAL_STATE)
    while step.board != TARGET_STATE:

        posdirs = getPossibleDirections(step.board)
        if posdirs[0] not in open_list:  # child is not on open list
            if posdirs[0] not in closed_list:  # child is not on closed list
                step.move_step(posdirs[0], state.board, zero_pos_x, zero_pos_y)
                open_list.append(step)
            else:  # child is on closed list
                posdirs.pop(0)
                for i in posdirs:
                    if posdirs[0] in closed_list:
                        posdirs.pop()
                        if len(posdirs) == 0:
                            open_list.remove(step)
                            closed_list.append(step)
                            step = step.parent
                    else:
                        break
                step.move_step(posdirs[0], state.board, zero_pos_x, zero_pos_y)
                open_list.append(step)
        else:  # parent is on the open list
            copystep = deepcopy(step)
            temp_x = deepcopy(zero_pos_x)
            temp_y = deepcopy(zero_pos_y)
            copystep.move_step(posdirs[0], copystep.board, temp_x, temp_y)
            if copystep != step.parent:
                open_list.remove(step)
                closed_list.append(step)
                step = step.parent
            else:
                posdirs.pop(0)
                for i in posdirs:
                    if posdirs[0] in closed_list:
                        posdirs.pop()
                        if len(posdirs) == 0:
                            return -1
                    else:
                        step.move_step(posdirs[0], state.board, zero_pos_x, zero_pos_y)
                        open_list.append(step)


def a_star():
    print('A*')


def print_board(board):
    for row in board:
        print(row)
    print()


def getPossibleDirections(board, order):
    row, col = find_zero(board)
    size_x, size_y = len(board[0]), len(board)

    # CORNERS
    # top left corner
    if row == 0 and col == 0:
        result = [char for char in order if char not in "UL"]
        # result = order.replace("U", '')
        # result = result.replace("L", '')
        return result[0], result[1]

    # top right corner
    elif row == 0 and col == size_x - 1:
        result = [char for char in order if char not in "UR"]
        # result = order.replace("U", '')
        # result = result.replace("R", '')
        return result[0], result[1]

    # bottom right corner
    elif row == size_y - 1 and col == size_x - 1:
        result = [char for char in order if char not in "DR"]
        # result = order.replace("D", '')
        # result = result.replace("R", '')
        return result[0], result[1]

    # bottom left corner
    elif row == size_y - 1 and col == 0:
        result = [char for char in order if char not in "LD"]
        # result = order.replace("L", '')
        # result = result.replace("D", '')
        return result[0], result[1]

    # EDGES
    # top edge
    elif row == 0:
        result = [char for char in order if char not in "U"]
        # result = order.replace("U", '')
        return result[0], result[1], result[2]

    # right edge
    elif col == size_x - 1:
        result = [char for char in order if char not in "R"]
        # result = order.replace("R", '')
        return result[0], result[1], result[2]

    # bottom edge
    elif row == size_y - 1:
        result = [char for char in order if char not in "D"]
        # result = order.replace("D", '')
        return result[0], result[1], result[2]

    # left edge
    elif col == 0:
        result = [char for char in order if char not in "L"]
        # result = order.replace("L", '')
        return result[0], result[1], result[2]

    # MIDDLE
    else:
        return order[0], order[1], order[2], order[3]


if __name__ == '__main__':
    moves = [0]
    step_t = Step(None, None, moves, TARGET_STATE)
    step_e = Step(None, None, moves, EXPERIMENTAL_STATE)

    print(getPossibleDirections(step_e.board, ORDER))
