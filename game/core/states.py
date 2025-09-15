import pygame as pg

WHITE = (240, 240, 240)
BG    = (30, 30, 10)
OVER  = (0, 0, 0, 160)

class BaseState:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.SysFont("consolas", 28)

    def handle_event(self, event): ...
    def update(self, dt: float): ...
    def draw(self, surface: pg.Surface): ...

class MenuState(BaseState):
    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_RETURN, pg.K_SPACE):
                self.game.set_state(RunState(self.game))
            elif event.key == pg.K_q:
                self.game.running = False

    def draw(self, surface):
        surface.fill(BG)
        self._center(surface, "MENU", -40)
        self._center(surface, "[Enter] Start    [Q] Quit", 10)

    def _center(self, srf, text, dy=0):
        img = self.font.render(text, True, WHITE)
        rect = img.get_rect(center=(self.game.size[0]//2, self.game.size[1]//2 + dy))
        srf.blit(img, rect)

class RunState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.t = 0.0 # пока что ебланчик просто по колу двигает

    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key in (pg.K_ESCAPE, pg.K_p):
            self.game.set_state(PauseState(self.game))

    def update(self, dt: float):
        self.t += dt

    def draw(self, surface):
        surface.fill((22, 24, 32))
        vec = pg.math.Vector2(200, 0).rotate_rad(self.t)
        cx, cy = self.game.size[0]//2, self.game.size[1]//2
        pg.draw.circle(surface, (200, 220, 255), (int(cx + vec.x), int(cy + vec.y)), 20)

class PauseState(BaseState):
    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_ESCAPE, pg.K_p, pg.K_r):
                self.game.set_state(RunState(self.game))
            elif event.key == pg.K_m:
                self.game.set_state(MenuState(self.game))
            elif event.key == pg.K_q:
                self.game.running = False

    def draw(self, surface):
        # здесь оно типо затемняет ыфраолывщад
        overlay = pg.Surface(self.game.size, pg.SRCALPHA)
        overlay.fill(OVER)
        surface.blit(overlay, (0, 0))
        self._center(surface, "PAUSED", -20)
        self._center(surface, "[R/ESC] Resume   [M] Menu   [Q] Quit", 24)

    def _center(self, srf, text, dy=0):
        img = self.font.render(text, True, WHITE)
        rect = img.get_rect(center=(self.game.size[0]//2, self.game.size[1]//2 + dy))
        srf.blit(img, rect)