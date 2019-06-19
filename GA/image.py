from abc import ABC, abstractmethod
import numpy as np
import cv2
from color import RandomColor
from random import randint


class Image(ABC):
    _orig_img_path = "sample_2.jpeg"  # 100x100
    _orig_img = cv2.imread(_orig_img_path)

    def __init__(self, properties, num_of_shapes=100):
        self._properties = properties
        self._num_of_shapes = num_of_shapes
        height, width = 100, 100
        self._img = np.zeros((height, width, 3), np.uint8)

    @property
    def properties(self):
        return self._properties

    @abstractmethod
    def _draw(self):
        pass

    @abstractmethod
    def replace_property(self):
        pass

    def save(self):
        cv2.imwrite("output.jpg", self._img)

    def calc_fitness(self):
        # score = 0 when 2 image sre identical
        difference = cv2.subtract(self._orig_img, self._img)
        b, g, r = cv2.split(difference)
        score = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
        return score


class CircleImage(Image):

    def __init__(self, properties):
        Image.__init__(self, properties)
        if not self._properties:
            for _ in range(self._num_of_shapes):
                self._append_rand_property()

        self._draw()

    def _draw(self):
        for item in self._properties:
            color, radius, x, y = item[0], item[1], item[2], item[3]
            # cv2.circle(img, center, radius, color, thickness=1, lineType=8, shift=0) → None
            cv2.circle(self._img, (x, y), radius, color, -1)

    def _append_rand_property(self):
        color = RandomColor().color
        radius = randint(1, 20)
        x = randint(0, 100)
        y = randint(0, 100)
        self._properties.append((color, radius, x, y))

    def replace_property(self):
        idx = randint(0, self._num_of_shapes - 1)
        del self._properties[idx]
        self._append_rand_property()
