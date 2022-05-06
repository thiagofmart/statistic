import numpy as np


class Population():
    def __init__(self, size):
        self.values = np.random.randint(0, 99, size=size)
    def get_variance(self):
        x=0
        for n in self.values:
            x+=((n-self.values.mean()))**2
        return x/self.values.size


class Sample():
    def __init__(self, population, size):
        self.values = np.random.choice(population.values, size=size)
    def get_biased_variance(self):
        x=0
        for n in self.values:
            x+=((n-self.values.mean()))**2
        return x/self.values.size
    def get_unbiased_variance(self):
        x=0
        for n in self.values:
            x+=((n-self.values.mean()))**2
        return x/(self.values.size-1)

def test():
    """
    real_variance, lst_biased, lst_unbiased = test()
    """
    population = Population(size=10000)
    real_variance = population.get_variance()
    lst_biased = []
    lst_unbiased = []
    for i in range(10):
        sample = Sample(population, 150)
        lst_biased.append(sample.get_biased_variance())
        lst_unbiased.append(sample.get_unbiased_variance())
    return real_variance, np.array(lst_biased), np.array(lst_unbiased)
