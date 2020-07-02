import pygame
import os


def load_pygame_image(image_name: str):
    full_path = os.path.join("assets", "images", image_name)
    try:
        image = pygame.image.load(full_path)
    except pygame.error:
        raise FileNotFoundError
    return image
