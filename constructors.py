class CreateGrid():
    """This class creates a grid of dimentions (x,y)."""
    def __init__(self, x_size: int, y_size: int) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.createBoard()

    def createBoard(self):
        GridMatrix = []
        for y in range(self.y_size):
            GridMatrix.append([])
            for x in range(self.x_size):
                GridMatrix[y].append(0)
        self.grid = GridMatrix
        return GridMatrix
    
    def switch(self, x, y):
        self.grid[x][y] = 1 if self.grid[x][y] == 0 else 0