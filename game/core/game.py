import pygame as pg
from .states import MenuState
from ..ui.window import create_display

class Game:
    def __init__(self, width=1280, height=720, title="Game"):
        self.size = (width, height)
        self.title = title

        self.screen = create_display(self.size, self.title)
        self.clock = pg.time.Clock()
        self.running = True

        self.state = None
        self.set_state(MenuState(self))

    def set_state(self, state_obj):
        self.state = state_obj

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0 # FPS

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                else:
                    self.state.handle_event(event)

            self.state.update(dt)
            self.state.draw(self.screen)

            # Fps в углу
            fps_img = self.state.font.render(f"FPS: {int(self.clock.get_fps())}", True, (220, 220, 220))
            self.screen.blit(fps_img, (10, 10))

            pg.display.flip()
        
        pg.quit()