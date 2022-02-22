from aoc_2021.utils.utils import Utils
from aoc_2021.one.sonar_sweep import find_depth_increases
from aoc_2021.two.dive import read_input
from aoc_2021.two.dive import find_final_position
from aoc_2021.three.binary_diag import calculate_power_consumption
from aoc_2021.three.binary_diag import calculate_life_support_rating
from aoc_2021.three.binary_diag import read_binary_input

if __name__ == "__main__":
    day_one_answer = find_depth_increases(Utils.read_int_input("one/input"))
    print(f"day 1 answer - {day_one_answer}")

    day_two_answer = find_final_position(read_input("two/input"))
    print(f"day 2 part 2 answer - {day_two_answer}")

    day_three_answer = calculate_power_consumption(read_binary_input())
    print(f"day 3 part 1 answer - {day_three_answer}")

    day_three_answer = calculate_life_support_rating(read_binary_input())
    print(f"day 3 part 2 answer - {day_three_answer}")
