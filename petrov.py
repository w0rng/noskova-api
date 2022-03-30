from typing import List
from uuid import uuid4
from utils import draw_gant
from utils import calc_start_time, calc_start_and_end_data

Matrix = List[List[int]]


def calc_sum_without_line(data: Matrix, num_line: int):
    result = [0] * len(data[0])
    for i, row in enumerate(data):
        if i == num_line:
            continue
        for j, element in enumerate(row):
            result[j] += element

    return result


def sort_data_on_sum(data: Matrix, summ: List[int]):
    summ = [(i, e) for i, e in enumerate(summ)]
    summ.sort(key=lambda x: x[1])

    new_data = []
    for row in data:
        tmp_row = []
        for i, _ in summ:
            tmp_row.append(row[i])
        new_data.append(tmp_row)

    return new_data, [i for i, _ in summ]


def petrov(data: Matrix):
    sum_1 = calc_sum_without_line(data, 0)
    sum_2 = calc_sum_without_line(data, len(data) - 1)
    difference_sum = [sum_2[i] - sum_1[i] for i in range(len(sum_1))]

    data_via_sum_1, ordered = sort_data_on_sum(data, sum_1)
    data_via_sum_2, ordered = sort_data_on_sum(data, sum_2)
    data_via_sum_difference, ordered = sort_data_on_sum(data, difference_sum)

    data_start_time_sum_1 = calc_start_time(data_via_sum_1)
    data_start_time_sum_2 = calc_start_time(data_via_sum_2)
    data_start_time_difference = calc_start_time(data_via_sum_difference)

    if (
        data_start_time_sum_1[-1][-1] <= data_start_time_sum_2[-1][-1]
        and data_start_time_sum_1[-1][-1] <= data_start_time_difference[-1][-1]
    ):
        data, _ = sort_data_on_sum(data, sum_1)
        result = calc_start_and_end_data(data, data_start_time_sum_1)
    elif (
        data_start_time_sum_2[-1][-1] <= data_start_time_sum_1[-1][-1]
        and data_start_time_sum_2[-1][-1] <= data_start_time_difference[-1][-1]
    ):
        data, _ = sort_data_on_sum(data, sum_2)
        result = calc_start_and_end_data(data, data_start_time_sum_2)
    else:
        data, _ = sort_data_on_sum(data, difference_sum)
        result = calc_start_and_end_data(data, data_start_time_difference)

    name = str(uuid4())
    draw_gant(result, name)

    return {
        "result": ordered,
        "matrix_with_line": result,
        "image": name,
    }


if __name__ == "__main__":
    data = [
        [1, 2, 3],
        [3, 2, 4],
        [5, 8, 9],
    ]
