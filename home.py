import pygame
from functions import draw_button 
pygame.init()
screen=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running= True

# Loading the home page background
img=pygame.image.load("home.png")
img.convert()
rect= img.get_rect()
# rect.width = screen.get_width()/2 - 100
# rect.height = screen.get_height()/2 - 100
rect.center = (screen.get_width()/2), (screen.get_height()/2)

quit, text_quit = draw_button("Quit", 300, 100)
play, text_play = draw_button("Play", (screen.get_width()/2), (screen.get_height()/2))



while running:

    screen.blit(img,rect)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
            pygame.quit()
        



        if event.type == pygame.MOUSEBUTTONDOWN: # Quit Button
            if quit.collidepoint(event.pos):
                pygame.quit()

    a, b = pygame.mouse.get_pos()
    if quit.x <= a  <= quit.x + 110 and quit.y <= b <= quit.y + 60:
        pygame.draw.rect(screen,  (180, 180, 180), quit)
    else:
        pygame.draw.rect(screen,  (110, 110, 110), quit)
        screen.blit(text_quit, (quit.x + 5, quit.y + 5))

    
    if play.x <= a  <= play.x + 110 and play.y <= b <= play.y + 60:
        pygame.draw.rect(screen,  (180, 180, 180), play)
    else:
        pygame.draw.rect(screen,  (110, 110, 110), play)
        screen.blit(text_play, (play.x + 5, play.y + 5))

        pygame.display.update()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
