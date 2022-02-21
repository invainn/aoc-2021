"""
Advent of Code Day 2
"""
import os
import sys
from dataclasses import dataclass
from typing import List
from enum import Enum


class Direction(str, Enum):
    """
    Direction is name of the action taken
    """

    FORWARD = "FORWARD"
    UP = "UP"
    DOWN = "DOWN"


@dataclass(frozen=True)
class Action:
    """
    Action is a direction and the value of that direction
    """

    direction: Direction
    value: int


def read_input(file_name: str) -> List[Action]:
    """
    read input for this problem
    """
    actions = []
    with open(os.path.join(sys.path[0], file_name), "r", encoding="utf-8") as file:
        for line in file:
            raw_string = line.strip()
            direction, value = raw_string.split(" ")

            actions.append(
                Action(direction=Direction(direction.upper()), value=int(value))
            )

    return actions


def find_final_position(actions: List[Action]) -> int:
    """
    finds final position after series of actions
    """
    final_depth = 0
    final_horizontal_position = 0

    aim = 0

    for action in actions:
        if action.direction == Direction.FORWARD:
            final_horizontal_position += action.value
            final_depth += action.value * aim
        if action.direction == Direction.UP:
            aim -= action.value
        if action.direction == Direction.DOWN:
            aim += action.value

    return final_depth * final_horizontal_position
