from aoc_2021.utils.utils import Utils
from aoc_2021.one.sonar_sweep import find_depth_increases
from aoc_2021.two.dive import read_input
from aoc_2021.two.dive import find_final_position

if __name__ == "__main__":
    day_one_answer = find_depth_increases(Utils.read_int_input("one/input"))
    print(f"day 1 answer - {day_one_answer}")

    day_two_answer = find_final_position(read_input("two/input"))
    print(f"day 2 answer - {day_two_answer}")
