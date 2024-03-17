# Creates the class called CreateGrid
class CreateGrid():
    """This class creates a grid of dimentions (x,y)."""
    def __init__(self, x_size: int, y_size: int, *dlc) -> None:
        self.x_size, self.y_size, self.dlc, self.grid =  x_size, y_size, dlc, []

        # Automatically runs the function createBoard()
        self.create_board()

    def create_board(self) -> None:
        """To create a co-ordinate system of (x,y) dimentions"""
        self.grid = [[0 for x in range(self.x_size)] for y in range(self.y_size)]
        return


    def switch(self, x: int, y: int) -> None:
        """Switches a cell from dead to alive and vise versa."""
        self.grid[y][x] = 1
    
    def count_alive_neighbours(self, x: int, y: int) -> int:
        """Returns the numer of alive cells."""  
        count = 0
        
        for dy in [-1, 0, 1]: # Range of rows
            for dx in [-1, 0, 1]: # Range of columns

                if dx == 0 and dy == 0: continue  # Skip current cell
                nx, ny = x + dx, y + dy # New x and y co-ordiantes
                if 0 <= nx < self.x_size and 0 <= ny < self.y_size: # Checks to make sure it isn't reading the grid at the index [-1].
                    count += self.grid[ny][nx] #  Adds value of neighbouring cells.
        return count

    
    def update_grid(self) -> None: 
        """Updates the grid automatically"""
        new_grid = [[0 for x in range(self.x_size)] for y in range(self.y_size)]
           
        for y in range(self.y_size):
            for x in range(self.x_size):

                alive_neighbours = self.count_alive_neighbours(x, y)
                
                if self.grid[y][x] == 1: 
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        new_grid[y][x] = 0  # Cell dies due to underpopulation or overpopulation
                    else:
                        new_grid[y][x] = 1  # Cell survives
                
                else:
                    if alive_neighbours == 3:
                        new_grid[y][x] = 1  # Cell becomes alive due to reproduction
        
        self.grid = new_grid