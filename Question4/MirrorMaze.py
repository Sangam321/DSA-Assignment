from collections import deque

def min_steps_to_collect_all_keys(maze):
    rows = len(maze)
    cols = len(maze[0])

    target_keys = 0
    start_x, start_y = 0, 0
    # Extract information from the maze
    for i in range(rows):
        for j in range(cols):
            cell = maze[i][j]
            if cell == 'S':
                start_x, start_y = i, j
            elif cell == 'E':
                target_keys |= (1 << (ord('f') - ord('a')))  
            elif 'a' <= cell <= 'f':
                target_keys |= (1 << (ord(cell) - ord('a')))

    #BFS traversal
    queue = deque([(start_x, start_y, 0, 0)]) 

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False] * (1 << 6) for _ in range(cols)] for _ in range(rows)]

    while queue:
        x, y, keys, steps = queue.popleft()

        if keys == target_keys:
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != 'W':
                cell = maze[new_x][new_y]

                if cell == 'E' or cell == 'P' or ('a' <= cell <= 'f') or ('A' <= cell <= 'F' and (keys & (1 << (ord(cell) - ord('A')))) != 0):
                    new_keys = keys
                    if 'a' <= cell:
                        new_keys |= (1 << (ord(cell) - ord('a')))  #Collect the key

                    if not visited[new_x][new_y][new_keys]:
                        visited[new_x][new_y][new_keys] = True
                        queue.append((new_x, new_y, new_keys, steps + 1))

    return -1 

if __name__ == "__main__":
    maze = ["SPaPP", "WWWPW", "bPAPB"]
    result = min_steps_to_collect_all_keys(maze)
    print("Minimum number of moves:", result)
