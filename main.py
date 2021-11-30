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
                 [4, 5, 6],
                 [7, 0, 8]]
EXPERIMENTAL_STATE = [[8, 15, 3, 0],
                      [5, 6, 4, 11],
                      [2, 9, 10, 12],
                      [1, 14, 7, 13]]
# ORDER = "RDUL"
# ORDER = "RDLU"
# ORDER = "DRUL"
# ORDER = "DRUL"
# ORDER = "DRLU"
# ORDER = "LUDR"
# ORDER = "LURD"
# ORDER = "ULDR"
ORDER = "ULRD"

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
        new_step = None

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
        else:
            print("step.move_step: wrong letter")
        return new_step


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
    opposite_directions = {"U": "D", "L": "R", "R": "L", "D": "U"}
    step = Step(None, None, [], INITIAL_STATE)
    open_list = [step]  # for steps that we stepped into
    closed_list = {}  # for steps with all neighbours checked
    print('START')
    print_board(step.board)
    while step.board != TARGET_STATE:
        posdirs = [char for char in get_possible_directions(step.board, ORDER)]
        iteration_counter = 0
        for direction in posdirs:
            sym = sym_move_step(direction, step.board, find_zero(step.board)[0],
                                find_zero(step.board)[1])
            if sym not in [b.board for b in closed_list] and sym not in [b.board for b in open_list]:
                # add new artificially created step to open list
                open_list.append(Step(step, direction, step.all_moves.copy(), sym))
                print(step.parent, step.previous_move, step.all_moves)
            # check how many new steps there are
            iteration_counter = iteration_counter + 1
        # if there are all done then move the step from open to closed and move to the first from open list
        if iteration_counter == len(posdirs):
            closed_list[step] = step
            open_list.pop(0)
            step = open_list[0]
    # if len(step.all_moves) - 1 == DEPTH:
    #     print('Depth reached, this is the end')
    #     return None
    return list_to_string(step.all_moves), len(list_to_string(step.all_moves))


def dfs():
    step = Step(None, None, [], INITIAL_STATE)
    open_list = [step]  # for steps that we stepped into
    closed_list = {}  # for steps with all neighbours checked
    print('START')
    print_board(step.board)
    while step.board != TARGET_STATE and len(open_list) != 0:
        print(len(open_list))
        iteration_counter = 0
        if len(step.all_moves) - 1 == DEPTH:
            open_list.remove(step)
            closed_list[step] = step
            step = step.parent
            continue
        posdirs = [char for char in get_possible_directions(step.board, ORDER)]
        for direction in posdirs:
            sym = sym_move_step(direction, step.board, find_zero(step.board)[0],
                                find_zero(step.board)[1])  # board sym for the specific direction
            if sym not in [b.board for b in open_list]:  # child is not on open list
                if sym not in [b.board for b in closed_list]:  # child is not on closed list
                    step = step.move_step(direction, step.board, find_zero(step.board)[0],
                                          find_zero(step.board)[1])  # not on lists so we move
                    # print_board(step.board)
                    open_list.append(step)  # adding current step to open_list
                    break  # getting out of for statement
            iteration_counter = iteration_counter + 1
        if iteration_counter == len(posdirs):
            open_list.remove(step)
            closed_list[step] = step
            step = step.parent
    if len(open_list) != 0:
        print('Depth reached, this is the end')
        return None
    return list_to_string(step.all_moves), len(list_to_string(step.all_moves))


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def a_star_hamming():
    step = Step(None, None, [], INITIAL_STATE)
    open_list = [step]  # for steps that we stepped into
    closed_list = {}  # for steps with all neighbours checked
    while how_many_in_pos(step.board):
        posdirs = [char for char in get_possible_directions(step.board, "LURD")]
        for direction in posdirs:
            sym = sym_move_step(direction, step.board, find_zero(step.board)[0],
                                find_zero(step.board)[1])


def print_board(board):
    for row in board:
        print(row)
    print()


def how_many_in_pos(board):
    count = 0
    k = 0
    l = 0
    for i in board:
        for j in i:
            if j == TARGET_STATE[k][l]:
                count = count + 1
            l = l + 1
        l = 0
        k = k + 1
    return count


def get_possible_directions(board, order):
    row, col = find_zero(board)
    size_x, size_y = len(board[0]), len(board)

    # CORNERS
    # top left corner
    if row == 0 and col == 0:
        result = [char for char in order if char not in "UL"]
        return result[0], result[1]

    # top right corner
    elif row == 0 and col == size_x - 1:
        result = [char for char in order if char not in "UR"]
        return result[0], result[1]

    # bottom right corner
    elif row == size_y - 1 and col == size_x - 1:
        result = [char for char in order if char not in "DR"]
        return result[0], result[1]

    # bottom left corner
    elif row == size_y - 1 and col == 0:
        result = [char for char in order if char not in "LD"]
        return result[0], result[1]

    # EDGES
    # top edge
    elif row == 0:
        result = [char for char in order if char not in "U"]
        return result[0], result[1], result[2]

    # right edge
    elif col == size_x - 1:
        result = [char for char in order if char not in "R"]
        return result[0], result[1], result[2]

    # bottom edge
    elif row == size_y - 1:
        result = [char for char in order if char not in "D"]
        return result[0], result[1], result[2]

    # left edge
    elif col == 0:
        result = [char for char in order if char not in "L"]
        return result[0], result[1], result[2]

    # MIDDLE
    else:
        return order[0], order[1], order[2], order[3]


if __name__ == '__main__':
    moves = [0]
    # step_t = Step(None, None, moves, TARGET_STATE)
    # step_e = Step(None, None, moves, EXPERIMENTAL_STATE)
    # print(dfs())
    # print(dfs())
    print("how_many_in_pos: ", how_many_in_pos(INITIAL_STATE))

    # print(getPossibleDirections(step_e.board, ORDER))
