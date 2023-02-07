import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    # """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N,N)

def decimal_to_quaternary(num, n):
    list = np.zeros(n)
    for x in range(n):
        list[x] = num//4**(n-x-1)
        num = num%4**(n-x-1)
    return(list)


CArule = [decimal_to_quaternary(i,9) for i in range(4**8)]

def update(grid, N, rule):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)

            # apply Conway's rules
            if CArule[rule][total] == 3:
                newGrid[i,j] = 255 - grid(i,j)
            if CArule[rule][total] == 1:
                newGrid[i,j] = 255
            if CArule[rule][total] == 0:
                newGrid[i,j] = 0

    # update data
    grid[:] = newGrid[:]

Grid1 = randomGrid(10)
states1 = np.zeros(10)
for x in range(10):
    states1[x] = Grid1
    update(x, Grid1, )