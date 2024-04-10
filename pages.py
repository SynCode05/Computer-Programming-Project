import pygame
from assets import colours
from functions import draw_button, draw_grid
from game import create_board, update_grid, switch, print_grid

pygame.mixer.init()
pygame.mixer.music.load("assets/soundtracks/minecraft.mp3")
# pygame.mixer.music.play()

def main_menu():
    screen = pygame.display.set_mode((1048, 720), pygame.NOFRAME)
    BG = pygame.image.load("assets/Background.png")

    # pygame.display.set_caption('Connaway - Game of Life | Main Menu')

    play_text_box, play_button = draw_button('PLAY', screen.get_width()/2, 200, 250, 100)
    mods_text_box, mods_button = draw_button('MODS', screen.get_width()/2, 400, 250, 100)
    quit_text_box, quit_button = draw_button('QUIT', screen.get_width()/2, 600, 250, 100)

    while True:
        screen.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos): game_page(); return
        if event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(event.pos): pygame.quit()


        x, y = pygame.mouse.get_pos()

        # Play Button
        if play_button.x <= x <= play_button.x + play_button.width and play_button.y <= y <= play_button.y + play_button.height:
            pygame.draw.rect(screen, colours.HOVERED_AQUA, play_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.AQUA, play_button, border_radius = 25)
        text_x = play_button.x + (play_button.width - play_text_box.get_width()) / 2
        text_y = play_button.y + (play_button.height - play_text_box.get_height()) / 2
        screen.blit(play_text_box, (text_x, text_y))

        # Mods Button
        if mods_button.x <= x <= mods_button.x + mods_button.width and mods_button.y <= y <= mods_button.y + mods_button.height:
            pygame.draw.rect(screen, colours.HOVERED_GREEN, mods_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.GREEN, mods_button, border_radius = 25)
        text_x = mods_button.x + (mods_button.width - mods_text_box.get_width()) / 2
        text_y = mods_button.y + (mods_button.height - mods_text_box.get_height()) / 2
        screen.blit(mods_text_box, (text_x, text_y))

        # Quit Button
        if quit_button.x <= x <= quit_button.x + quit_button.width and quit_button.y <= y <= quit_button.y + quit_button.height:
            pygame.draw.rect(screen, colours.HOVERED_RED, quit_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.RED, quit_button, border_radius = 25)
        text_x = quit_button.x + (quit_button.width - quit_text_box.get_width()) / 2
        text_y = quit_button.y + (quit_button.height - quit_text_box.get_height()) / 2
        screen.blit(quit_text_box, (text_x, text_y))


        pygame.display.flip()

def game_page():

    data = { "x_size": 40, "y_size": 40 }
    grid = create_board(data)
    switch(grid, 2, 1) # To switch the state of the cell (Alive/Dead).
    switch(grid, 3, 2)
    switch(grid, 1, 3)
    switch(grid, 2, 3)
    switch(grid, 3, 3)
    state, state_colour, state_hovered_colour = 'START', colours.GREEN, colours.HOVERED_GREEN

    # pygame.display.set_caption('Connaway - Game of Life | Game')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    reset_text_box, reset_button = draw_button('RESET', screen.get_width()/8*7, screen.get_height()/2, 300, 100)
    quit_text_box, quit_button = draw_button('BACK', screen.get_width()/8*7, screen.get_height()/2 + 200, 300, 100)



    while True:
        grid_background, cells, cell_coulour = draw_grid(50, 50, screen.get_width() - (250 * 2), screen.get_height() - (50 * 2), grid)
        pygame.draw.rect(screen, colours.AQUA, grid_background, border_radius = 5)


        for i, cell in enumerate(cells):

            pygame.draw.rect(screen, cell_coulour[i], cell) 


        start_stop_text_box, start_stop_button = draw_button(state, screen.get_width()/8*7, screen.get_height()/2 - 200, 300, 100)

        x, y = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_stop_button.collidepoint(event.pos):
                    # Set a flag to indicate that the button is being pressed
                    button_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:

                # Check if the mouse position is inside the rectangle
                for i, cell in enumerate(cells): 
                    if cell.collidepoint((x, y)):
                        switch(grid, (i % data["y_size"]), (i // data["y_size"]))

                if start_stop_button.collidepoint(event.pos) and button_pressed:
                    # Toggle the state and update the colors
                    if state != 'START':
                        state = 'START'
                        state_colour = colours.GREEN
                        state_hovered_colour = colours.HOVERED_GREEN
                    else:
                        state = 'STOP'
                        state_colour = colours.RED
                        state_hovered_colour = colours.HOVERED_RED
                    # Reset the flag
                    button_pressed = False
                

            if event.type == pygame.MOUSEBUTTONDOWN and reset_button.collidepoint(event.pos): game_page(); return
            if event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(event.pos): main_menu(); return
        
        # Start/Stop Button
        if start_stop_button.x <= x <= start_stop_button.x + start_stop_button.width and start_stop_button.y <= y <= start_stop_button.y + start_stop_button.height:
            pygame.draw.rect(screen, state_hovered_colour, start_stop_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, state_colour, start_stop_button, border_radius = 25)
        text_x = start_stop_button.x + (start_stop_button.width - start_stop_text_box.get_width()) / 2
        text_y = start_stop_button.y + (start_stop_button.height - start_stop_text_box.get_height()) / 2
        screen.blit(start_stop_text_box, (text_x, text_y))

        # Reset Button
        if reset_button.x <= x <= reset_button.x + reset_button.width and reset_button.y <= y <= reset_button.y + reset_button.height:
            pygame.draw.rect(screen, colours.HOVERED_GRAY, reset_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.GRAY, reset_button, border_radius = 25)
        text_x = reset_button.x + (reset_button.width - reset_text_box.get_width()) / 2
        text_y = reset_button.y + (reset_button.height - reset_text_box.get_height()) / 2
        screen.blit(reset_text_box, (text_x, text_y))

        # Quit Button
        if quit_button.x <= x <= quit_button.x + quit_button.width and quit_button.y <= y <= quit_button.y + quit_button.height:
            pygame.draw.rect(screen, colours.HOVERED_RED, quit_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.RED, quit_button, border_radius = 25)
        text_x = quit_button.x + (quit_button.width - quit_text_box.get_width()) / 2
        text_y = quit_button.y + (quit_button.height - quit_text_box.get_height()) / 2
        screen.blit(quit_text_box, (text_x, text_y))

        if state is not "START":
            # print_grid(grid)
            update_grid(grid, data, 0.1)
            # grid = __import__("_thread").start_new_thread(update_grid, (grid, data, 0.1))

        
        pygame.display.flip()
        

def mods_page():
    return
# Initialize pygame
pygame.init()



main_menu()

