#!/usr/bin/python3
"""lockbox solution"""


def canUnlockAll(boxes):
    """check if boxes can be opened
    Args:
        boxes: list
    Returns: boalen
    """

    n = len(boxes)
    if n == 0:
        return False

    opened = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key < n and key not in opened:
                opened.add(key)
                queue.append(key)

    return len(opened) == n
