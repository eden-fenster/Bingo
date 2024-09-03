#!/usr/bin/env python3
import logging
import sys
from typing import List



def main():
    NUMBERS: int = 100
    ROW: int = 5
    COL: int = 5

    bingo_board: List[List[int]] = [[1, 2, 3 ,4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    for i in range(0, ROW):
        for j in range(0, COL):
            print(f'{bingo_board[i][j]}' + '\n')
            print('we now have a bingo board !\n')

if __name__ == '__main__':
    main()

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

