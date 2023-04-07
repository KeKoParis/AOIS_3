import bond_rule as br
import quine
import karnaugh as kar


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
    orig_expr = orig_expr.replace(' ', '')

    expr = list()
    if orig_expr.find(')+(') != -1:
        orig_expr = orig_expr.replace('(', '')
        orig_expr = orig_expr.replace(')', '')
        orig_expr = orig_expr.split('+')
        for i in range(len(orig_expr)):
            expr.append(orig_expr[i].split('*'))
        quine.bond(expr)

    else:
        orig_expr = orig_expr.replace('(', '')
        orig_expr = orig_expr.replace(')', '')
        orig_expr = orig_expr.split('*')
        for i in range(len(orig_expr)):
            expr.append(orig_expr[i].split('+'))
        quine.bond(expr)


def karnaugh_method(expr):
    table = [[0 for i in range(4)] for j in range(8)]
    table = kar.fill_table(table)

    for i in range(8):
        table = kar.solve(table, expr, i)

    kar_map = kar.fill_kar(table)

    for i in kar_map:
        print(i)
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
                    break
                elif row[i] and i == 1:
                    result.append('x1')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif (square[j] and j == 0) or (square[(j//2)*2] and j == 1):
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif (square[j] and j == 1) or (square[j-1] and j == 2):
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif (square[j] and j == 2) or (square[(j//2)*2] and j == 3):
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif (square[j] and j == 3) or (square[j-1] and j == 3):
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_v[j] and j == 0:
                    result.append('!x2')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_v[j] and j == 1:
                    result.append('!x2')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_v[j] and j == 2:
                    result.append('x2')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_v[j] and j == 3:
                    result.append('x2')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_t[j] and j == 0:
                    result.append('!x1')
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_t[j] and j == 1:
                    result.append('!x1')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_t[j] and j == 2:
                    result.append('!x1')
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_t[j] and j == 3:
                    result.append('!x1')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_b[j] and j == 0:
                    result.append('!x1')
                    result.append('!x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_b[j] and j == 1:
                    result.append('!x1')
                    result.append('x3')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_b[j] and j == 2:
                    result.append('!x1')
                    result.append('x2')
                    big_result.append(list(result))
                    result.clear()
                    break
                elif pairs_h_b[j] and j == 3:
                    result.append('!x1')
                    result.append('!x3')
                    big_result.append(list(result))
                    result.clear()
                    break

    print()
    print('Karnaugh map')
    print(big_result)


def main():
    # orig_expr = input('Enter expression: ')
    # FUNCTION: ((x1*!x2)+((!x1+x2)*x3))
    function = '((x1*!x2)+((!x1+x2)*x3))'
    orig_expr = '(x1 + x2 + x3)*(x1 + !x2 + x3)*(!x1 + !x2 + x3)'
    # orig_expr = '(!x1 * !x2 * x3)+(!x1 * x2 * x3)+(x1 * !x2 * !x3)+(x1 * !x2 * x3)+(x1 * x2 * x3)'
    calc_method(orig_expr)
    # quine_method(orig_expr)
    karnaugh_method(function)


if __name__ == '__main__':
    main()
