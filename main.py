import random


def generate_grid():
    main_grid = [['s','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_','_','_','_']]
    return main_grid


def move(direction, grid):
    if direction not in ['left','l','right','r','up','u','down','d']:
        return grid
    
    elif direction == 'right' or direction == 'r':
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y == 's' and j+1 < len(x):
                    grid[i][j] = '_'
                    print(grid[i][j+1])
                    grid[i][j+1] = 's'
                    return grid
                
    elif direction == 'left' or direction == 'l':
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y == 's' and j-1 < len(x):
                    grid[i][j] = '_'
                    print(grid[i][j-1])
                    grid[i][j-1] = 's'
                    return grid
                
    elif direction == 'up' or direction == 'u':
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y == 's' and i-1 < len(grid):
                    grid[i][j] = '_'
                    print(grid[i-1][j])
                    grid[i-1][j] = 's'
                    return grid


    elif direction == 'down' or direction == 'd':
        for i,x in enumerate(grid):
            for j,y in enumerate(x):
                if y == 's' and i+1 < len(grid):
                    grid[i][j] = '_'
                    print(grid[i+1][j])
                    grid[i+1][j] = 's'
                    return grid
    return grid       


def spawn_food(grid):
    random_pos = (random.randint(1,9), random.randint(1,9))
    grid[random_pos[0]][random_pos[1]] = 'f'

    return grid

main_grid = spawn_food(generate_grid())

for i in main_grid:
    print(i)

# Main loop
while True:

    direction = input()
    if direction.lower() == 'q':
        break
    else:
        grid = move(direction.lower(), main_grid)
        for i in grid:
            print(i)


