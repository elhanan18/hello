# from enum import Enum
#
#
# class Type(Enum):
#     none = '-'
#     white = 'w'
#     black = 'b'
#
#
# class Board:
#     def __init__(self):
#         self._board = [[Type.none, Type.white, Type.none, Type.white, Type.none, Type.white, Type.none, Type.white],
#                        [Type.white, Type.none, Type.white, Type.none, Type.white, Type.none, Type.white, Type.none],
#                        [Type.none, Type.white, Type.none, Type.white, Type.none, Type.white, Type.none, Type.white],
#                        [Type.none, Type.none, Type.none, Type.none, Type.none, Type.none, Type.none, Type.none],
#                        [Type.none, Type.none, Type.none, Type.none, Type.none, Type.none, Type.none, Type.none],
#                        [Type.black, Type.none, Type.black, Type.none, Type.black, Type.none, Type.black, Type.none],
#                        [Type.none, Type.black, Type.none, Type.black, Type.none, Type.black, Type.none, Type.black],
#                        [Type.black, Type.none, Type.black, Type.none, Type.black, Type.none, Type.black, Type.none]]
#
#     def print(self):
#         print('\n'.join([''.join(['{:4}'.format(item.value) for item in row])
#                          for row in self._board]))
#
#
# class Game:
#     def __init__(self):
#         self._board = Board()
#         self._board.print()
#
#
# Game()
