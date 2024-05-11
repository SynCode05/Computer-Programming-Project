import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from assets import colours, presets
from functions import draw_button, draw_grid
from game import create_board, update_grid, switch
from random import randrange



pygame.mixer.init()

music = ["assets/soundtracks/minecraft.mp3", "assets/soundtracks/nyan_cat.mp3", "assets/soundtracks/pedro.mp3"]

pygame.mixer.music.load(music[randrange(len(music))])

data = { "x_size": 100, "y_size": 100 }
preset = presets.configs["none"]
preset_counter = 0
preset_name, preset_hovered_colour, preset_colour = presets.preset_state[0]

logo = pygame.image.load("assets/ECAM.png")
pygame.display.set_icon(logo)

BG = pygame.image.load("assets/Background.png")

def main_menu():
    screen = pygame.display.set_mode((1048, 720), pygame.NOFRAME)
    pygame.display.set_caption('Connaway - Game of Life | Main Menu')

    play_text_box, play_button = draw_button('PLAY', screen.get_width()/2, 200, 250, 100)
    mods_text_box, mods_button = draw_button('MODS', screen.get_width()/2, 400, 250, 100)
    quit_text_box, quit_button = draw_button('QUIT', screen.get_width()/2, 600, 250, 100)

    while True:

        screen.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos): game_page(); return
            if event.type == pygame.MOUSEBUTTONDOWN and mods_button.collidepoint(event.pos): mods_page(); return
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

def game_page() -> None:

    global preset_counter; global preset

    if preset == presets.configs["random"]: 
        for i in range((data['x_size']**2) // 5):
            preset.append((randrange(data["x_size"]), randrange(data["y_size"])))

    pygame.display.set_caption('Connaway - Game of Life | Game')


    grid = create_board(data)

    for coordinates in preset: 
        switch(grid, coordinates[0], coordinates[1])

    state, state_colour, state_hovered_colour = 'START', colours.GREEN, colours.HOVERED_GREEN
    global preset_name; global preset_hovered_colour; global preset_colour

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    reset_text_box, reset_button = draw_button('RESET', screen.get_width()/8*7, screen.get_height()/2, 300, 100)
    quit_text_box, quit_button = draw_button('BACK', screen.get_width()/8*7, screen.get_height()/2 + 300, 300, 100)

    slider = Slider(screen, 100, 0, 400, 20, min=1, max=90, step=1, colour = colours.AQUA, handleColour = colours.HOVERED_AQUA)

    time_now, finish_time = pygame.time.get_ticks(), pygame.time.get_ticks()

    while True:
        
        screen.fill(colours.BLACK)
        
        time_now = pygame.time.get_ticks()

        grid_background, cells, cell_coulour = draw_grid(50, 50, screen.get_width() - (250 * 2), screen.get_height() - (50 * 2), grid)
        pygame.draw.rect(screen, colours.AQUA, grid_background, border_radius = 5)


        for i, cell in enumerate(cells):
            pygame.draw.rect(screen, cell_coulour[i], cell) 


        start_stop_text_box, start_stop_button = draw_button(state, screen.get_width()/8*7, screen.get_height()/2 - 250, 300, 100)
        preset_text_box, preset_button = draw_button(preset_name, screen.get_width()/8*7, screen.get_height()/2 + 150, 300, 100)

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set a flag to indicate that the button is being pressed
                    if start_stop_button.collidepoint(event.pos): start_button_pressed = True 
                    if preset_button.collidepoint(event.pos): preset_button_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:

                    # Check if the mouse position is inside the rectangle
                    for i, cell in enumerate(cells): 
                        if cell.collidepoint((x, y)) and state == 'START':
                            switch(grid, (i % data["x_size"]), (i // data["x_size"]))

                    if start_stop_button.collidepoint(event.pos) and start_button_pressed:
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
                        start_button_pressed = False



                    if preset_button.collidepoint(event.pos) and preset_button_pressed and state == "START":
                        # Toggle the state and update the colors
                        item_index = preset_counter%len(presets.preset_state)
                        preset_name, preset_hovered_colour, preset_colour = presets.preset_state[item_index]
                        preset = presets.configs[(preset_name).lower()]
                        preset_counter += 1
                        # Reset the flag
                        preset_button_pressed = False      
                        
                        game_page() ; return              

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

        # Preset Button
        if preset_button.x <= x <= preset_button.x + preset_button.width and preset_button.y <= y <= preset_button.y + preset_button.height:
            pygame.draw.rect(screen, preset_hovered_colour, preset_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, preset_colour, preset_button, border_radius = 25)
        text_x = preset_button.x + (preset_button.width - preset_text_box.get_width()) / 2
        text_y = preset_button.y + (preset_button.height - preset_text_box.get_height()) / 2
        screen.blit(preset_text_box, (text_x, text_y))


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


        if state != "START" and finish_time < time_now:
            # print_grid(grid)
            update_grid(grid, data)
            finish_time = time_now + 1000 - slider.getValue()/100 * 1000
        
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
        

def mods_page():

    screen = pygame.display.set_mode((1048, 720), pygame.NOFRAME)


    pygame.display.set_caption('Connaway - Game of Life | Mods Menu')
    
    quit_text_box, quit_button = draw_button('Back', screen.get_width()/2, 600, 250, 100)
    state, state_colour, state_hovered_colour = 'Music: OFF', colours.GRAY, colours.HOVERED_GRAY

    
    while True:

        music_start_stop_text_box, music_start_stop_button = draw_button(state, screen.get_width()/2, 200, 600, 100)
        
        screen.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(event.pos): main_menu(); return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_start_stop_button.collidepoint(event.pos):
                    # Set a flag to indicate that the button is being pressed
                    button_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:

                if music_start_stop_button.collidepoint(event.pos) and button_pressed:
                    # Toggle the state and update the colors
                    if state != 'Music: OFF':
                        state = 'Music: OFF'
                        state_colour = colours.GRAY
                        state_hovered_colour = colours.HOVERED_GRAY

                        pygame.mixer.music.stop()
                    else:
                        state = 'Music: ON'
                        state_colour = colours.AQUA
                        state_hovered_colour = colours.HOVERED_AQUA

                        pygame.mixer.music.play()
                    # Reset the flag
                    button_pressed = False


        x, y = pygame.mouse.get_pos()

        # Music Start/Stop Button
        if music_start_stop_button.x <= x <= music_start_stop_button.x + music_start_stop_button.width and music_start_stop_button.y <= y <= music_start_stop_button.y + music_start_stop_button.height:
            pygame.draw.rect(screen, state_hovered_colour, music_start_stop_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, state_colour, music_start_stop_button, border_radius = 25)
        text_x = music_start_stop_button.x + (music_start_stop_button.width - music_start_stop_text_box.get_width()) / 2
        text_y = music_start_stop_button.y + (music_start_stop_button.height - music_start_stop_text_box.get_height()) / 2
        screen.blit(music_start_stop_text_box, (text_x, text_y))

        # Quit Button
        if quit_button.x <= x <= quit_button.x + quit_button.width and quit_button.y <= y <= quit_button.y + quit_button.height:
            pygame.draw.rect(screen, colours.HOVERED_RED, quit_button, border_radius = 25)
        else:
            pygame.draw.rect(screen, colours.RED, quit_button, border_radius = 25)
        text_x = quit_button.x + (quit_button.width - quit_text_box.get_width()) / 2
        text_y = quit_button.y + (quit_button.height - quit_text_box.get_height()) / 2
        screen.blit(quit_text_box, (text_x, text_y))
        
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()

    

# Initialize pygame
pygame.init()


main_menu()


