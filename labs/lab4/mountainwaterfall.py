def simulate_waterfall(grid, R, C):
    from collections import deque

    # Turn grid into a mutable list of lists
    result = [list(row) for row in grid]

    # Initialize water sources queue
    queue = deque()

    # Find all initial water sources and enqueue them
    for row in range(R):
        for col in range(C):
            if grid[row][col] == '*':
                queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        # Flow down
        while row + 1 < R and result[row + 1][col] == '.':
            result[row + 1][col] = '*'
            row += 1

        # Check if it hits a rock and splits
        if row + 1 < R and result[row + 1][col] == 'o':
            # Flow left
            left_row, left_col = row, col
            while left_col - 1 > 0 and result[left_row][left_col - 1] == '.':
                if result[left_row + 1][left_col - 1] == '.':
                    break
                result[left_row][left_col - 1] = '*'
                queue.append((left_row, left_col - 1))
                left_col -= 1

            # Flow right
            right_row, right_col = row, col
            while right_col + 1 < C - 1 and result[right_row][right_col + 1] == '.':
                if result[right_row + 1][right_col + 1] == '.':
                    break
                result[right_row][right_col + 1] = '*'
                queue.append((right_row, right_col + 1))
                right_col += 1

    return result


# Read input
R, C = map(int, input().strip().split())
grid = [input().strip() for _ in range(R)]

# Simulate the water flows and capture the result
result_grid = simulate_waterfall(grid, R, C)

# Print the resulting grid
for row in result_grid:
    print(''.join(row))
