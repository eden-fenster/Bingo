#!/usr/bin/env python3
''' Bingo '''
import sys
import logging
from typing import List
ROWS: int = 5
COLS: int = 5

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# pylint: disable=C0103, C0116, W0511, w0612, C0200, W1203, W0613

# TODO: write tests with pytest and build list of numbers
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
            if not is_already_in_board(col=col, num=num):
                col.append(num)
                print(f'{num}\n')
        bingo_board.append(col)

def is_board_valid(bingo_board: List[List[int]]) -> bool:
    # go over board to scan if there are duplicates
    for i in range (0, ROWS):
        for j in range(0, COLS):
            # if yes, return false
            if is_already_in_board(col=bingo_board[i], num=bingo_board[i][j]):
                return False
    # else, return true
    return True

def is_already_in_board(col: List[int], num: int) -> bool:
    for i in range(0, len(col)):
        logging.debug(f'current square is {col[i]} and number is {num}\n')
        if col[i] == num:
            print("error: number can't be in the board more than once")
            sys.exit(1)
    return False

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
