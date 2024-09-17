#!/usr/bin/env python3
''' Bingo '''
import logging
import random
from typing import List
ROWS: int = 5
COLS: int = 5
NUMBER_OF_NUMBERS: int = 99
OUT_NUMBERS: List[int] = [0] * NUMBER_OF_NUMBERS
BINGO_BOARD: List[List[int]] = [[0]*ROWS]*COLS
NUMBER_FOR_BINGO: int = 5
IS_MARKED: List[List[bool]] = [[False]*ROWS]*COLS


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# pylint: disable=C0103, C0116, W0511, w0612, C0200, W1203, W0613, W0621

def its_bingo_time(BINGO_BOARD: List[List[int]]) -> str:
    out_counter: int = 0
    # checking if board is valid
    is_board_valid(BINGO_BOARD = BINGO_BOARD)
    # get out a random number
    num: int = random_number(out_counter=out_counter)
    logging.debug(f'num is {num} and counter is {out_counter}')
    while num != -1:
        # check to see if we have a bingo
        if is_bingo():
            # if yes, break
            return "You got a bingo !\n"
        # if not, continue
        out_counter += 1
        num = random_number(out_counter=out_counter)
        logging.debug(f'num is {num} and counter is {out_counter}')

    logging.error(f'{num} is already out, terminating program.\n')
    return "Game Over !\n"


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
        if col[i] == num:
            print("error: number can't be in the board more than once")
            return True
    return False

# TODO: there is a bug where it doesn't keep track of the numbers that have come out correctly
def is_out(num: int) -> bool:
    if num in OUT_NUMBERS:
        return True
    return False
def random_number(out_counter: int) -> int:
    # return a random number between 1 - 100
    num: int = random.randrange(1, 25, 1)
    # logging.debug(f'num is {num} and count is {out_counter}\n')
    # check to see if number has already been taken out
    if not is_out(num):
        # if not, add to list
        OUT_NUMBERS[out_counter] = num
        logging.debug(f'counter = {out_counter}')
        # marking in board
        is_in_board(num)
        return num
    # if yes, terminate program
    return -1
# finding a number in the board
def is_in_board(num: int) -> bool:
    for i in range(0, ROWS):
        for j in range(0, COLS):
            if num == BINGO_BOARD[i][j]:
                # marking the number
                IS_MARKED[i][j] = True
                return True
    return False
# method for checking for a bingo
def is_bingo() -> bool:
    if is_row():
        return True
    if is_col():
        return True
    if is_upper_diagional():
        return True
    if is_lower_diagional():
        return True
    return False

def is_row() -> bool:
    count: int = 0
    for i in range(0, ROWS):
        for j in range(0, COLS):
            if IS_MARKED[i][j]:
                count +=1
        if count == NUMBER_FOR_BINGO:
            return True
        count = 0
    return False

def is_col() -> bool:
    count: int = 0
    for j in range(0, COLS):
        for i in range(0, ROWS):
            if IS_MARKED[i][j]:
                count +=1
        if count == NUMBER_FOR_BINGO:
            return True
        count = 0
    return False

def is_upper_diagional() -> bool:
    count: int = 0
    i : int = 0
    j : int = 0
    while i < ROWS and j < COLS:
        if IS_MARKED[i][j]:
            count += 1
        i += 1
        j += 1
        if count != i:
            return False
    return True

def is_lower_diagional() -> bool:
    count: int = 0
    i : int = ROWS - 1
    j : int = 0
    while i >= 0 and j < COLS:
        if IS_MARKED[i][j]:
            count += 1
        i -= 1
        j += 1
        if count != j:
            return False
    return True

def test_bingo():
    board_one: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    board_two: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 1]]
    board_three: List[List[int]] = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 24]]
    assert its_bingo_time(board_one), "You got a bingo !\n"
    # assert its_bingo_time(board_two), "You got a bingo !\n"
    # assert its_bingo_time(board_three), "You got a bingo !\n"
    # assert is_board_valid(board_one) is True
    # assert is_board_valid(board_three) is False
    # assert is_board_valid(board_two) is False
