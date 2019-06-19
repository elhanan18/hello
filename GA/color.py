from abc import ABC, abstractmethod
from random import randint


class Color(ABC):
    def __init__(self, color=None):
        self._color = color

    @property
    def color(self):
        return self._color


class RandomColor(Color):
    def __init__(self):
        b, g, r = randint(0, 255), randint(0, 255), randint(0, 255)
        self._color = b, g, r
