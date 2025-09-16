import sys
import pygame as pg

from game.ui.window import create_display, shutdown
from game.core import states as S

# ---- Константи ----
WIDTH, HEIGHT = 1280, 720
TITLE = "Survivor Py - Dev Build"
FPS = 60

# ---- Глобальний простий FSM ----
game_state = "menu"   # "menu" | "run" | "pause"
running = True
t = 0.0               # таймер для анімації у run

def handle_events():
    """Роутинг подій у відповідний хендлер залежно від стану."""
    global running, game_state
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            continue

        if game_state == "menu":
            game_state, running = S.handle_menu_event(event, game_state, running)
        elif game_state == "run":
            game_state, running = S.handle_run_event(event, game_state, running)
        elif game_state == "pause":
            game_state, running = S.handle_pause_event(event, game_state, running)

def update(dt: float):
    """Оновлення логіки (тут порожньо; t інкрементуємо у draw/loop)."""
    pass

def draw(screen: pg.Surface, font: pg.font.Font, clock: pg.time.Clock):
    """Малюємо залежно від стану + FPS."""
    if game_state == "menu":
        S.draw_menu(screen, font)
    elif game_state == "run":
        S.draw_run(screen, font, t)
    elif game_state == "pause":
        S.draw_pause(screen, font)

    S.draw_fps(screen, font, int(clock.get_fps()))

def main():
    global t
    screen = create_display((WIDTH, HEIGHT), TITLE)
    font = pg.font.SysFont("consolas", 28)
    clock = pg.time.Clock()

    while running:
        dt = clock.tick(FPS) / 1000.0
        t += dt

        handle_events()
        update(dt)
        draw(screen, font, clock)

        pg.display.flip()

    shutdown()
    sys.exit()

if __name__ == "__main__":
    main()