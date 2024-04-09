import pygame
from functions import create_button 

pygame.init()
screen=pygame.display.set_mode((1980,1280))
clock=pygame.time.Clock()
running= True

# Loading the home page background
img=pygame.image.load("home.png")
img.convert()
rect= img.get_rect()
rect.center = screen.get_width()/2, screen.get_height()/2



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    screen.blit(img,rect)
    pygame.draw.rect(screen, (255,0,0), rect, 1)

    screen.blit(img,rect)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
