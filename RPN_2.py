import sys


'''
Run: python RPN_2.py "a b +"
Variables input: a 2 b 3
'''


class Calculator:
    def __init__(self):
        self._expression = []
        self._variables = {}
        self._op_dict = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

    def run(self):
        self._expression = self._handle_expression()
        stop = False
        while not stop:
            try:
                print("Expression: {}\nInsert variables:".format(self._expression))
                variables_str = input().strip()
                self._parse_variables_input(variables_str)
                res = self._calc_result()
                print("= {}".format(res))
            except EOFError:
                stop = True
        print("Good Bye")

    def _handle_expression(self):
        assert (len(sys.argv) == 2)
        expression_str = sys.argv[1].strip().split()
        expression = []
        # simplify expression
        print("\nExpression: {}".format(expression_str))
        for item in expression_str:
            if self._is_operand(item):
                if self._is_digit(item):
                    item = int(item)
                expression.append(item)
            else:  # operator
                assert (len(expression) >= 2)
                operator = item
                operand_2, operand_1 = expression.pop(), expression.pop()
                if type(operand_1) == int and type(operand_2) == int:
                    tmp_res = self._op_dict[operator](operand_1, operand_2)
                    expression.append(tmp_res)
                else:
                    expression.append(operand_1)
                    expression.append(operand_2)
                    expression.append(operator)
        return expression

    def _parse_variables_input(self, variables_str):
        if not variables_str:
            return
        variables_arr = variables_str.split(' ')
        assert (len(variables_arr) % 2 == 0)
        for i in range(0, len(variables_arr), 2):
            self._variables[variables_arr[i]] = int(variables_arr[i+1])

    def _calc_result(self):
        stack = []
        for item in self._expression:
            if self._is_operand(item):
                stack.append(item)
            else:  # operator
                assert (len(stack) >= 2)
                operand_2, operand_1 = stack.pop(), stack.pop()
                tmp_res = self._calc_tmp_exp(operand_1, operand_2, item)
                stack.append(tmp_res)
        assert (len(stack) == 1)
        return stack.pop()

    def _calc_tmp_exp(self, operand_1, operand_2, operator):
        if operand_1 in self._variables:
            operand_1 = self._variables[operand_1]
        if operand_2 in self._variables:
            operand_2 = self._variables[operand_2]

        return self._op_dict[operator](operand_1, operand_2)

    @staticmethod
    def _is_digit(item):
        return item.isdigit() or (item[0] == '-' and item[1:].isdigit())

    @staticmethod
    def _is_operand(item):
        return item not in ['+', '-', '*', '/']


if __name__ == '__main__':
    Calculator().run()