#!/usr/bin/env python3
''' Bingo '''
import logging
import sys
import random
from typing import List
ROWS: int = 5
COLS: int = 5
OUT_NUMBERS: List[int] = []
BINGO_BOARD: List[List[int]] = []
IS_MARKED: List[List[bool]] = [[False]*ROWS]*COLS


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# pylint: disable=C0103, C0116, W0511, w0612, C0200, W1203, W0613, W0621


# TODO: clean up code and mark positions on board
def main() -> None:
    fill_board(BINGO_BOARD=BINGO_BOARD)
    for i in range(0, ROWS):
        for j in range(0, COLS):
            print(f'{BINGO_BOARD[i][j]}' + ', ')
    print('we now have a bingo board !\n')
    # get out a random number
    # mark it
    # check to see if we have a bingo
    # if not, continue
    # if yes, break

def fill_board(BINGO_BOARD: List[List[int]]):
    num: int
    print('fill 25 different numbers to put in the board\n')
    for i in range (0, ROWS):
        col: List[int] = []
        for j in range (0, COLS):
            num = int(input('put a different number\n'))
            if not is_already_in_board(col=col, num=num):
                col.append(num)
                print(f'{num}\n')
        BINGO_BOARD.append(col)

def is_board_valid(BINGO_BOARD: List[List[int]]) -> bool:
    # go over board to scan if there are duplicates
    for i in range (0, ROWS):
        col: List[int] = []
        for j in range(0, COLS):
            # if yes, return false
            for k in range(0, i):
                if not is_already_in_board(col=BINGO_BOARD[k], num=BINGO_BOARD[i][j]):
                    continue
                return False
            if not is_already_in_board(col=col, num=BINGO_BOARD[i][j]):
                col.append(BINGO_BOARD[i][j])
            else:
                return False
    # else, return true
    return True

def is_already_in_board(col: List[int], num: int) -> bool:
    for i in range(0, len(col)):
        logging.debug(f'current square is {col[i]} and number is {num}\n')
        if col[i] == num:
            print("error: number can't be in the board more than once")
            return True
    return False

def test_bingo():
    board_one: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    board_two: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 1]]
    board_three: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 24]]
    assert is_board_valid(board_one) is True
    assert is_board_valid(board_three) is False
    assert is_board_valid(board_two) is False

def is_out(num: int) -> bool:
    if num in OUT_NUMBERS:
        return True
    return False
def random_number() -> int:
    # return a random number between 1 - 100
    num: int = random.randrange(1, 99, 1)
    # check to see if number has already been taken out
    if not is_out(num):
        OUT_NUMBERS[len(OUT_NUMBERS)] = num
        # if num in BINGO_BOARD:
            # find position in board
            # mark number in IS_MARKED
        return num
    # if yes, terminate program
    else:
        logging.error(f'{num} is already out, terminating program.\n')
        sys.exit(1)
# method for checking for a bingo


if __name__ == '__main__':
    main()
