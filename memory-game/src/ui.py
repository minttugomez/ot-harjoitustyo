from os import path
import pygame
from memorygame import MemoryGame

class Button:
    def __init__(self, rect, display, action = None, picture = None, color = (255, 255, 255)):
        self.rect = rect
        self.display = display
        self.action = action
        self.picture = picture
        self.color = color
        self.click_color = self.darken(color)
        self.clicked = False

    def draw(self):
        if self.clicked:
            pygame.draw.rect(self.display, self.click_color, self.rect)
        else:
            pygame.draw.rect(self.display, self.color, self.rect)
        pygame.draw.rect(self.display, (0, 0, 0), self.rect, 5)
        if self.picture:
            self.display.blit(self.picture, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
                self.clicked = False

        if event.type == pygame.MOUSEMOTION:
            if self.clicked and not self.rect.collidepoint(event.pos):
                self.clicked = False

    def darken(self, color):
        darkened_color = tuple(max(0, component - 50) for component in color)
        return darkened_color

class UI:
    def __init__(self, memorygame=MemoryGame):
        self.memorygame = memorygame

        questionmark_path = path.join(path.dirname(__file__), 'assets/questionmark.png')
        questionmark = pygame.image.load(questionmark_path)
        self.questionmark = pygame.transform.scale(questionmark, (80, 80))

        circle_path = path.join(path.dirname(__file__), 'assets/circle.png')
        circle = pygame.image.load(circle_path)
        self.circle = pygame.transform.scale(circle, (100, 100))

        self.screen_height = 1000
        self.screen_width = 1040

        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.init()

        self.font = pygame.font.Font(None, 80)
        self.buttons = []
        self.menu_buttons = []

    def setup(self):
        pygame.display.set_caption("Memory game")
        pygame.display.set_icon(self.questionmark)

        self.memorygame.setup()

        self.create_grid()
        self.create_menu_buttons()

    def create_grid(self):

        for i, row in enumerate(self.memorygame.grid):
            for j, card in enumerate(row):

                x = j * 110 + 30
                y = i * 110 + 100

                rect = pygame.Rect(x, y, 100, 100)
                color = (75, 150, 100)
                picture = self.questionmark
                action = lambda i=i, j=j: self.handle_card_click(i, j)
                button = Button(rect, self.display, action, picture, color)
                self.buttons.append(button)

    def create_menu_buttons(self):

        for i in range(2, 5):
            x = 525 + (i - 2) * 100
            y = 400

            rect = pygame.Rect(x - 30, y - 20, 90, 90)
            action = lambda i=i: self.handle_player_select(i)
            picture = self.add_padding(self.font.render(str(i), True, (0, 0, 0)), 20, 10)
            color = (75, 150, 100)
            button = Button(rect, self.display, action, picture, color)
            self.menu_buttons.append(button)

        x = 425
        y = 570
        rect = pygame.Rect(x - 105, y - 35, 400, 120)
        action = self.start_game
        picture = self.add_padding(self.font.render("START", True, (0, 0, 0)), 100, 25)
        color = (75, 150, 100)
        start_button = Button(rect, self.display, action, picture, color)
        self.menu_buttons.append(start_button)

    def add_padding(self, surface, padding_x, padding_y):
        x = padding_x
        y = padding_y
        x_2 = surface.get_width()
        y_2 = surface.get_height()
        new_surface = pygame.Surface((x_2 + x, y_2 + y), pygame.SRCALPHA)
        new_surface.fill((0, 0, 0, 0))
        new_surface.blit(surface, (padding_x, padding_y))
        return new_surface

    def start(self):
        self.setup()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if not self.memorygame.is_started():
                    for button in self.menu_buttons:
                        button.handle_event(event)
                else:
                    for button in self.buttons:
                        button.handle_event(event)

            self.display.fill((200, 200, 200))
            for button in self.buttons:
                button.draw()
            if self.memorygame.is_started():
                self.write_points(self.memorygame.get_points())
            else:
                self.draw_menu_screen()
                for button in self.menu_buttons:
                    button.draw()
                self.draw_circle()

            pygame.display.update()

        pygame.quit()

    def start_game(self):
        if self.memorygame.players != 0:
            self.memorygame.start()

    def handle_card_click(self, row, col):
        pass

    def handle_player_select(self, players):
        self.memorygame.change_players(players)

    def write_points(self, points):
        for player in points:

            text = f"{player}: {points[player]}"
            x = 50 + (player-1) * 260
            y = 30

            self.display.blit(self.font.render(text, True, (0, 0, 0,)), (x, y))

    def draw_menu_screen(self):
        pygame.draw.rect(self.display, (200, 200, 200), (200, 230, 640, 500))
        pygame.draw.rect(self.display, (0, 0, 0), (200, 230, 640, 500), 5)

        self.display.blit(self.font.render("MENU", True, (0, 0, 0)), (435, 280))
        self.display.blit(self.font.render("Players:", True, (0, 0, 0)), (250, 400))

    def draw_circle(self):

        if self.memorygame.players:
            x = 490 + (self.memorygame.players- 2) * 100
            y = 375

            self.display.blit(self.circle, (x, y))
