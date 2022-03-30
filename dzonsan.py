"""Алгоритм джонсана"""

from gantt import draw_gant
from uuid import uuid4
from typing import Dict, List, Any


def dzonsan(data: List) -> Dict[str, Any]:
    """Сначала детали требуюющие мин времени обработки на первом станке в порядке возрастания"""
    parts = list(enumerate(data[1]))
    num_parts_for_first_machine = [i[0] for i in sorted(parts, key=lambda x: x[1])]

    """Детали требующие макс времени на последнем станке в порядке убывания"""
    last_machine = list(enumerate(data[-1]))
    num_parts_for_last_machine = [i[0] for i in sorted(last_machine, key=lambda x: x[1], reverse=True)]

    """Ищем максимальную деталь. Станок с ней сортируем в порядке убывания"""
    max_part = max([max(i) for i in data])
    num_parts_with_max_parts = []
    for i, machine in enumerate(data):
        if max_part not in machine:
            continue
        max_machine = list(enumerate(data[i]))
        num_parts_with_max_parts = [i[0] for i in sorted(max_machine, key=lambda x: x[1], reverse=True)]

    """Считаем суммы обработки деталей на станках и сортируем в обратном порядке"""
    sum_parts = []
    for part in range(len(data[0])):
        sum_parts.append((part, sum([machine[part] for machine in data])))
    num_parts_on_sum = [i[0] for i in sorted(sum_parts, key=lambda x: x[1], reverse=True)]

    result = []
    for i in range(len(data[0])):
        result.append(
            (
                i,
                num_parts_for_first_machine[i]
                + num_parts_for_last_machine[i]
                + num_parts_with_max_parts[i]
                + num_parts_on_sum[i],
            ),
        )

    result = [i[0] for i in sorted(result, key=lambda x: x[1])]

    gantt = [[sum(data[result[0]][:i]) for i in range(1, len(result) + 1)]]
    for machine in result[1:]:
        gantt.append([data[machine][i] + gantt[-1][i] for i in range(len(result))])

    new_data = []
    for i in result:
        new_data.append(data[i])

    gantt_with_line = []
    for machine in range(len(data)):
        gantt_with_line.append(
            [(gantt[machine][i] - new_data[machine][i], new_data[machine][i]) for i in range(len(result))]
        )

    name = str(uuid4())
    draw_gant(gantt_with_line, name)
    return {
        "result": result,
        "image": name,
    }


"""
Сначала пишем зачем это надо
В каких продуктах это необходимо, в каких решениях это применяется
Показываем что у нас в качестве ТЗ методы ограниченного перебора, их плюсы и минусы
Диаграмма последовательсноти (от программиста к программисту) какие функции и перменные, что с чем взаимодействкет
Расипсать про API
"""
