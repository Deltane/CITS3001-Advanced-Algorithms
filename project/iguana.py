from collections import deque

def readInput():
    import sys
    input_lines = sys.stdin.readlines()
    size = int(input_lines[0])
    maze = []
    idx = 1
    while len(maze) < size:
        line = input_lines[idx].strip()
        if line != '':
            maze.append(line)
        idx += 1
    return size, maze

def startQueue(queue, start_position, maze):
    if maze[start_position[0]][start_position[1]] == '.':
        queue.append((start_position[0], start_position[1], None, 0))

def runQueue(queue, maze, size):
    if not queue:
        return -1
    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    visited_instr = [[float('inf')] * size for _ in range(size)]
    visited_instr[0][0] = 0
    while queue:
        row, col, prev_direction, instr = queue.popleft()
        if (row, col) == (size - 1, size - 1):
            return instr
        for d in directions:
            dr, dc = directions[d]
            new_instr = instr + 1 if prev_direction != d else instr
            new_row, new_col = row, col
            while True:
                next_row = new_row + dr
                next_col = new_col + dc
                if checkMoves(next_row, next_col, size, maze):
                    new_row, new_col = next_row, next_col
                    if visited_instr[new_row][new_col] > new_instr:
                        visited_instr[new_row][new_col] = new_instr
                        queue.append((new_row, new_col, d, new_instr))
                else:
                    break
    return -1

def checkMoves(row, col, size, maze):
    return 0 <= row < size and 0 <= col < size and maze[row][col] == '.'

def main():
    size, maze = readInput()
    queue = deque()
    if maze[0][0] == '#' or maze[size - 1][size - 1] == '#':
        print(-1)
        return
    startQueue(queue, (0, 0), maze)
    result = runQueue(queue, maze, size)
    print(result)

if __name__ == '__main__':
    main()
