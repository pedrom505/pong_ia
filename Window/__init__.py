from Utils import Image
import pygame
import sys


class Screen:

    screen = None
    bg = None

    def __init__(self, size: tuple):
        check_error = pygame.init()
        if check_error[1] > 0:
            sys.exit(-1)
        self.size(size)

    @staticmethod
    def close():
        pygame.quit()

    @staticmethod
    def icon(image_name: str):
        image = Image.load_pygame_image(image_name)
        pygame.display.set_icon(image)

    @staticmethod
    def caption(text: str):
        pygame.display.set_caption(text)

    def size(self, size: tuple):
        self.screen = pygame.display.set_mode(size)

    @staticmethod
    def get_surface():
        return pygame.display.get_surface()

    def background(self,
                   image_name: str = None,
                   color: tuple = None):

        if color is not None:
            self.screen.fill(color)
        if image_name is not None:
            background = Image.load_pygame_image(image_name)
            self.screen.blit(background, (0, 0))

    def update(self, position: tuple = None, size: tuple = None):
        if position is None and size is None:
            pygame.display.update()
        else:
            rectangle = pygame.Rect(position, size)
            pygame.display.update([rectangle])



