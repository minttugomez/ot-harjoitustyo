from os import path
import pygame
from memorygame import MemoryGame

class UI:
    def __init__(self, memorygame=MemoryGame):
        self.memorygame = memorygame

        questionmark_path = path.join(path.dirname(__file__), 'assets/questionmark.png')
        questionmark = pygame.image.load(questionmark_path)
        self.questionmark = pygame.transform.scale(questionmark, (80, 80))

        self.screen_height = 1000
        self.screen_width = 1040

        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.init()
        
        self.font = pygame.font.Font(None, 80)

    def setup(self):
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
            self.write_points(self.memorygame.get_points())

            if not self.memorygame.is_started():
                self.draw_menu_screen()

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

    def write_points(self, points):
        for player in points:

            text = f"{player}: {points[player]}"
            x = 50 + (player-1) * 260
            y = 30

            self.display.blit(self.font.render(text, True, (0, 0, 0,)), (x, y))

    def draw_menu_screen(self):
        pygame.draw.rect(self.display, (175, 175, 175), (200, 230, 640, 500))
        pygame.draw.rect(self.display, (0, 0, 0), (200, 230, 640, 500), 5)

        self.display.blit(self.font.render("MENU", True, (0, 0, 0,)), (435, 280))
        self.display.blit(self.font.render("Players:", True, (0, 0, 0,)), (250, 400))

        for i in range(2,5):
            x = 525 + (i-2) * 100
            y = 400

            pygame.draw.rect(self.display, (75, 150, 100), (x - 30, y - 20, 90, 90))
            pygame.draw.rect(self.display, (0, 0, 0), (x - 30, y - 20, 90, 90), 5)
            self.display.blit(self.font.render(str(i), True, (0, 0, 0,)), (x, y))

        x = 425
        y = 570
        pygame.draw.rect(self.display, (75, 150, 100), (x - 105, y - 35, 400, 120))
        pygame.draw.rect(self.display, (0, 0, 0), (x - 105, y - 35, 400, 120), 5)
        self.display.blit(self.font.render("START", True, (0, 0, 0,)), (x, y))
