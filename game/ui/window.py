import pygame as pg

DEFAULT_SIZE = (1280, 720)
DEFAULT_TITLE = "Survivor Py - Dev Build"

def create_display(size=DEFAULT_SIZE, title=DEFAULT_TITLE) -> pg.Surface:
    """Ініціалізує pygame і створює вікно."""
    pg.init()
    screen = pg.display.set_mode(size)   # можна додати pg.RESIZABLE / FULLSCREEN
    pg.display.set_caption(title)
    return screen

def shutdown():
    """Коректне завершення."""
    pg.quit()