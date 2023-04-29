import re


def solve(curr_table, curr_expression, index):  # finds pcnf and pdnf

    curr_expression = replace_negation(curr_table, curr_expression, index)
    curr_expression = replace_positive(curr_table, curr_expression, index)
    curr_expression = replace_signs(curr_expression)

    curr_table[index][3] = solve_expr(curr_expression)  # resolves logical expression

    return curr_table


# !((x1+!x2)*(x2+!x3))
def solve_sub_str(sub_str):
    sub_str = sub_str[1:len(sub_str) - 1]
    if sub_str[0] == '1' and sub_str[1] == 'a' and sub_str[len(sub_str) - 1] == '1':
        return '1'
    if (sub_str[0] == '1' or sub_str[len(sub_str) - 1] == '1') and sub_str[1] == 'o':
        return '1'
    return '0'


# ((x1+x2)*x3)

def check_neg(expr):
    expr = expr.replace("!0", "1")
    expr = expr.replace("!1", "0")
    return expr


# (((x1+!x2)*x3)+(x3*!x2))
def solve_expr(curr_expression):
    while re.search(r'\([01]+[or|and]+[01]+\)', curr_expression):
        curr_expression = check_neg(curr_expression)
        curr_expression = curr_expression.replace(re.search(r'\([01]+[or|and]+[01]+\)', curr_expression).group(),
                                                  solve_sub_str(
                                                      re.search(r'\([01]+[or|and]+[01]+\)', curr_expression).group()))

        curr_expression = check_neg(curr_expression)

    return curr_expression


def replace_negation(curr_table, curr_expression, index):  # replaces negation vars to their values
    while curr_expression.find("!x1") != -1:
        curr_expression = curr_expression.replace("!x1", str(abs(curr_table[index][0] - 1)))
    while curr_expression.find("!x2") != -1:
        curr_expression = curr_expression.replace("!x2", str(abs(curr_table[index][1] - 1)))
    while curr_expression.find("!x3") != -1:
        curr_expression = curr_expression.replace("!x3", str(abs(curr_table[index][2] - 1)))

    return curr_expression


def replace_positive(curr_table, curr_expression, index):  # replaces positive vars to their values
    while curr_expression.find("x1") != -1:
        curr_expression = curr_expression.replace('x1', str(curr_table[index][0]))
        break
    while curr_expression.find("x2") != -1:
        curr_expression = curr_expression.replace("x2", str(curr_table[index][1]))
    while curr_expression.find("x3") != -1:
        curr_expression = curr_expression.replace("x3", str(curr_table[index][2]))

    return curr_expression


def replace_signs(curr_expression):  # replaces signs to their logical equivalent in python
    while curr_expression.find("+") != -1:
        curr_expression = curr_expression.replace("+", "or")
    while curr_expression.find("*") != -1:
        curr_expression = curr_expression.replace("*", "and")

    return curr_expression


def fill_table(curr_table):
    check = 0
    for i in range(8):
        if i < 4:
            curr_table[i][0] = 0
        else:
            curr_table[i][0] = 1

        if check == 4:
            check = 0

        if check < 2:
            curr_table[i][1] = 0
        else:
            curr_table[i][1] = 1

        if i % 2 == 0:
            curr_table[i][2] = 0
        else:
            curr_table[i][2] = 1

        check = check + 1

    return curr_table


def fill_kar(table):
    kar = [[1, 2, 4, 3],
           [5, 6, 8, 7]]

    for i in range(len(kar)):
        for j in range(len(kar[i])):
            kar[i][j] = table[kar[i][j] - 1][3]

    return kar


def check_row(karn_map):
    row = 0
    rows = [False for i in range(2)]

    for i in range(len(karn_map)):
        for j in range(len(karn_map[i])):
            if karn_map[i][j] != 0:
                row += 1
        if row == 4:
            rows[i] = True
        row = 0

    return rows


def check_squares(karn_map):
    square = [False for i in range(4)]

    for i in range(3):
        if karn_map[0][i] != 0 and karn_map[0][i + 1] != 0 and karn_map[1][i] != 0 and karn_map[1][i + 1] != 0:
            square[i] = True

    if karn_map[0][3] != 0 and karn_map[0][0] != 0 and karn_map[1][3] != 0 and karn_map[1][0] != 0:
        square[3] = True

    return square


def check_pairs_vertical(karn_map):
    pairs = [False for i in range(4)]

    for i in range(len(karn_map[0])):
        if karn_map[0][i] != 0 and karn_map[1][i] != 0:
            pairs[i] = True

    return pairs


def check_horiz_pairs_top(karn_map):
    pairs = list()
    for i in range(3):
        if karn_map[0][i] == 1 and karn_map[0][i + 1] == 1:
            pairs.append(True)
        else:
            pairs.append(False)

    if karn_map[0][3] == 1 and karn_map[0][1] == 1:
        pairs.append(True)
    else:
        pairs.append(False)

    return pairs


def check_horiz_pairs_bottom(karn_map):
    pairs = list()
    for i in range(3):
        if karn_map[1][i] == 1 and karn_map[1][i + 1] == 1:
            pairs.append(True)
        else:
            pairs.append(False)

    if karn_map[1][3] == 1 and karn_map[1][0] == 1:
        pairs.append(True)
    else:
        pairs.append(False)

    return pairs
