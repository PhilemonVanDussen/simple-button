# Pygame game template

import pygame
import sys

# Color constants (RBG)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
PURPLE = (157, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (150, 75, 0)

# Game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Window title (caption)
# Update the window title as needed
TITLE = 'Simple Button Project'

# Frame rate (frames per second)
FPS = 60

def init_game():
    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen








def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

    button_length = 150
    button_hieght = 30
    button1 = pygame.Rect(280, 200, button_length, button_hieght)
    button2 = pygame.Rect(280, 290, button_length, button_hieght)
    button3 = pygame.Rect(280, 380, button_length, button_hieght)

    font_style = pygame.font.Font('c:\Font\EmblemaOne-Regular.ttf', 50)
    header_style = pygame.font.Font('c:\Font\Tektur-VariableFont_wdth,wght.ttf', 60)
    options_style = pygame.font.Font('c:\Font\EmblemaOne-Regular.ttf', 32)
    header = header_style.render('MAIN MENU', True, RED)
    button1_text = font_style.render('PLAY', True, BLACK)
    button2_text = options_style.render('OPTIONS', True, BLACK)
    button3_text = font_style.render('EXIT', True, BLACK)

    running = True
    while running:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if button1.collidepoint(mouse_pos):
                    print('Now playing the game!')
                elif button2.collidepoint(mouse_pos):
                    print('Game Options!')
                elif button3.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit

        screen.fill(WHITE) # Use color from config
        
        screen.blit(header, (215, 125))

        pygame.draw.rect(screen, GREEN, button1)
        pygame.draw.rect(screen, GREEN, button2)
        pygame.draw.rect(screen, GREEN, button3)

        screen.blit(button1_text, (button1.x + (button_length - button1_text.get_width()) // 2, button1.y + (button_hieght - button1_text.get_height()) // 2))

        screen.blit(button2_text, (button2.x + (button_length - button2_text.get_width()) // 2, button2.y + (button_hieght - button2_text.get_height()) // 2))

        screen.blit(button3_text, (button3.x + (button_length - button3_text.get_width()) // 2, button3.y + (button_hieght - button3_text.get_height()) // 2))

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



