from os import path
import pygame
from memorygame import MemoryGame

class UI:
    def __init__(self, memorygame=MemoryGame):
        self.memorygame = memorygame

        self.questionmark_path = path.join(path.dirname(__file__), 'assets/questionmark.png')
        self.questionmark = pygame.image.load(self.questionmark_path)
        self.questionmark = pygame.transform.scale(self.questionmark, (80, 80))

        self.screen_height = 1000
        self.screen_width = 1040

        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

    def setup(self):
        pygame.init()

        pygame.display.set_caption("Memory game")
        pygame.display.set_icon(self.questionmark)

        self.memorygame.start()

    def start(self):
        self.setup()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display.fill((175, 175, 175))
            self.draw_grid()
            pygame.display.update()

        pygame.quit()

    def draw_grid(self):
        for i, row in enumerate(self.memorygame.grid):
            for j, card in enumerate(row):

                x = j * 110 + 30
                y = i * 110 + 100

                pygame.draw.rect(self.display, (75, 150, 100), (x, y, 100, 100))
                pygame.draw.rect(self.display, (0, 0, 0), (x, y, 100, 100), 5)
                self.display.blit(self.questionmark, (x+10, y+10))
