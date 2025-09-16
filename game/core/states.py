import pygame as pg

WHITE = (240, 240, 240)
BG_MENU = (30, 30, 30)
BG_RUN  = (22, 24, 32)
OVERLAY = (0, 0, 0, 160)

# ---------- DRAW ----------
def draw_menu(screen: pg.Surface, font: pg.font.Font):
    screen.fill(BG_MENU)
    _center_text(screen, font, "MENU", -40)
    _center_text(screen, font, "[Enter] Start   [Q] Quit", 8)

def draw_run(screen: pg.Surface, font: pg.font.Font, t: float):
    screen.fill(BG_RUN)
    # проста «анімашка»: кружок рухається по колу
    vec = pg.math.Vector2(200, 0).rotate_rad(t)
    w, h = screen.get_size()
    cx, cy = w // 2, h // 2
    pg.draw.circle(screen, (200, 220, 255), (int(cx + vec.x), int(cy + vec.y)), 20)

def draw_pause(screen: pg.Surface, font: pg.font.Font):
    overlay = pg.Surface(screen.get_size(), pg.SRCALPHA)
    overlay.fill(OVERLAY)
    screen.blit(overlay, (0, 0))
    _center_text(screen, font, "PAUSED", -20)
    _center_text(screen, font, "[R/ESC] Resume   [M] Menu   [Q] Quit", 24)

def draw_fps(screen: pg.Surface, font: pg.font.Font, fps: int):
    img = font.render(f"FPS: {fps}", True, WHITE)
    screen.blit(img, (10, 10))

def _center_text(surface: pg.Surface, font: pg.font.Font, text: str, dy: int = 0):
    w, h = surface.get_size()
    img = font.render(text, True, WHITE)
    rect = img.get_rect(center=(w // 2, h // 2 + dy))
    surface.blit(img, rect)

# ---------- EVENTS ----------
def handle_menu_event(event: pg.event.Event, game_state: str, running: bool):
    if event.type == pg.KEYDOWN:
        if event.key in (pg.K_RETURN, pg.K_SPACE):
            game_state = "run"
        elif event.key == pg.K_q:
            running = False
    return game_state, running

def handle_run_event(event: pg.event.Event, game_state: str, running: bool):
    if event.type == pg.KEYDOWN and event.key in (pg.K_ESCAPE, pg.K_p):
        game_state = "pause"
    return game_state, running

def handle_pause_event(event: pg.event.Event, game_state: str, running: bool):
    if event.type == pg.KEYDOWN:
        if event.key in (pg.K_ESCAPE, pg.K_p, pg.K_r):
            game_state = "run"
        elif event.key == pg.K_m:
            game_state = "menu"
        elif event.key == pg.K_q:
            running = False
    return game_state, running