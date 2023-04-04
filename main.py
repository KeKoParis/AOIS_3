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


def main():
    # orig_expr = input('Enter expression: ')
    # FUNCTION: ((x1*!x2)+((!x1+x2)*x3))
    function = '((x1*!x2)+((!x1+x2)*x3))'
    # orig_expr = '(x1 + x2 + x3)*(x1 + !x2 + x3)*(!x1 + !x2 + x3)'
    # orig_expr = '(!x1 * !x2 * x3)+(!x1 * x2 * x3)+(x1 * !x2 * !x3)+(x1 * !x2 * x3)+(x1 * x2 * x3)'

    # calc_method(orig_expr)
    # quine_method(orig_expr)
    karnaugh_method(function)


if __name__ == '__main__':
    main()
