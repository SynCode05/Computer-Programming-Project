# # import pygame
# # pygame.init()

# # Creates the class called CreateGrid
class CreateGrid():
    """This class creates a grid of dimentions (x,y)."""
    def __init__(self, x_size: int, y_size: int) -> None:
        self.x_size = x_size
        self.y_size = y_size 

        # Automatically runs the function createBoard()
        self.create_board()

    def create_board(self) -> None:
        """To create a co-ordinate system of (x,y) dimentions"""
        self.grid = [[0 for x in range(self.x_size)] for y in range(self.y_size)]
        return


    def switch(self, x, y) -> None:
        """Switches a cell from dead to alive and vise versa."""
        self.grid[y][x] = 0 if self.grid[y][x] >= 1 else 1
    
    def off_board(self, x: int, y: int) -> object:
        """Returns the items that need to be checked."""
        top = ["TL", "TC", "TR"]
        bottom = ["BL", "BC", "BR"]
        left = ["TL", "CL", "BL"]
        right = ["TR", "CR", "BR"]
        cells_to_check = {"TL", "TC", "TR", "CL", "CR", "BL", "BC", "BR"}
        if y == 0: 
            for i in range(3): cells_to_check.discard(top[i])
        if y == self.y_size - 1: 
            for i in range(3): cells_to_check.discard(bottom[i])
        if x == 0: 
            for i in range(3): cells_to_check.discard(left[i])
        if x == self.x_size - 1: 
            for i in range(3): cells_to_check.discard(right[i])
        return cells_to_check


    def check_neighbors(self, x: int, y: int) -> int:
        cells_to_check = self.off_board(x, y)
        live_neighbour_count = 0 
        for cell in cells_to_check:
            if cell == "TL" and self.grid[y-1][x-1]:
                live_neighbour_count += 1
            elif cell == "TC" and self.grid[y-1][x]:
                live_neighbour_count += 1
            elif cell == "TR" and self.grid[y-1][x+1]:
                live_neighbour_count += 1
            elif cell == "CL" and self.grid[y][x-1]:
                live_neighbour_count += 1
            elif cell == "CR" and self.grid[y][x+1]:
                live_neighbour_count += 1
            elif cell == "BL" and self.grid[y+1][x-1]:
                live_neighbour_count += 1
            elif cell == "BC" and self.grid[y+1][x]:
                live_neighbour_count += 1
            elif cell == "BR" and self.grid[y+1][x+1]:
                live_neighbour_count += 1
        return live_neighbour_count

    def next_population(self) -> None: 
        """Returns the matrix of the next population."""
        to_update = []
        for y in range(self.y_size):
            for x in range(self.x_size):
                alive = self.grid[y][x]
                neighbours = self.check_neighbors(x, y)

    #         # Line to return important information
    #         print(f"x: {x}, y: {y}, N: {neighbours}")  
                
    #         # Line to return important information
    #         print(f"Alive: {alive}\nLess than 2 neighbours: {neighbours < 2}\nMore than 3 neighbours: {neighbours > 3}\nNeighbour number: {self.grid[y][x]}\n") 

                if alive:
                    if neighbours < 2 or neighbours > 3:
                        to_update.append((x, y))
                else:
                    if neighbours == 3:
                        to_update.append((x, y))
        self.update_grid(to_update)
        return self.grid

    def update_grid(self, to_update: list) -> None: 
        for x, y in to_update: self.switch(x, y)
        return
            
    
    def check_alive(self, x: int, y: int) -> bool:
       return self.grid[y][x] >= 1