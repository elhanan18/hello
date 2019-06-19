import sys


class Calculator:
    def __init__(self):
        self._expression = []
        self._variables = {}

    def run(self):
        self._handle_expression()
        stop = False
        while not stop:
            try:
                print("\nExpression: {}\nInsert variables:".format(self._expression))
                variables_str = input().strip()
                self._parse_variables_input(variables_str)
                res = self._calc_result()
                print("= {}".format(res))
            except EOFError:
                stop = True
        print("Good Bye")

    def _handle_expression(self):
        for item in sys.argv[1].strip().split():
            if self._is_operand(item):
                if self._is_digit(item):
                    item = int(item)
                self._expression.append(item)
            else:  # operator
                assert (len(self._expression) >= 2)
                operand_2, operand_1 = self._expression.pop(), self._expression.pop()
                if self._is_digit(operand_1) and self._is_digit(operand_2):
                    tmp_res = self._calc_tmp_exp(operand_1, operand_2, item)
                    self._expression.append(tmp_res)
                else:
                    self._expression.append(operand_1)
                    self._expression.append(operand_2)
                    self._expression.append(item)

    def _parse_variables_input(self, variables_str):
        if not variables_str:
            return
        variables_arr = variables_str.split(' ')
        assert (len(variables_arr) % 2 == 0)
        for i in range(0, len(variables_arr), 2):
            self._variables[variables_arr[i]] = int(variables_arr[i+1])

    def _calc_result(self):
        stack = []
        for item in self._expression.split():
            if self._is_operand(item):
                if self._is_digit(item):
                    item = int(item)
                stack.append(item)
            else:  # operator
                assert (len(stack) >= 2)
                operand_2, operand_1 = stack.pop(), stack.pop()
                tmp_res = self._calc_tmp_exp(operand_1, operand_2, item)
                stack.append(tmp_res)
        assert (len(stack) == 1)
        return stack.pop()

    def _calc_tmp_exp(self, operand_1, operand_2, operator):
        if type(operand_1) is str:
            operand_1 = self._variables[operand_1]
        if type(operand_2) is str:
            operand_2 = self._variables[operand_2]

        return {
            '+': operand_1 + operand_2,
            '-': operand_1 - operand_2,
            '*': operand_1 * operand_2,
            '/': operand_1 / operand_2,
        }[operator]

    @staticmethod
    def _is_digit(item):
        return item.isdigit() or (item[0] == '-' and item[1:].isdigit())

    @staticmethod
    def _is_operand(item):
        return item not in ['+', '-', '*', '/']


if __name__ == '__main__':
    Calculator().run()