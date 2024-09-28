#!/usr/bin/python3
"""calculating total amount of rainwater kept after it rains"""


def rain(walls):
    """
    Assumption:
    The ends of the list  are not walls,
    meaning they will not retain water.
    """

    # checking if input list is empy
    if not walls:
        return 0

    # Initialise two pointers for both ends of list & tracking max heights
    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_retained = 0

    # Balancing their heights before they reach same level.
    while left < right:
        if left_max < right_max:
            left += 1

            # Update left_max if other wall taller
            left_max = max(left_max, walls[left])

            # Calculate water retained above current wall
            water_retained += left_max - walls[left]
        else:
            # Move the right pointer towards the left
            right -= 1
            right_max = max(right_max, walls[right])
            # Calculate the water retained above the current wall
            water_retained += right_max - walls[right]

    return water_retained


if __name__ == "__main__":
    # Uses algorithm above to actually calculate example
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))
