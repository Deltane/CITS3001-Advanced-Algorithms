from collections import deque


def go_stone_puzzle(N, S, T):
    # Check if transformation is possible by comparing counts of 'W' and 'B'
    if sorted(S) != sorted(T):
        return -1

    # Initialize BFS queue and visited set
    initial_state = S + ".."  # Add two empty cells to the initial state
    target_state = T + ".."  # Add two empty cells to the target state
    queue = deque([(initial_state, 0)])
    visited = set([initial_state])

    while queue:
        current_state, move_count = queue.popleft()

        if current_state == target_state:
            return move_count

        # Find the positions of the two empty cells ('.') in the current state
        empty_indices = [i for i, c in enumerate(current_state) if c == '.']

        if len(empty_indices) != 2:
            continue

        k, k_plus_1 = empty_indices

        # Try all possible moves of two adjacent stones into the empty cells
        for x in range(N + 1):
            if current_state[x] != '.' and current_state[x + 1] != '.':
                # Perform the move
                new_state = list(current_state)
                new_state[k], new_state[k_plus_1] = new_state[x], new_state[x + 1]
                new_state[x], new_state[x + 1] = '.', '.'
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, move_count + 1))

    return -1  # If the target state is not reachable


# Read input
N = int(input().strip())
S = input().strip()
T = input().strip()

# Get the result
result = go_stone_puzzle(N, S, T)
print(result)
