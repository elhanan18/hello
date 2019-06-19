from abc import ABC, abstractmethod
from image import CircleImage
from random import randint, shuffle


class Gen(ABC):
    def __init__(self):
        self._population = []
        self._size = 100

    @abstractmethod
    def _create(self):
        pass

    def get(self):
        return self._population


class FirstGen(Gen):
    def __init__(self):
        Gen.__init__(self)
        self._create()

    def _create(self):
        for i in range(self._size):
            self._population.append(CircleImage([]))


class NextGen(Gen):
    _gen_num = 0  # static

    def __init__(self, prev_population):
        Gen.__init__(self)
        self._prev_population = prev_population
        self._create()
        self._print_gen_num()

    def _create(self):
        self._selection()
        self._elitism()
        self._add_children()
        assert (len(self._population) == self._size)

    def _add_children(self):
        for _ in range(int(self._size * 0.9)):  # 90%
            child = self._crossover()
            child = self._mutation(child)
            self._population.append(child)

    def _crossover(self):
        min_idx, max_idx = 0, self._size // 2 - 1
        i, j = randint(min_idx, max_idx), randint(min_idx, max_idx)
        parent_1, parent_2 = self._prev_population[i], self._prev_population[j]
        half = len(parent_1.properties) // 2
        child_properties = parent_1.properties[:half] + parent_2.properties[half:]
        # shuffle(child_properties)
        child = CircleImage(child_properties)
        return child

    def _mutation(self, child):
        if randint(0, self._size) < 10:
            for _ in range(4):
                child.replace_property()
            return CircleImage(child.properties)
        return child

    def _selection(self):
        tmp = []
        for item in self._prev_population.get():
            fitness_score = item.calc_fitness()  # evaluation
            tmp.append((fitness_score, item))
        tmp.sort(key=lambda tup: tup[0])
        # print(tmp[0][0])
        self._prev_population = [item[1] for item in tmp[:self._size // 2]]  # 50%

    def _elitism(self):
        self._population.extend(self._prev_population[:self._size // 10])  # 10%

    @staticmethod
    def _print_gen_num():
        NextGen._gen_num += 1
        if NextGen._gen_num % 1000 == 0:
            print("Gen: {}. ".format(NextGen._gen_num))

