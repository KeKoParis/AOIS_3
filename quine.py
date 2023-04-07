def bond(expr):
    new_const = list()
    for i in range(len(expr)):
        for j in range(len(expr)):
            if i != j and if_similar(expr[i], expr[j]):
                new_const.append(create_new_const(expr[i], expr[j]))

    new_const = remove_similar(new_const)
    new_const = new_const + additional(new_const)
    table = [[0 for i in range(len(new_const))] for j in range(len(expr))]

    for j in range(len(expr)):
        for i in range(len(new_const)):
            table[j][i] = is_there(expr[j], new_const[i])

    bonded = list()
    for j in range(len(expr)):
        num_ones = 0
        for i in range(len(new_const)):
            if table[j][i] == 1:
                num_ones += 1
        if num_ones == 1:
            for i in range(len(new_const)):
                if table[j][i] == 1:
                    bonded.append(new_const[i])

    zeros = 0
    for j in range(len(expr)):
        for i in range(len(new_const)):
            if len(new_const[i]) == 1:
                if table[j][i] == 0:
                    zeros += 1

    for i in range(len(new_const)):
        if len(new_const[i]) == 1 and zeros == 1:
            bonded.append(new_const[i])
            break

    print('\nQuine')
    print(bonded)


def is_there(first_expr, second_expr):
    count_similar = 0
    for i in second_expr:
        for j in first_expr:
            if i == j:
                count_similar += 1
        if count_similar == len(second_expr):
            return 1

    return 0


def if_similar(first_expr, second_expr):
    similar = 0
    for i in first_expr:
        for j in second_expr:
            if i[-1] == j[-1]:
                similar += 1
                break

    two_similar = 0

    for i in first_expr:
        for j in second_expr:
            if i == j:
                two_similar += 1
                break

    if similar == len(first_expr) and two_similar == 2:
        return True
    return False


def remove_similar(expr):
    fixed_expr = list()
    for i in expr:
        try:
            fixed_expr.index(i)
        except ValueError:
            fixed_expr.append(i)

    return fixed_expr


def create_new_const(first_expr, second_expr):
    new_const = list()

    for i in first_expr:
        for j in second_expr:
            if i == j:
                new_const.append(i)
                break
    return new_const


def additional(expr):
    new_const = list()
    for i in range(len(expr)):
        for j in range(len(expr)):
            if i != j and is_similar(expr[i], expr[j]):
                new_const.append(create_new_const(expr[i], expr[j]))

    new_const = remove_similar(new_const)
    return new_const


def is_similar(first_expr, second_expr):
    same = 0
    similar = 0
    for i in first_expr:
        for j in second_expr:
            if i[-1] == j[-1]:
                same += 1
            if i == j:
                similar += 1

    if same == 2 and similar == 1:
        return True
    return False
