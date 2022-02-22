import os
import sys
from collections import defaultdict
from typing import List
from typing import Callable


def read_binary_input(file_name: str = "three/input") -> List[str]:
    """
    read input from file into list of ints
    """
    result = []
    with open(os.path.join(sys.path[0], file_name), "r", encoding="utf-8") as file:
        for line in file:
            result.append(line.strip())

    return result


def calculate_power_consumption(report: List[str]) -> int:
    counts = defaultdict(int)

    for binary_number in report:
        for index, bit in enumerate(binary_number):
            if bit == "1":
                counts[index] += 1
            else:
                counts[index] -= 1

    most_common_bits_in_pos = []
    for count in counts.values():
        if count < 0:
            most_common_bits_in_pos.append("0")
        else:
            most_common_bits_in_pos.append("1")

    least_common_bits_in_pos = []
    for bit in most_common_bits_in_pos:
        if bit == "1":
            least_common_bits_in_pos.append("0")
        else:
            least_common_bits_in_pos.append("1")

    gamma_rate = int("".join(most_common_bits_in_pos), base=2)
    epsilon_rate = int("".join(least_common_bits_in_pos), base=2)

    return gamma_rate * epsilon_rate


def _find_ratings(report: List[str], comparison_func: Callable[[int], int]) -> str:
    new_elimination_list = report
    elimination_list = new_elimination_list

    current_index = 0
    while len(elimination_list) > 1:
        new_elimination_list = []
        count = 0

        for binary_number in elimination_list:
            if binary_number[current_index] == "1":
                count += 1
            else:
                count -= 1

        criteria_bit = comparison_func(count)

        for binary_number in elimination_list:
            if int(binary_number[current_index]) == criteria_bit:
                new_elimination_list.append(binary_number)

        elimination_list = new_elimination_list
        current_index += 1

    return elimination_list[0]


def calculate_life_support_rating(report: List[str]) -> int:
    oxygen_generator_rating = int(
        _find_ratings(report, lambda count: count >= 0), base=2
    )
    co2_scrubber_rating = int(_find_ratings(report, lambda count: count < 0), base=2)

    return oxygen_generator_rating * co2_scrubber_rating
