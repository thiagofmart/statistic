import numpy as np
import matplotlib.pyplot as plt


def plot_sine():
    fig, ax = plt.subplots(figsize=(8, 3.75))
    ax.plot([np.sin(data/10) for data in range(-20, 100)])
    ax.axhline(y=0)
    ax.axvline(x=20)
    ax.set_ylim(bottom=-1, top=1)
    plt.show()
