from gen import FirstGen, NextGen
import time


class GA:
    @staticmethod
    def run():
        start = time.time()
        cur_gen = FirstGen()
        for i in range(1000):
            next_gen = NextGen(cur_gen)
            cur_gen = next_gen
        cur_gen.get()[0].save()
        end = time.time()
        print("Time: {} min".format((end - start) / 60))


if __name__ == '__main__':
    GA().run()








