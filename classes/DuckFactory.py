import random

from classes.Duck import Duck


class DuckFactory:

    @staticmethod
    def generate():
        return Duck(bool(random.getrandbits(1)))
