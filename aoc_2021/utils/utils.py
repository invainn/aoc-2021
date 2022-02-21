"""
Utilities for AoC problems
"""

import os
import sys
from typing import List


class Utils:
    """
    Utiliy class for AoC problems
    """

    @staticmethod
    def read_int_input(file_name: str = "input") -> List[int]:
        """
        read input from file into list of ints
        """
        result = []
        with open(os.path.join(sys.path[0], file_name), "r", encoding="utf-8") as file:
            for line in file:
                result.append(int(line.strip()))

        return result
