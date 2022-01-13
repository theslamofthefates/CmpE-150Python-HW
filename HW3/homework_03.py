glass_size = int(input())
straw_pos = int(input())

glass_size_copyF = glass_size
number_of_shots = 0
f = glass_size * 2 - straw_pos + 1

if f % 2 == 0:
    number_of_shots = f // 2
else:
    number_of_shots = (f + 1)//2

"""
 NOTES
    1-For all functions that start with n, the preceding n indicates that the function will print the string for n times
    2- I tried to make naming as obvious as possible. Therefore, I may not explain what each stands for.
    3- Each function has an if-elif structure which determines when the terminate the recursion.
"""


def n_empty(execution_time):
    if execution_time > 0:
        print(" ", end='')
    elif execution_time <= 0:
        return
    n_empty(execution_time - 1)


def n_asterix(execution_time):
    if execution_time > 0:
        print("*", end='')
    elif execution_time <= 0:
        return
    n_asterix(execution_time - 1)


def n_straw(execution_time, inside_execution_time, ins_con):
    if execution_time > 0:
        n_empty(ins_con)
    elif execution_time <= 0:
        return
    print("o")
    n_straw(execution_time - 1, inside_execution_time, ins_con + 1)


def straw(straw_size):
    n_straw(straw_size, straw_size, 0)


# upper_body is the function that prints the drunk parts of the glass.
def upper_body(b, contr, glass_size_copyF, straw_pos, pre_space=0):  # b = 0
    if b < contr:
        n_empty(pre_space)
        print("\\", end='')
        n_empty(straw_pos + b - pre_space - 1)
        print("o", end='')
        afterSpace = 2 * glass_size_copyF - straw_pos - 1
        n_empty(afterSpace - 1)
        print("/")
        return upper_body(b + 1, contr, glass_size_copyF - 1, straw_pos, pre_space + 1)
    else:
        return pre_space


# bottom_body is the functions that prints the remaining parts of the glass.
def bottom_body(glass_size, i, preSpace, contr=0):
    if contr + 1 < glass_size - i:
        n_empty(preSpace)
        print("\\", end='')
        n_asterix(2 * (glass_size - i - contr - 1))
        print("/")
        bottom_body(glass_size, i, preSpace + 1, contr + 1)
    else:
        return


# tail is the function that prints the rest of glass.
def tail(glass_size, contr=0):
    if contr == 0:
        n_empty(glass_size)
        print("--")
    if contr < glass_size:
        n_empty(glass_size)
        print("||")
        tail(glass_size, contr + 1)
    else:
        return


# last main function that starts to all printing and recursively calls itself
def general_function(number_of_shots, contr=0):
    if contr < number_of_shots:
        straw(straw_pos)
        preSpace = upper_body(0, contr, glass_size + 1, straw_pos)
        bottom_body(glass_size + 1, contr, preSpace)
        tail(glass_size)
        general_function(number_of_shots, contr + 1)
    else:
        return


general_function(number_of_shots + 1)