
"""Pascal Triangle Problem"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Each row 1st element is always 1
        if i > 0:
            prev_row = triangle[i - 1]

            for h in range(1, i):
                row.append(prev_row[h - 1] + prev_row[h])
            row.append(1)  # Each row end element is always 1
        triangle.append(row)
    return triangle  # Once sequence is done triangle is wholly returned


def triangle(triangle):
    """Prints the triangle"""
    for row in triangle:
        # formats each row to make triangular shape
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    triangle(pascal_triangle(10))
