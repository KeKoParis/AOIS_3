import bond_rule as br
import karnaugh as kar
import quine_method as quine


def calc_method(orig_expr):
    orig_expr = orig_expr.replace(' ', '')

    print('Calc')
    expr = list()
    if orig_expr.find(')+(') != -1:
        orig_expr = orig_expr.replace('(', '')
        orig_expr = orig_expr.replace(')', '')
        orig_expr = orig_expr.split('+')
        for i in range(len(orig_expr)):
            expr.append(orig_expr[i].split('*'))
        print(br.bond_pcnf(br.bond(expr)))

    else:
        orig_expr = orig_expr.replace('(', '')
        orig_expr = orig_expr.replace(')', '')
        orig_expr = orig_expr.split('*')
        for i in range(len(orig_expr)):
            expr.append(orig_expr[i].split('+'))
        print(br.bond(expr))


def quine_method(orig_expr):
    print('\n\nQuine')
    quine.solve(orig_expr)


def karnaugh_method(expr):
    table = [[0 for i in range(4)] for j in range(8)]
    table = kar.fill_table(table)

    for i in range(8):
        table = kar.solve(table, expr, i)

    for i in table:
        i[3] = int(i[3])

    kar_map = kar.fill_kar(table)

    row = kar.check_row(list(kar_map))
    square = kar.check_squares(list(kar_map))
    pairs_v = kar.check_pairs_vertical(list(kar_map))
    pairs_h_t = kar.check_horiz_pairs_top(kar_map)
    pairs_h_b = kar.check_horiz_pairs_bottom(kar_map)

    result = list()
    big_result = list()
    for i in range(len(kar_map)):
        for j in range(len(kar_map[i])):

            if kar_map[i][j] == 1:
                if row[i] and i == 0:
                    result.append('!x1')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif row[i] and i == 1:
                    result.append('x1')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif (square[j] and j == 0) or (square[(j // 2) * 2] and j == 1):
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif (square[j] and j == 1) or (square[j - 1] and j == 2):
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif (square[j] and j == 2) or (square[(j // 2) * 2] and j == 3):
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif (square[j] and j == 3) or (square[j - 1] and j == 3):
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_v[j] and j == 0:
                    result.append('!x2')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_v[j] and j == 1:
                    result.append('!x2')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_v[j] and j == 2:
                    result.append('x2')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_v[j] and j == 3:
                    result.append('x2')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_t[j] and j == 0:
                    result.append('!x1')
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_t[j] and j == 1:
                    result.append('!x1')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_t[j] and j == 2:
                    result.append('!x1')
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_t[j] and j == 3:
                    result.append('!x1')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_b[j] and j == 0:
                    result.append('x1')
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_b[j] and j == 1:
                    result.append('x1')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_b[j] and j == 2:
                    result.append('x1')
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    continue
                elif pairs_h_b[j] and j == 3:
                    result.append('x1')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    continue
    big_result = remove_similar(big_result)
    print()
    print('\nKarnaugh map')
    result_str = ''

    for i in big_result:
        for j in i:
            result_str += j
            result_str += '*'
        result_str = result_str[:-1]
        result_str += ' + '
    result_str = result_str[:-1]

    for i in kar_map:
        print(i)
    print('mdnf', result_str)


def remove_similar(result):
    curr = list()

    for i in result:
        check = 0
        for j in curr:
            if i == j:
                check += 1
        if check == 0:
            curr.append(i)

    return curr


def main():
    # orig_expr = input('Enter expression: ')
    # FUNCTION: ((x1*!x2)+((!x1+x2)*x3))
    function = '((x1*!x2)+((!x1+x2)*x3))'
    # orig_expr = '(x1 + x2 + x3)*(x1 + !x2 + x3)*(!x1 + !x2 + x3)'
    # orig_expr = '(!x1 * !x2 * x3)+(!x1 * x2 * x3)+(x1 * !x2 * !x3)+(x1 * !x2 * x3)+(x1 * x2 * x3)'
    # function = '(!x1+(x2*x3))'

    orig_expr = '(!x1 + x2 + x3)*(!x1+ x2+ !x3)*(!x1 + !x2 + x3)'
    calc_method(orig_expr)
    quine_method(orig_expr)
    karnaugh_method(function)


if __name__ == '__main__':
    main()
