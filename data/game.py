def create_board(data: set) -> list[list[int]]:
    """To create a co-ordinate system of (x,y) dimentions"""
    grid = [[0 for x in range(data["x_size"])] for y in range(data["y_size"])]
    return grid


def switch(grid: list[list[int]], x: int, y: int) -> None:
    """Switches a cell from dead to alive and vise versa."""
    if grid[y][x] >= 1:
        grid[y][x] = 0
    else:
        grid[y][x] = 1

def count_alive_neighbours(grid: list[list[int]], data: set, x: int, y: int) -> int:
    """Returns the numer of alive cells."""  
    count = 0
        
    for dy in [-1, 0, 1]: # Range of rows
        for dx in [-1, 0, 1]: # Range of columns

            if dx == 0 and dy == 0: continue  # Skip current cell
            nx, ny = x + dx, y + dy # New x and y co-ordiantes
            if 0 <= nx < data["x_size"] and 0 <= ny < data["y_size"]: # Checks to make sure it isn't reading the grid at the index [-1].
                if grid[ny][nx] >= 1:
                    count +=1 #  Adds value of neighbouring cells.
    return count

def update_grid(grid: list[list[int]], data: set) -> list[list[int]]: 
    """Updates the grid automatically"""

    # __import__("time").sleep(delay)

    new_grid = [[0 for x in range(data["x_size"])] for y in range(data["y_size"])]
           
    for y in range(data["y_size"]):
        for x in range(data["x_size"]):

            alive_neighbours = count_alive_neighbours(grid, data, x, y)
            if grid[y][x] >= 1: 
                if alive_neighbours < 2 or alive_neighbours > 3:
                    new_grid[y][x] = 0  # Cell dies due to underpopulation or overpopulation
                else:
                    new_grid[y][x] += 1  # Cell survives
                
            else:
                if alive_neighbours == 3:
                    new_grid[y][x] = 1  # Cell becomes alive due to reproduction
    
    grid = combine_grids(grid, new_grid, data)  
    return grid

def combine_grids(grid: list[list[int]], new_grid: list[list[int]], data: set):
    for y in range(data["y_size"]):
        for x in range(data["x_size"]):
            if new_grid[y][x] == 1: grid[y][x] += 1
            else: grid[y][x] = 0
    return grid
      

def print_grid(grid: list[list[int]]) -> None: 
    """Information on the grid."""
    for row in grid:
        print(" ".join(["⬜" if cell else "⬛" for cell in row]))
