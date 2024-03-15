# import pygame
# pygame.init()

# Creates the class called CreateGrid
class CreateGrid():
    """This class creates a grid of dimentions (x,y)."""
    def __init__(self, x_size: int, y_size: int) -> None:
        self.x_size = x_size
        self.y_size = y_size 

        # Automatically runs the function createBoard()
        self.create_board()

    def create_board(self):
        """To create a co-ordinate system of (x,y) dimentions"""
        grid_matrix = []
        for y in range(self.y_size):
            grid_matrix.append([])
            for x in range(self.x_size):
                grid_matrix[y].append(0)
        self.grid = grid_matrix
        self.counter = grid_matrix
        return grid_matrix
    
    def switch(self, x, y) -> None:
        """Switches a cell from dead to alive and vise versa."""
        self.grid[y][x] = 0 if self.grid[y][x] >= 1 else 1
    
    def off_board(self, x: int, y: int) -> int:
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


    def check_neighbours(self, x, y):
        """Checks the current state of the  neighbours of a given cell."""
        cells_to_check = self.off_board(x,y)
        live_neighbour_count = 0 
        for cell in cells_to_check:
            match cell:
                case "TL":
                    if self.grid[y-1][x-1]:
                        live_neighbour_count += 1
                case "TC":
                    if self.grid[y-1][x]:
                        live_neighbour_count += 1
                case "TR":
                    if self.grid[y-1][x+1]:
                        live_neighbour_count += 1
                case "CL":
                    if self.grid[y][x-1]: 
                        live_neighbour_count += 1
                case "CR":
                    if self.grid[y][x+1]: 
                        live_neighbour_count += 1
                case "BL":
                    if self.grid[y+1][x-1]: 
                        live_neighbour_count += 1
                case "BC":
                    if self.grid[y+1][x]:
                        live_neighbour_count += 1
                case "BR":
                    if self.grid[y+1][x+1]:
                        live_neighbour_count += 1
        return live_neighbour_count

    def next_population(self): 
        """Returns the matrix of the next population."""
        for y in range(self.y_size):
            for x in range(self.x_size):
                # if self.check_neighbours(x , y) < 2 and self.grid[y][x] == 0: self.switch(x,y)
                # if self.check_neighbours(x , y) > 3 and self.grid[y][x] >= 1: self.switch(x,y)
                # if self.check_neighbours(x, y) == 3 and self.grid[y][x] == 0: self.switch(x,y)
                if self.grid[y][x] >= 1: self.counter[y][x] += 1
        return self.counter



        


# BACKGROUND_COLOR = (0, 0, 0)
# BUTTON_COLOR = (255, 255, 255)
# BUTTON_FONT_COLOR = (0, 0, 255)
# pygame.font.init()
# font = pygame.font.SysFont("pwchalk", 24)
# class Button():
#     def __init__(self, x, y, width, height, text):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text
#         self.rect = pygame.Rect(x, y, width, height)

#     def draw(self, screen):
#         pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
#         label = font.render(self.text, 1, BUTTON_FONT_COLOR)
#         screen.blit(label, (self.x + 10, self.y + 10))

#     def check_click(self, pos):
#         if self.rect.collidepoint(pos):
#             return True
#         return False