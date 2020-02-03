#Question4- grid

#pseudo- 1. take the number of rows. 2. take the number of columns. 3. work with row index and column index to fill the grid


grid = []
for i in range(0,5):
    grid.append([])
    for j in range(0,6):
        grid[i].append(i+j*5)
for element in grid:
    print (element)

