import pygame
from pygame.locals import *

def disable_close_button():
    pygame.display.set_caption("Your Window Title")  # Set your window title here
    pygame.display.set_mode((800, 600), NOFRAME)

def main():
    pygame.init()
    disable_close_button()

    ui = UIController()
    is_active = True

    while is_active:
        pygame.display.set_mode((800, 600))

        ui.on_update()
        ui.on_close_button_clicked(is_active)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                is_active = False

    pygame.quit()

if __name__ == "__main__":
    main()
