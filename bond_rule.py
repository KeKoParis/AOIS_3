def bond(expr):
    bonded_expr = find_two_similar(expr)
    bonded_expr = remove_similar(bonded_expr)
    return bonded_expr


def remove_similar(expr):
    fixed_expr = list()
    for i in expr:
        try:
            fixed_expr.index(i)
        except ValueError:
            fixed_expr.append(i)

    return fixed_expr


def find_two_similar(expr):
    new_const = list()
    for i in range(len(expr)):
        for j in range(len(expr)):
            if i != j and is_similar(expr[i], expr[j]):
                new_const.append(create_new_const(expr, i, j))

    return new_const


def is_similar(first_expr, second_expr):
    count_similar = 0
    for i in first_expr:
        for j in second_expr:
            if i == j:
                count_similar += 1

    if count_similar >= len(first_expr) - 1 and count_similar > 1:
        return True

    return False


def create_new_const(expr, first_num, second_num):
    new_const = list()
    for i in range(len(expr[first_num])):
        for j in range(len(expr[second_num])):
            if expr[first_num][i] == expr[second_num][j]:
                new_const.append(expr[first_num][i])

    return new_const


def bond_pcnf(expr):
    for i in expr:
        for j in expr:
            if i != j and is_similar_pcnf(i, j):
                compose(i, j)
                expr.remove(j)
    expr = remove_similar(expr)
    return expr


def compose(first_expr, second_expr):
    if first_expr[0] != second_expr[0]:
        first_expr.remove(first_expr[0])
    else:
        first_expr.remove(first_expr[1])


def is_similar_pcnf(first_expr, second_expr):
    count = 0

    for i in first_expr:
        for j in second_expr:
            if i[-1] == j[-1]:
                count += 1

    if count == len(first_expr):
        return True
    return False
