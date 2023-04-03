import bond_rule as br
import quine


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


def main():
    # orig_expr = input('Enter expression: ')
    # FUNCTION: ((x1*!x2)+((!x1+x2)*x3))
    orig_expr = '(x1 + x2 + x3)*(x1 + !x2 + x3)*(!x1 + !x2 + x3)'
    # orig_expr = '(!x1 * !x2 * x3)+(!x1 * x2 * x3)+(x1 * !x2 * !x3)+(x1 * !x2 * x3)+(x1 * x2 * x3)'

    calc_method(orig_expr)
    quine_method(orig_expr)


if __name__ == '__main__':
    main()
