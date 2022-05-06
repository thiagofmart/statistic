import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


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

def construct_population_distribution():
    population = Population(size=100000)
    fig, ax = plt.subplots(figsize=(8, 3.75))
    x = np.array(range(population.values.min(), population.values.max()+1))
    y = [(population.values==data).sum() for data in x]
    ax.set_ylabel("Counts")
    ax.set_ylabel("Data")
    ax.set_title(f'Population Distribution\nN = {population.values.size}, mean = {population.values.mean()}, variance = {population.get_variance()}')
    ax.bar(x, y)
    plt.show()

def compare_sample_variance_biased_x_unbiased(percentage=False):
    population = Population(size=100000)
    real_variance = population.get_variance()
    lst_biased = []
    lst_unbiased = []
    for i in range(100):
        sample = Sample(population, 10)
        lst_biased.append(sample.get_biased_variance())
        lst_unbiased.append(sample.get_unbiased_variance())

    real_variance, lst_biased, lst_unbiased = real_variance, np.array(lst_biased), np.array(lst_unbiased)
    if percentage==True:
        real_variance, lst_biased, lst_unbiased = 1, lst_biased/real_variance, lst_unbiased/real_variance

    fig, ax = plt.subplots(figsize=(8, 3.75))
    ax.set_ylabel("variance")
    ax.plot(range(1,lst_biased.size+1), lst_biased, label='biased')
    ax.plot(range(1,lst_unbiased.size+1), lst_unbiased, label='unbiased')
    ax.axhline(y=real_variance, label='real', color='r')
    ax.set_ylim(bottom=real_variance*0, top=real_variance*2)
    ax.legend()
    ax.set_title(f'Var: {real_variance}, Biased: {lst_biased.mean()}, Unbiased: {lst_unbiased.mean()}')
    plt.show()


def test():
    construct_population_distribution() # SHOW THE POPULATION DISTRIBUTION
    compare_sample_variance_biased_x_unbiased(percentage=True) # COMPARISON OF SAMPLE VARIANCE 
