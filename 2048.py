import tkinter as tk
from tkinter import *
import random

def sum_2048(board, action):
    
    if type(action) != str:
        print('ERROR: "action" should be string')
        return
    
    def indx(action):
        
        if action in ('Right', 'Down'):
            ind = [[j for j in range(len(board))] for i in range(len(board))]
        else:
            ind = [[j for j in range(len(board)-1, -1, -1)] for i in range(len(board))]
        
        indx = []
        for i in range(len(ind)):
            for j in ind[i]:
                if action in ('Down', 'Up'):
                    indx.append([j, i])
                else:
                    indx.append([i, j])
        return indx
    
    def calculate(board, action):
        change = 0
        ind = indx(action)    
        for k in range(len(ind)-1, 0, -1):
            i = ind[k][0]
            j = ind[k][1]
            i_l = i
            j_l = j
            if k > 0:
                i_l = ind[k-1][0]
                j_l = ind[k-1][1]
            if board[i_l][j_l] != 0 and ((i != i_l and j == j_l) or (i == i_l and j != j_l)):
                if board[i][j] == board[i_l][j_l]:
                    board[i][j] += board[i_l][j_l]
                    board[i_l][j_l] = 0
                    change = 1
                if board[i][j] == 0:
                    board[i][j] = board[i_l][j_l]
                    board[i_l][j_l] = 0
                    change = 1
        if change == 1:
            board = calculate(board, action)
        return board
    
    board = calculate(board, action)
    return board


def add_random_num(board):
    global label, over
    empty_cells = []
    rand_num = [1, 2, 4]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty_cells.append([i, j])
    total_empty = len(empty_cells)
    if total_empty == 0:
        over = 1
        return
    add_cell = random.randrange(0, total_empty, 1)
    board[empty_cells[add_cell][0]][empty_cells[add_cell][1]] = random.choice(rand_num)
    return board


def check_max_num(board):
    max_element = 0
    for line in board:
        for element in line:
            if element > max_element:
                max_element = element
    return max_element


def calculate_total(board):
    total = 0
    for line in board:
        for element in line:
            total += element
    return total


def random_start_board(board_dimention):
    board = [[0 for i in range(board_dimention)] for j in range(board_dimention)]
    cells = []
    updated_cells = []
    for i in range(board_dimention):
        for j in range(board_dimention):
            cells.append([i, j])
    total_cells = len(cells)
    ones_num = random.randrange(0, total_cells // 3)
    twos_num = random.randrange(0, total_cells // 3)
    fours_num = random.randrange(0, total_cells // 4)

    for i in range(ones_num):
        i_j = cells.pop(random.randrange(0, len(cells), 1))
        ind_i = i_j[0]
        ind_j = i_j[1]
        board[ind_i][ind_j] = 1
    for i in range(twos_num):
        i_j = cells.pop(random.randrange(0, len(cells), 1))
        ind_i = i_j[0]
        ind_j = i_j[1]
        board[ind_i][ind_j] = 2
    for i in range(fours_num):
        i_j = cells.pop(random.randrange(0, len(cells), 1))
        ind_i = i_j[0]
        ind_j = i_j[1]
        board[ind_i][ind_j] = 4
    return board


def load_board(board):
    global board_0_0, board_0_1, board_0_2, board_0_3, board_1_0, board_1_1, board_1_2, board_1_3
    global board_2_0, board_2_1, board_2_2, board_2_3, board_3_0, board_3_1, board_3_2, board_3_3
    board_0_0 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_0_0.insert(END, board[0][0])
    board_0_0.grid(row=2, column=0)
    board_0_1 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_0_1.insert(END, board[0][1])
    board_0_1.grid(row=2, column=1)
    board_0_2 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_0_2.insert(END, board[0][2])
    board_0_2.grid(row=2, column=2)
    board_0_3 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_0_3.insert(END, board[0][3])
    board_0_3.grid(row=2, column=3)

    board_1_0 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_1_0.insert(END, board[1][0])
    board_1_0.grid(row=3, column=0)
    board_1_1 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_1_1.insert(END, board[1][1])
    board_1_1.grid(row=3, column=1)
    board_1_2 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_1_2.insert(END, board[1][2])
    board_1_2.grid(row=3, column=2)
    board_1_3 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_1_3.insert(END, board[1][3])
    board_1_3.grid(row=3, column=3)

    board_2_0 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_2_0.insert(END, board[2][0])
    board_2_0.grid(row=4, column=0)
    board_2_1 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_2_1.insert(END, board[2][1])
    board_2_1.grid(row=4, column=1)
    board_2_2 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_2_2.insert(END, board[2][2])
    board_2_2.grid(row=4, column=2)
    board_2_3 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_2_3.insert(END, board[2][3])
    board_2_3.grid(row=4, column=3)

    board_3_0 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_3_0.insert(END, board[3][0])
    board_3_0.grid(row=5, column=0)
    board_3_1 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_3_1.insert(END, board[3][1])
    board_3_1.grid(row=5, column=1)
    board_3_2 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_3_2.insert(END, board[3][2])
    board_3_2.grid(row=5, column=2)
    board_3_3 = tk.Entry(master, width=4, font=("Helvetica", 9, "bold"))
    board_3_3.insert(END, board[3][3])
    board_3_3.grid(row=5, column=3)


def refresh_board(board):
    global over
    if over == 0:
        board_0_0.delete(0, END)
        board_0_1.delete(0, END)
        board_0_2.delete(0, END)
        board_0_3.delete(0, END)
        board_1_0.delete(0, END)
        board_1_1.delete(0, END)
        board_1_2.delete(0, END)
        board_1_3.delete(0, END)
        board_2_0.delete(0, END)
        board_2_1.delete(0, END)
        board_2_2.delete(0, END)
        board_2_3.delete(0, END)
        board_3_0.delete(0, END)
        board_3_1.delete(0, END)
        board_3_2.delete(0, END)
        board_3_3.delete(0, END)
        board_0_0.insert(0, board[0][0])
        board_0_1.insert(0, board[0][1])
        board_0_2.insert(0, board[0][2])
        board_0_3.insert(0, board[0][3])
        board_1_0.insert(0, board[1][0])
        board_1_1.insert(0, board[1][1])
        board_1_2.insert(0, board[1][2])
        board_1_3.insert(0, board[1][3])
        board_2_0.insert(0, board[2][0])
        board_2_1.insert(0, board[2][1])
        board_2_2.insert(0, board[2][2])
        board_2_3.insert(0, board[2][3])
        board_3_0.insert(0, board[3][0])
        board_3_1.insert(0, board[3][1])
        board_3_2.insert(0, board[3][2])
        board_3_3.insert(0, board[3][3])


def left():
    game('Left')


def right():
    game('Right')


def up():
    game('Up')


def down():
    game('Down')


def game(action):
    global board, total, max_num, over, label
    if over == 0:
        board = sum_2048(board, action)
        board = add_random_num(board)
        refresh_board(board)
    if over == 0:
        total = tk.Label(master, text="Total score: {}".format(calculate_total(board)), font=("Helvetica", 10)).grid(row=1, column=0, pady=3, columnspan=4)
        max_num = tk.Label(master, text="Max element: {}".format(check_max_num(board)), font=("Helvetica", 10)).grid(row=1, column=4, columnspan=4)
        if check_max_num(board) >= 2048:
            over = 2
    if over == 1:
        label = tk.Label(master, text="            GAME OVER!            ", font=("Helvetica", 15, 'bold')).grid(row=0, column=0, pady=3, columnspan=8)
        print("No empty cells left - you have lost.")
    if over == 2:
        label = tk.Label(master, text="            YOU WIN!            ", font=("Helvetica", 15, 'bold')).grid(row=0, column=0, pady=3, columnspan=8)
        print("You collected 2048 - you won!")


# ______________________________________MAIN PROGRAM______________________________________
print("Game started - please do NOT close this window.")
over = 0
board = random_start_board(4)
master = tk.Tk()
Title = master.title("2048 Game")
label = tk.Label(master, text="Please use buttons for moving cells", font=("Helvetica", 10)).grid(row=0, column=0, pady=3, columnspan=8)
total = tk.Label(master, text="Total score: {}".format(calculate_total(board)), font=("Helvetica", 10)).grid(row=1, column=0, pady=3, columnspan=4)
max_num = tk.Label(master, text="Max element: {}".format(check_max_num(board)), font=("Helvetica", 10)).grid(row=1, column=4, columnspan=4)
load_board(board)
tk.Button(master, text='<-', font=("Helvetica", 9, "bold"), command=left, width=5).grid(row=3, column=5, pady=0, padx=5, columnspan=1, rowspan=2, stick=W)
tk.Button(master, text='->', font=("Helvetica", 9, "bold"), command=right, width=5).grid(row=3, column=7, pady=0, padx=5, columnspan=1, rowspan=2, stick=W)
tk.Button(master, text='^', font=("Helvetica", 9, "bold"), command=up, width=5).grid(row=2, column=6, pady=0, padx=5, rowspan=2, stick=W)
tk.Button(master, text='v', font=("Helvetica", 9, "bold"), command=down, width=5).grid(row=4, column=6, pady=0, padx=5, rowspan=2, stick=W)
tk.Button(master, text='Quit', font=("Helvetica", 9, "bold"), command=master.quit, width=20, heigh=2).grid(row=8, column=0, pady=5, columnspan=8)

tk.mainloop()
