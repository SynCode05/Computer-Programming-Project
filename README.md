# Computer-Programming-Project
A project emulating the "game of life"

Example:

```python
from constructors import CreateGrid

def print_grid(grid): 
    """Information on the grid."""
    for row in grid.grid:
        print(" ".join(["⬜" if cell else "⬛" for cell in row]))

grid = CreateGrid(20, 20) # Creates an instance of GreatGrid (20 x 20)
grid.switch(2, 1) # To switch the state of the cell (Alive/Dead).
grid.switch(3, 2)
grid.switch(1, 3)
grid.switch(2, 3)
grid.switch(3, 3)
print("Initial Grid:")
print_grid(grid)

for i in range(20): #Repeats 20 times
    print("\nNext Generation:") 
    print_grid(grid) # Shows a visual representation of the grid in the cli.
    grid.next_population() # Simulates a generation passing. 
```
