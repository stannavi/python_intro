# Задача 1. Создайте программу для игры в "Крестики-нолики".

import os
import time
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")


def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False


def is_board_full(board):
    if " " in board:
        return False
    else:
        return True


def get_computer_move(board, player):
    if board[5] == " ":
        return 5

    while True:
        move = random.randint(1, 9)
        if board[move] == " ":
            return move
            break
    return 5


while True:
    os.system("cls")
    print_board()

    choice = input("Первый ход делает игрок (X): ")
    choice = int(choice)

    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Это место занято.")
        time.sleep(1)

    if is_winner(board, "X"):
        os.system("cls")
        print_board()
        print("Вы победили!")
        break

    os.system("cls")
    print_board()

    if is_board_full(board):
        print("Ничья!")
        break

    choice = get_computer_move(board, "O")

    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Место занято!")
        time.sleep(1)

    if is_winner(board, "O"):
        os.system("cls")

        print_board()
        print("Бот победил!")
        break

    if is_board_full(board):
        print("Ничья!")
        break

# Задача 2. Напишите программу вычисления арифметического выражения заданного
# строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

def parse_math_expression(exp):
    PRECENDENCE = {
        ')': 3,
        '(': 3,
        '*': 1,
        '/': 1,
        '+': 0,
        '-': 0,
    }
    output = []
    operators = []
    for ch in exp:
        # Handle nested expressions
        if ch == ')':
            opr = operators.pop(0)
            while opr != '(':
                output.append(opr)
                opr = operators.pop(0)
        elif ch.isdigit():
            output.append(ch)
        else:
            # Handle operator prescendence
            top_op = None
            if len(operators) and operators[0]:
                top_op = operators[0]
            # Check if top operator has greater prcendencethan current char
            if top_op in ['*', '/'] and PRECENDENCE[top_op] > PRECENDENCE[ch]:
                output.append(top_op)
                operators.pop(0)
            # Push operator onto queues
            operators.insert(0, ch)
    # Handle any leftover operators
    while len(operators):
        output.append(operators.pop(0))
    return output


def eval_parsed_expression(exp):
    OPRS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    tmp = []
    while len(exp) > 1:
        k = exp.pop(0)
        while not k in ['*', '-', '+', '/']:
            tmp.insert(0, k)
            k = exp.pop(0)
        o = k
        b = tmp.pop(0)
        a = tmp.pop(0)
        r = OPRS[o](int(a), int(b))
        exp.insert(0, r)
    return exp[0]

text = input("Введите арифметическое выражение: ")
text = text.replace(" ","")
exp_list = parse_math_expression(text)

print(eval_parsed_expression(exp_list))
