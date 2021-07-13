import pygame

from utils import load_sprite


class SpaceRocks():

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

    def main_loop(self):
        while True:
            self._input()
            self._game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("PySpace")

    def _input(self):
        for event in pygame.event.get():
            # close the game with alt+4 (windows and linux) or cmd + w (mac)
            if event.type == pygame.QUIT or (
                # close the game with ESC
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()