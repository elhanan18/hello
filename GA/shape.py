from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self._prop = {}

    @abstractmethod
    def get(self):
        return self._prop


class ShapeDecorator(Shape):
    def __init__(self, decorated_shape):
        self._decorated_shape = decorated_shape

    def get(self):
        return self._decorated_shape.get()


class Circle(Shape):
    def __init__(self, radius, center):
        self._radius = radius
        self._center = center

    def get(self):
        self._prop["radius"] = self._radius
        self._prop["center"] = self._center
        return self._prop


class ColorDecorator(ShapeDecorator):
    def __init__(self, _decorated_shape, color):
        ShapeDecorator.__init__(_decorated_shape)
        self._color = color

    def get(self):
        self._prop["color"] = self._color
        return self._prop



