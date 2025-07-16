import random
import copy

def generate_board():
    base = 3
    side = base * base

    # pattern for a baseline valid solution
    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    # randomize rows, columns and numbers
    def shuffle(s): return random.sample(s, len(s))

    r_base = range(base)
    rows  = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols  = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums  = shuffle(range(1, side + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4  # 75% removed

    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def check_solution(board):
    # board is a 9x9 list of lists of ints
    for i in range(9):
        row = board[i]
        col = [board[r][i] for r in range(9)]
        box = [board[r][c] for r in range(i // 3 * 3, i // 3 * 3 + 3)
                            for c in range(i % 3 * 3, i % 3 * 3 + 3)]
        if len(set(row)) != 9 or len(set(col)) != 9 or len(set(box)) != 9:
            return False
    return True
