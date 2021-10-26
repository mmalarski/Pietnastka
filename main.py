DEPTH = 20
TARGET_STATE = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
INITIAL_STATE = []

class Step:

    def __init__(self, parent, previous_move, all_moves, board):
        self.parent = parent
        self.previous_move = previous_move
        self.all_moves = all_moves
        self.board = board

    # def move_step(self, move, board_state):


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



if __name__ == '__main__':
    print_hi('PyCharm')



