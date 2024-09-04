#!/usr/bin/env python3
''' Bingo '''
from typing import List
ROWS: int = 5
COLS: int = 5

# pylint: disable=C0103, C0116, W0511, w0612

# TODO: check vadility of input and write tests with pytest
def main() -> None:
    # NUMBERS: int = 100
    bingo_board: List[List[int]] = []
    fill_board(bingo_board=bingo_board)
    for i in range(0, ROWS):
        for j in range(0, COLS):
            print(f'{bingo_board[i][j]}' + ', ')
    print('we now have a bingo board !\n')

def fill_board(bingo_board: List[List[int]]):
    num: int
    print('fill 25 different numbers to put in the board\n')
    for i in range (0, ROWS):
        col: List[int] = []
        for j in range (0, COLS):
            num = int(input('put a different number\n'))
            col.append(num)
            print(f'{num} + \n')
        bingo_board.append(col)

# def fill_list(number_list: List[int]):
#     for i in range (0, 100):
#         number_list[i] = i + 1
#         is_marked[i] = False

# def random_number() -> int:
#     # return a random number between 1 - 100
#     return 1

# def mark_number():
#     #mark number
#     return 1

if __name__ == '__main__':
    main()
