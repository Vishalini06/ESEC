from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

queue, fresh = deque(), sum(row.count(1) for row in grid)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i, j, 0))

directions, time = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0

while queue:
    x, y, t = queue.popleft()
    time = max(time, t)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
            grid[nx][ny] = 2
            fresh -= 1
            queue.append((nx, ny, t + 1))

print(f"All oranges can become rotten in {time} time frames." if fresh == 0 else "All oranges cannot rot")
