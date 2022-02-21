"""
Advent of Code Day 1
"""
from typing import List


def find_depth_increases(sonar_sweep: List[int]) -> int:
    """
    Find amount of depth increases in a list of sweeps
    """
    depth_increases = 0

    for idx in range(len(sonar_sweep) - 1):
        if sonar_sweep[idx + 1] > sonar_sweep[idx]:
            depth_increases += 1

    return depth_increases
