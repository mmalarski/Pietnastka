from copy import deepcopy

DEPTH = 20
# TARGET_STATE = [[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12],
#                 [13, 14, 15, 0]]
TARGET_STATE = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]]
# INITIAL_STATE = [[1, 2, 3, 0],
#                  [5, 6, 7, 4],
#                  [9, 10, 11, 8],
#                  [13, 14, 15, 12]]
INITIAL_STATE = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]
ORDER = "DLUR"
EXPERIMENTAL_STATE = [[8, 15, 3, 0],
                      [5, 6, 4, 11],
                      [2, 9, 10, 12],
                      [1, 14, 7, 13]]

POS = [0, 0]


class Step:
    def __init__(self, parent, previous_move, all_moves, board):
        self.parent = parent
        self.previous_move = previous_move
        self.all_moves = all_moves
        self.board = board
        if previous_move is not None:
            self.all_moves.append(previous_move)

    def create_next_step(self, move, new_board):
        next_step = Step(self, move, self.all_moves, new_board)
        return next_step

    def move_step(self, move, board_state, x, y):
        new_arr = deepcopy(board_state)

        if move == 'U':
            new_arr[x - 1][y] = board_state[x][y]
            new_arr[x][y] = board_state[x - 1][y]
            new_step = self.create_next_step(move, new_arr)
            POS[0] = x - 1
        elif move == 'D':
            new_arr[x + 1][y] = board_state[x][y]
            new_arr[x][y] = board_state[x + 1][y]
            new_step = self.create_next_step(move, new_arr)
            POS[0] = x + 1
        elif move == 'R':
            new_arr[x][y + 1] = board_state[x][y]
            new_arr[x][y] = board_state[x][y + 1]
            new_step = self.create_next_step(move, new_arr)
            POS[1] = y + 1
        elif move == 'L':
            new_arr[x][y - 1] = board_state[x][y]
            new_arr[x][y] = board_state[x][y - 1]
            new_step = self.create_next_step(move, new_arr)
            POS[1] = y - 1
        return new_step

    def is_child(self, other_step, dir):
        copystep = deepcopy(other_step)
        x, y = find_zero(copystep)
        copystep.move_step(dir, copystep.board, temp_x, temp_y)
        if self.board == other_step.board:
            return true
        return false


def find_zero(board):
    x, y = None, None
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                x = row
                y = column
    return x, y


def sym_move_step(move, board_state, x, y):
    new_arr = deepcopy(board_state)
    if move == 'U':
        new_arr[x - 1][y] = board_state[x][y]
        new_arr[x][y] = board_state[x - 1][y]
    elif move == 'D':
        new_arr[x + 1][y] = board_state[x][y]
        new_arr[x][y] = board_state[x + 1][y]
    elif move == 'R':
        new_arr[x][y + 1] = board_state[x][y]
        new_arr[x][y] = board_state[x][y + 1]
    elif move == 'L':
        new_arr[x][y - 1] = board_state[x][y]
        new_arr[x][y] = board_state[x][y - 1]
    return new_arr


def bfs():
    print("bfs")


def dfs():
    print("dfs")
    step = Step(None, None, [], INITIAL_STATE)
    open_list = [step]  # for steps that we stepped into
    closed_list = {}  # for steps with all neighbours checked
    POS[0], POS[1] = find_zero(INITIAL_STATE)  # zeros position on the board
    move_to_CL = False
    iteration_counter = 0
    debug_counter = 0
    print('START')
    print_board(step.board)
    while step.board != TARGET_STATE:
        # print(debug_counter)
        # print_board(open_list)
        # print_board(closed_list)
        posdirs = [char for char in getPossibleDirections(step.board, ORDER)]
        iteration_counter = 0
        print(POS[0], POS[1], posdirs)
        for direction in posdirs:
            print(direction)
            sym = sym_move_step(direction, step.board, POS[0], POS[1])  # board sym for the specific direction
            if sym not in [b.board for b in open_list]:  # child is not on open list
                if sym not in [b.board for b in closed_list]:  # child is not on closed list
                    print('out', direction)
                    # step = step.move_step(posdirs[0], step.board, POS[0], POS[1])  # not on lists so we move
                    step = step.move_step(direction, step.board, POS[0], POS[1])
                    print_board(step.board)
                    open_list.append(step)  # adding current step to open_list
                    break  # getting out of for statement
                # else:  # child is on closed list
                    # posdirs.pop(0)  # we remove child's direction from direction list
                    # for i in posdirs:
                    #     if sym in closed_list:
                    #         posdirs.pop(i)
                    #         if len(posdirs) == 0:
                    #             open_list.remove(step)
                    #             closed_list[step] = step
                    #             step = step.parent
                    #             print('''
                    #
                    #             HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                    #             EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                    #             LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
                    #             LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
                    #             OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                    #
                    #             ''')
                    #     else:
                    #         break
                    # # step = step.move_step(posdirs[0], step.board, POS[0], POS[1])
                    # step = step.move_step(direction, step.board, POS[0], POS[1])
                    # open_list.append(step)
                    # break
            iteration_counter = iteration_counter + 1
            # print(iteration_counter)
        if iteration_counter == len(posdirs):
            # move_to_CL = True
            iteration_counter = 0
            open_list.remove(step)
            closed_list[step] = step
            step = step.parent


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
    # step_t = Step(None, None, moves, TARGET_STATE)
    # step_e = Step(None, None, moves, EXPERIMENTAL_STATE)
    dfs()

    # print(getPossibleDirections(step_e.board, ORDER))
