import collections
from copy import deepcopy
import time as t
import os
import sys

DEPTH = 20
TARGET_STATE = []

ORDER = "RDUL"
# ORDER = "RDLU"
# ORDER = "DRUL"
# ORDER = "DRLU"
# ORDER = "LUDR"
# ORDER = "LURD"
# ORDER = "ULDR"
# ORDER = "ULRD"

POS = [0, 0]


class Step:
    def __init__(self, parent, previous_move, all_moves, board):
        self.parent = parent
        self.previous_move = previous_move
        self.all_moves = all_moves
        self.board = board
        self.board_string = sq_list_to_string(board)
        if previous_move is not None:
            self.all_moves.append(previous_move)

    @property
    def f_m(self):
        return len(self.all_moves) + distance_manhattan(self.board)

    @property
    def f_h(self):
        return how_many_in_pos(self.board)

    def create_next_step(self, move, new_board):
        next_step = Step(self, move, deepcopy(self.all_moves), new_board)
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


def blind_algorithms(order, variant, init_state, t_state):
    step = Step(None, None, [], init_state)
    open_list = [step]
    closed_list = {}
    max_depth = 0
    start_time = t.time()
    while open_list:
        if variant == "dfs":
            step = open_list.pop()
        elif variant == "bfs":
            step = open_list.pop(0)
        else:
            return "Wrong variant"

        if closed_list.get(step.board_string) is None:
            if len(step.all_moves) > max_depth:
                max_depth = len(step.all_moves)
            if step.board == t_state:
                # stan odwiedzone - kiedykolwiek byly na openliscie
                return str(len(list_to_string(step.all_moves))), list_to_string(step.all_moves), len(open_list), len(
                    closed_list), max_depth, t.time() - start_time
            closed_list[step.board_string] = step.all_moves
            if variant == "dfs" and len(step.all_moves) == DEPTH:
                continue
            for direction in reversed(get_possible_directions(step.board, order)): # reversed order depending on method
                child = deepcopy(step)
                child = child.move_step(direction, step.board, find_zero(step.board)[0], find_zero(step.board)[1])
                #is target state return
                if closed_list.get(child.board_string) is None:
                    open_list.append(child)
                elif len(closed_list.get(child.board_string)) > len(child.all_moves):
                    # optimalisation for each method all moves
                    open_list.append(child)
                    closed_list.pop(child.board_string)
    return str(-1), list_to_string(step.all_moves), len(open_list), len(closed_list), max_depth, t.time() - start_time


def a_star(variant, init_state, t_state):
    global TARGET_STATE
    TARGET_STATE = t_state
    step = Step(None, None, [], init_state)
    # check if init state isnt target
    open_list = [step]
    closed_list = set()
    closed_list.add(step)
    max_depth = 0
    start_time = t.time()
    while open_list:
        if variant == "manh":
            open_list = collections.deque(sorted(list(open_list), key=lambda elem: elem.f_m))
        elif variant == "hamm":
            open_list = collections.deque(sorted(list(open_list), key=lambda elem: elem.f_h, reverse=True))
        else:
            print("Wrong variant in astar.")
        step = open_list.popleft()
        if len(step.all_moves) > max_depth:
            max_depth = len(step.all_moves)
        if step.board == t_state:
            return str(len(list_to_string(step.all_moves))), list_to_string(step.all_moves), len(open_list), len(
                closed_list), max_depth, t.time() - start_time
        for direction in get_possible_directions(step.board, "LURD"):
            # check if is target
            child = deepcopy(step)
            child = child.move_step(direction, step.board, find_zero(step.board)[0], find_zero(step.board)[1])
            if child.board not in [b.board for b in closed_list]:
                open_list.append(child)
                closed_list.add(child)


def find_zero(board):
    x, y = None, None
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                x = row
                y = column
    return x, y


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1


def sq_list_to_string(s):
    str1 = ""
    for ele in s:
        for inner_element in ele:
            str1 += str(inner_element) + ','
    return str1


def how_many_in_pos(board):
    # ignore 0
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


def convert_to_boards(text):
    w = int(text[0][0])
    k = int(text[0][2])

    initial_board = []
    target_board = []
    for i in range(w):
        target_board.append([])
        initial_board.append(text[i + 1].strip("\n").split(" "))
    for i in range(w):
        for j in range(k):
            target_board[i].append(i * k + j + 1)
            initial_board[i][j] = int(initial_board[i][j])
    target_board[w - 1][k - 1] = 0

    return initial_board, target_board


if __name__ == '__main__':
    # [0]name.py [1]algorithm [2]ORDER/variant [3]initial state [4]output file solution [5]output file with statistics
    if len(sys.argv) == 6:
        file = open(f"{sys.argv[3]}")
        initial_state, target_state = convert_to_boards(file.readlines())
        file.close()
        solution_file = open(sys.argv[4], "w")
        statistics_file = open(sys.argv[5], "w")

        if sys.argv[1] == "bfs" or sys.argv[1] == "dfs":
            if sys.argv[2] not in ["RDUL", "RDLU", "DRUL", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]:
                print("Podaj odpowiedni porzadek przeszukiwania (ORDER)")
            else:
                length, solution, ol_size, cl_size, depth, time = blind_algorithms(sys.argv[2], sys.argv[1],
                                                                                   initial_state, target_state)
                solution_file.writelines([length, '\n', solution]) if length != "-1" else solution_file.writelines(
                    [length])
                statistics_file.write(length)
                if length != -1:
                    statistics_file.writelines(['\n', str(ol_size),
                                                '\n', str(cl_size),
                                                '\n', str(depth),
                                                '\n', str(round(time * 1000, 3))])
        elif sys.argv[1] == "astr":
            if sys.argv[2] not in ["manh", "hamm"]:
                print("Podaj odpowiedni wariant metody A*")
            else:
                length, solution, ol_size, cl_size, depth, time = a_star(sys.argv[2], initial_state, target_state)
                solution_file.writelines([length, '\n', solution])
                statistics_file.writelines([length,
                                            '\n', str(ol_size),
                                            '\n', str(cl_size),
                                            '\n', str(depth),
                                            '\n', str(round(time * 1000, 3))])
        else:
            print(f"Podano bledna nazwe algorytmu: {sys.argv[1]}")

        solution_file.close()
        statistics_file.close()
    else:
        print("Podaj poprawna ilosc argumentow (5)")
    #
    # INITIAL_STATE = [
    #     [0, 2, 3, 4],
    #     [1, 5, 6, 8],
    #     [9, 10, 7, 12],
    #     [13, 14, 11, 15]
    # ]
    # TARGET_STATE = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, 15, 0]
    # ]
    #
    # print(a_star("manh", INITIAL_STATE, TARGET_STATE))
