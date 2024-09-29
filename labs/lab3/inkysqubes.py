def count_squares(L, R):
    count = 0
    k = 1
    while k * k <= R:
        if k * k >= L:
            count += 1
        k += 1
    return count


def count_cubes(L, R):
    count = 0
    k = 1
    while k * k * k <= R:
        if k * k * k >= L:
            count += 1
        k += 1
    return count


def count_squbes(L, R):
    count = 0
    k = 1
    while k ** 6 <= R:
        if k ** 6 >= L:
            count += 1
        k += 1
    return count


# Read input
L, R = map(int, input().strip().split())

# Calculate counts
num_squares = count_squares(L, R)
num_cubes = count_cubes(L, R)
num_squbes = count_squbes(L, R)

print(num_squares, num_cubes, num_squbes)
