H, W, N = map(int, input().split())
grid = [[0]*W for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y, d = 0, 0, 0

for _ in range(N):
    grid[x][y] ^= 1
    d = (d + 1 - 2*grid[x][y]) % 4
    x = (x + dx[d]) % H
    y = (y + dy[d]) % W

for row in grid:
    print(''.join('#' if cell else '.' for cell in row))
