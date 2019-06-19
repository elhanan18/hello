import unittest


'''
Reverse Polish notation
'''


class RPN:
    def run(self, expression):
        stack = []
        li = expression.split(' ')
        for item in li:
            if item in ['+', '-', '*', '/']:
                assert (len(stack) >= 2)
                operand_2, operand_1 = stack.pop(), stack.pop()
                operator = item
                res = self.calc(operand_1, operand_2, operator)
                stack.append(res)
            else:
                assert (item.isdigit() or (item[0] == "-" and item[1:].isdigit()))
                operand = int(item)
                stack.append(operand)
        return stack.pop() if stack else None

    @staticmethod
    def calc(operand_1, operand_2, operator):
        return {
            '+': operand_1 + operand_2,
            '-': operand_1 - operand_2,
            '*': operand_1 * operand_2,
            '/': operand_1 / operand_2,
        }.get(operator, None)


class TestRPN(unittest.TestCase):

    _samples = [('2 3 +', 5),
                ('3 4 5 * -', -17),
                ('15 7 1 1 + - / 3 * 2 1 1 + + -', 5)]

    def test_rpn(self):
        for expression, result in self._samples:
            self.assertEqual(RPN().run(expression), result, "Result of {} should be: {}".format(expression, result))


if __name__ == '__main__':
    unittest.main()

