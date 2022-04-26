import matplotlib.pyplot as plt
import random
from typing import List
from copy import deepcopy


Matrix = List[List[int]]


def calc_start_time(data: Matrix) -> Matrix:
    copy_data = deepcopy(data)

    for i in range(1, len(data[0])):
        copy_data[0][i] += copy_data[0][i - 1]

    for i in range(1, len(data)):
        copy_data[i][0] += copy_data[i - 1][0]

    for i in range(1, len(data)):
        for j in range(1, len(data[0])):
            copy_data[i][j] += max(copy_data[i - 1][j], copy_data[i][j - 1])

    return copy_data


def calc_start_and_end_data(data: Matrix, data_with_start: Matrix) -> Matrix:
    result = data_with_start.copy()

    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] = (result[i][j] - data[i][j], data[i][j])

    return result


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
            gnt.broken_barh(
                [data[machine][num_part]],
                ((machine + 1) * 2 - size / 2, size),
                facecolors=color,
                label=f"Деталь {num_part+1}" if machine == 0 else None,
            )

    plt.legend(bbox_to_anchor=(1, 0.25))
    plt.savefig(f"{name}.png")


def calc_lines(data: List[List[int]], order: List[int]):
    new_data = []
    for i in order:
        new_data.append(data[i])

    gantt = [[sum(data[order[0]][:i]) for i in range(1, len(order) + 1)]]
    for machine in order[1:]:
        gantt.append([data[machine][i] + gantt[-1][i] for i in range(len(order))])

    gantt_with_line = []
    for machine in range(len(data)):
        gantt_with_line.append(
            [(gantt[machine][i] - new_data[machine][i], new_data[machine][i]) for i in range(len(order))]
        )

    return gantt_with_line
