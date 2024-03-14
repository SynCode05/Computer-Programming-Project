import pygame

def createGrid(size: int) -> list:
    """This function creates a square grid."""
    GridMatrix = []
    for x in range(size):
        GridMatrix.append([])
        for y in range(size):
            GridMatrix[x].append(0)
    return GridMatrix

print(createGrid(2))