import bond_rule as br
import karnaugh as kar
import quine_method as quine
import check_karno as ck


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
        minimized = br.bond_pcnf(br.bond(expr))
        result = ""
        for i in minimized:
            for j in i:
                result += str(j)
            result += " + "

    else:
        orig_expr = orig_expr.replace('(', '')
        orig_expr = orig_expr.replace(')', '')
        orig_expr = orig_expr.split('*')
        for i in range(len(orig_expr)):
            expr.append(orig_expr[i].split('+'))
        minimized = br.bond(expr)
        result = ""
        for i in minimized:
            for j in i:
                result += str(j) + "+"
            result = result[:-1]
            result += " * "

    result = result[:-3]
    print(result)


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

    karn_check = ck.KarnoCheck(kar_map)

    big_result = karn_check.check_karno()
    print()
    print('\nKarnaugh map')
    result_str = ''

    for i in big_result:
        for j in i:
            result_str += j
            result_str += '*'
        result_str = result_str[:-1]
        result_str += ' + '
    result_str = result_str[:-3]

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
