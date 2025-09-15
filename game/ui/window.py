import pygame as pg

# Окно
DEFAULT_SIZE = (1280, 720)
DEFAULT_TITLE = "Survivor Py - Dev Build"

def create_display(size: tuple[int, int] = DEFAULT_SIZE, title: str = DEFAULT_TITLE):
    pg.init()
    screen = pg.display.set_mode(size)
    pg.display.set_caption(title)
    return screen