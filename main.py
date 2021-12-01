import collections
from copy import deepcopy
from enum import Enum

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
                 [4, 5, 0],
                 [7, 8, 6]]
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


class variants(Enum):
    HAMMING = 0,
    MANHATTAN = 1


class Step:
    def __init__(self, parent, previous_move, all_moves, board):
        self.parent = parent
        self.previous_move = previous_move
        self.all_moves = all_moves
        self.board = board
        if previous_move is not None:
            self.all_moves.append(previous_move)

    @property
    def f(self):
        return len(self.all_moves) + distance_manhattan(self.board)

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


def find_value(board, value):
    x, y = None, None
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == value:
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
    while len(open_list) != 0 and step.board != TARGET_STATE:
        print(len(open_list))
        print("closed: ", len(closed_list))
        iteration_counter = 0
        if len(step.all_moves) - 1 == DEPTH:
            open_list.remove(step)
            closed_list[step] = step
            if step.parent is None:
                return -1
            step = step.parent
            continue
        posdirs = [char for char in get_possible_directions(step.board, ORDER)]
        print("posdirs: ", len(posdirs))
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
            else:
                step = step.move_step(direction, step.board, find_zero(step.board)[0],
                                          find_zero(step.board)[1])
                break
        if iteration_counter == len(posdirs):
            open_list.remove(step)
            closed_list[step] = step
            if step.parent is None:
                return -1
            step = step.parent
    if len(open_list) != 0:
        print('Depth reached, this is the end')
        return -1
    else:
        return list_to_string(step.all_moves), len(list_to_string(step.all_moves))


def dfs2():
    step = Step(None, None, [], INITIAL_STATE)
    open_list = [step]
    closed_list = set()
    while open_list:
        step1 = open_list.pop()
        closed_list.add(tuple(step1.board))
        if step1.board == TARGET_STATE:
            return list_to_string(step.all_moves), len(list_to_string(step.all_moves))
        posdirs = [char for char in get_possible_directions(step1.board, ORDER)]
        for direction in posdirs:
            step2 = deepcopy(step1)
            step2 = step2.move_step(direction, step2.board, find_zero(step2.board)[0],
                                  find_zero(step2.board)[1])
            if tuple(step2.board) not in closed_list:
                open_list.append(step2)
                closed_list.add(tuple(step2.board))




def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1


def a_star(variant):
    if variant == variants.HAMMING:
        step = Step(None, None, [], INITIAL_STATE)
        open_list = [step]  # for steps that we stepped into
        closed_list = {}  # for steps with all neighbours checked
        while not all_positions_good(step.board):
            posdirs = [char for char in get_possible_directions(step.board, "LURD")]
            good_positions_count = []
            for direction in posdirs:
                sym = sym_move_step(direction,
                                    step.board,
                                    find_zero(step.board)[0],
                                    find_zero(step.board)[1])
                good_positions_count.append(how_many_in_pos(sym))
            # move step to the direction corresponding to the index of max value in good positions count array
            step = step.move_step(posdirs[good_positions_count.index(max(good_positions_count))],
                                  step.board,
                                  find_zero(step.board)[0],
                                  find_zero(step.board)[1])
        return list_to_string(step.all_moves), len(list_to_string(step.all_moves))

    elif variant == variants.MANHATTAN:
        step = Step(None, None, [], INITIAL_STATE)
        open_list = [step]  # for steps that we stepped into
        closed_list = set()  # for steps with all neighbours checked
        closed_list.add(step)
        while open_list:
            open_list = collections.deque(sorted(list(open_list), key=lambda elem: elem.f))
            step = open_list.popleft()
            if step.board == TARGET_STATE:
                return list_to_string(step.all_moves), len(list_to_string(step.all_moves))
            for direction in [char for char in get_possible_directions(step.board, "LURD")]:
                child = deepcopy(step)
                child = child.move_step(direction, step.board, find_zero(step.board)[0], find_zero(step.board)[1])
                if child.board not in [b.board for b in closed_list]:
                    open_list.append(child)
                    closed_list.add(child)


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


def all_positions_good(board):
    count = how_many_in_pos(board)

    result = 0
    for i in TARGET_STATE:
        for j in i:
            result = result + 1
    return count == result


def distance(board1, board2):
    x, y = find_zero(board1)
    x_tar, y_tar = find_zero(board2)
    return abs(x - x_tar) + abs(y - y_tar)


def distance_manhattan(board):
    distance_result = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                x, y = divmod(board[i][j] - 1, len(TARGET_STATE[0]))
                distance_result += abs(x - i) + abs(y - j)
    return distance_result


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
    visited = set()
    print(dfs2())

    # print(getPossibleDirections(step_e.board, ORDER))
