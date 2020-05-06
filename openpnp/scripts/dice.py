import random


class Dice:
    """
    Dice(n) represents a n-sided dice
    To throw the dice, call it.

    A dice obj implements the following operators:
    (+) Throw the dice and add a value
    (-) Throw the dice and subtract a value
    (*) Throw the dice "value-times" and sum the results

    Example of use:
    > d6 = Dice(6) # Define dice
    > 6 * d6 + 1   # Throw dice 6 times and add 1
    """

    __slots__ = ["n"]

    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Dice({self.n})"

    def __call__(self):
        return random.randint(1, self.n)

    def __add__(self, value):
        return self() + value

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        return self() - value

    def __rsub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        return sum([self() for i in range(value)])

    def __rmul__(self, value):
        return self.__mul__(value)


d4   = Dice(4)
d6   = Dice(6)
d8   = Dice(8)
d10  = Dice(10)
d12  = Dice(12)
d20  = Dice(20)
d100 = Dice(100)


def gaussint(lower, upper, sigma=1, radius=3):
    """
    Like random.randint but with a normal distribution

    Use random.gauss with ´sigma´ to get a random value on the x-axis.
    The ´radius´ then defines the x-axis' portion
    which will be mapped to the desired range.
    If the value falls outside this portion,
    it will be replaced by a new one.
    """
    value = random.gauss(radius, sigma)
    while value < 0 or value > 2*radius:
        value = random.gauss(sigma, radius)
        # Uncomment for checking likeliness of reroll
        # print("reroll")

    step = 2*radius/(upper - lower + 1)
    return lower + int(value // step)


class GaussDice(Dice):
    """
    A GaussDice is Dice with a normal distribution.

    See Dice for more information
    """

    def __init__(self, n, sigma=1):
        self.n = n
        self.sigma = sigma

    def __call__(self):
        return gaussint(1, n)


gd4   = GaussDice(4)
gd6   = GaussDice(6)
gd8   = GaussDice(8)
gd10  = GaussDice(10)
gd12  = GaussDice(12)
gd20  = GaussDice(20)
gd100 = GaussDice(100)


def test(func, prob_size=1000, lower=0, upper=10):
    """
    Shitty function for testing randint's distribution

    Call random.randint-like ´func´ ´prob_size´-times
    and count the result.
    """
    list = [0 for i in range(lower, upper+1)]
    for i in range(prob_size):
        list[func(lower, upper)-lower] += 1
    return list

