import numpy as np
import matplotlib.pyplot as plt


def display_nqueens(sol):
    board = [[0] * len(sol) for i in range(len(sol))]
    for x,y in sol:
        board[x][y] = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            symbol = '♛' if board[i][j] == 1 else '.'
            print(symbol, end = ' ')
        print()


def display_sudoku(sol):
    fig, ax = plt.subplots(figsize =(4,4))
    min_val, max_val = 0, 9
    for l in range(9):
        for c in range(9):
            v = sol[c][l]
            s = " "
            if v > 0:
                s = str(v)
            ax.text(l+0.5,8.5-c, s, va='center', ha='center')
        ax.set_xlim(min_val, max_val)
    ax.set_ylim(min_val, max_val)
    ax.set_xticks(np.arange(max_val))
    ax.set_yticks(np.arange(max_val))
    ax.grid()
    plt.show()