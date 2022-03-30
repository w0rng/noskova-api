import matplotlib.pyplot as plt
import random


def draw_gant(data: list, name: str, size: int = 1):
    _, gnt = plt.subplots()
    gnt.set_xlabel("Время")
    gnt.set_ylabel("Станки")

    gnt.set_yticks([(i + 1) * 2 for i in range(len(data))])
    gnt.set_yticklabels([str(i + 1) for i in range(len(data))])

    gnt.grid(True)

    for num_part in range(len(data[0])):
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        for machine in range(len(data)):
            gnt.broken_barh([data[machine][num_part]], ((machine + 1) * 2 - size / 2, size), facecolors=color)

    plt.savefig(f"{name}.png")
