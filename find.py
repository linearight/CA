import copy

import numpy as np
import matplotlib.pyplot as plt
ON = 255
OFF = 0
vals = [ON, OFF]

def decimal_to_quaternary(num, n):
    list = np.zeros(n)
    for x in range(n):
        list[n-1-x] = num//4**(n-x-1)
        num = num%4**(n-x-1)
    return(list)

CArule = [decimal_to_quaternary(i,9) for i in range(4**9)]

def randomGrid(N, p):
    return np.random.choice(vals, N * N, p=[p, 1-p]).reshape(N,N)


def update(grid, rule):
    n = len(grid)
    grid_b = np.zeros((n + 2) * (n + 2)).reshape((n + 2), (n + 2))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grid_b[i, j] = grid[i - 1, j - 1]
    newGrid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = int((grid_b[i, j] + grid_b[i, j + 1] + grid_b[i, j + 2] +
                            grid_b[i + 2, j] + grid_b[i + 2, j + 1] + grid_b[i + 2, j + 2] +
                            grid_b[i + 1, j] + grid_b[i + 1, j + 2]) / 255)
            if CArule[rule][total] == 3:
                newGrid[i,j] = 255 - grid[i,j]
            if CArule[rule][total] == 1:
                newGrid[i,j] = 255
            if CArule[rule][total] == 0:
                newGrid[i,j] = 0
    grid[:] = newGrid[:]

def updatelife(grid):
    n = len(grid)
    grid_b = np.zeros((n + 2) * (n + 2)).reshape((n + 2), (n + 2))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grid_b[i, j] = grid[i - 1, j - 1]
    newGrid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = int((grid_b[i, j] + grid_b[i, j + 1] + grid_b[i, j + 2] +
                         grid_b[i + 2, j] + grid_b[i + 2, j + 1] + grid_b[i + 2, j + 2] +
                         grid_b[i + 1, j] + grid_b[i + 1, j + 2]) / 255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    grid[:] = newGrid[:]

def compare_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

grid = randomGrid(10,0.5)
grid1 = copy.deepcopy(grid)
update(grid1, 45)
for x in range(512):
    grid2 = copy.deepcopy(grid)
    update(grid2, x)
    if compare_matrices(grid1, grid2) == True:
        print(x)

