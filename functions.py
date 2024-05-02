import pygame
from assets import colours

def draw_button(text: str, x: int, y: int, width: int, height: int) -> object:
    "Create a Button and Text Surafce"
    font = pygame.font.Font('assets/PressStart2P-Regular.ttf', 50)
    text_box = font.render(text, True, (255, 255, 255))
    button = pygame.Rect(x-width/2, y-height/2, width, height)

    button.width = width
    button.height = height
    return text_box, button

def draw_grid(x: int, y: int, width: int, height: int, grid: list[list[int]]):
    "Render the grid on the UI"
    cells = []; cell_colours = []; new_cells = []; new_cell_colours = []

    rows = len(grid)
    columns = len(grid[0])

    cell_width = (width-10) / rows
    cell_height = (height-10) / columns

    for row in range(rows):
        for column in range(columns):
            cell = pygame.Rect((x + column * cell_width) + 5, (y + row * cell_height) + 5, cell_width, cell_height)
            cells.append(cell)
            cell_colours.append(colours.WHITE) if grid[row][column] == 0 else cell_colours.append(colours.BLACK)
    # cells.append([new_cells])
    # cell_colours.append([new_cell_colours])
    # new_cells = []
    # new_cell_colours = []
            

    background = pygame.Rect(x, y, width, height)



    return background, cells, cell_colours
