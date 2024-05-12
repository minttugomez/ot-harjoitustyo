from os import path
import pygame
from memorygame import MemoryGame

class Button:

    """ Class for handling buttons

    Attributes:
        rect: dimensions of the rectancle
        display: set display
        action: action for button clicks
        picture: picture that shows on the button
        color: color of the button """

    def __init__(self, rect, display, action = None, picture = None, color = (255, 255, 255)):

        """ Constuctor for the class. Creates a button.

        Args:
            rect: dimensions of the rectancle
            display: set display
            action: action for button clicks
            picture: picture that shows on the button
            color: color of the button """

        self.rect = rect
        self.display = display
        self.action = action
        self.picture = picture
        self.color = color
        self.click_color = self.darken(color)
        self.clicked = False
        self.valid = True

    def draw(self):

        """ Draws the button. """

        if self.valid:
            if self.clicked:
                pygame.draw.rect(self.display, self.click_color, self.rect)
            else:
                pygame.draw.rect(self.display, self.color, self.rect)
            pygame.draw.rect(self.display, (0, 0, 0), self.rect, 5)
            if self.picture:
                self.display.blit(self.picture, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):

        """ Handles event when button is clicked.

        Args:
            event: pygame event """

        if not self.valid:
            return
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

        """ Returns darker version of the original color

        Args:
            color: original color

        Returns:
            darkened_color: darker version of the original color """

        darkened_color = tuple(max(0, component - 50) for component in color)
        return darkened_color

    def change_picture(self, picture):

        """ Changes the picture on the button

        Args:
            picture: new picture """

        self.picture = picture

class UI:

    """ Class for handling user interface interactions.

    Attributes:
        memorygame: MemoryGame-item that is already initialized"""

    def __init__(self, memorygame=MemoryGame):

        """ Constructor for the class. Creates a user interface for the game.

        Args:
            memorygame: MemoryGame-item that is already initialized """

        self.memorygame = memorygame

        questionmark_path = path.join(path.dirname(__file__), 'assets/questionmark.png')
        questionmark = pygame.image.load(questionmark_path)
        self.questionmark = pygame.transform.scale(questionmark, (80, 80))

        circle_path = path.join(path.dirname(__file__), 'assets/circle.png')
        circle = pygame.image.load(circle_path)
        self.circle = pygame.transform.scale(circle, (100, 100))

        self.error_message = False
        self.reset_cards_flag = False
        self.reset_cards_time = 0

        self.screen_height = 1000
        self.screen_width = 1040

        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.init()

        self.font = pygame.font.Font(None, 80)
        self.smaller_font = pygame.font.Font(None, 50)

        self.buttons = []
        self.menu_buttons = []
        self.end_buttons = []

    def setup(self):

        """ Sets things up. Runs through all the fundamental methods. """

        pygame.display.set_caption("Memory game")
        pygame.display.set_icon(self.questionmark)

        self.memorygame.setup()

        self.create_grid()
        self.create_menu_buttons()
        self.create_end_buttons()

    def create_grid(self):

        """ Creates buttons for every grid item. """

        for i, row in enumerate(self.memorygame.grid):
            for j, _ in enumerate(row):

                x = j * 110 + 30
                y = i * 110 + 100

                rect = pygame.Rect(x, y, 100, 100)
                color = (75, 150, 100)
                picture = self.questionmark
                action = self.create_card_click_handler(i, j)
                button = Button(rect, self.display, action, picture, color)
                self.buttons.append(button)

    def create_card_click_handler(self, i, j):

        """ Creates a card click handler for the grid buttons.

        Args:
            i: row index
            j: column index

        Returns:
            handler: card click handler """

        def handler():
            self.handle_card_click(i, j)
        return handler

    def create_menu_buttons(self):

        """ Creates buttons for menu items. """

        for i in range(2, 5):
            x = 525 + (i - 2) * 100
            y = 400

            rect = pygame.Rect(x - 30, y - 20, 90, 90)
            action = action = self.create_player_select_handler(i)
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

    def create_player_select_handler(self, i):

        """ Creates a card click handler for the player buttons.

        Args:
            i: the button index

        Returns:
            handler: card click handler """

        def handler():
            self.handle_player_select(i)
        return handler

    def create_end_buttons(self):

        """ Creates buttons for game ending screen. """

        x = 425
        y = 570
        rect = pygame.Rect(x - 105, y - 35, 400, 120)
        action = self.back_to_menu
        picture = self.add_padding(self.font.render("CONTINUE", True, (0, 0, 0)), 40, 25)
        color = (75, 150, 100)
        end_button = Button(rect, self.display, action, picture, color)
        self.end_buttons.append(end_button)

    def add_padding(self, surface, padding_x, padding_y):

        """ Adds padding to certain surface items.

        Args:
            surface: surface item
            padding_x: padding added on left side
            padding_y: padding added above

        Returns:
            new_surface: new surface item that includes the padding """

        x = padding_x
        y = padding_y
        x_2 = surface.get_width()
        y_2 = surface.get_height()
        new_surface = pygame.Surface((x_2 + x, y_2 + y), pygame.SRCALPHA)
        new_surface.fill((0, 0, 0, 0))
        new_surface.blit(surface, (padding_x, padding_y))
        return new_surface

    def start(self):

        """ Runs the application.
        Takes care of drawing buttons and handling events.
        Closes the application when done. """

        self.setup()

        running = True
        while running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.memorygame.is_ended():
                    self.handle_buttons(self.end_buttons, event)
                elif not self.memorygame.is_started():
                    self.handle_buttons(self.menu_buttons, event)
                else:
                    self.handle_buttons(self.buttons, event)

            self.display.fill((200, 200, 200))
            for button in self.buttons:
                if button.valid:
                    button.draw()

            if self.memorygame.is_started():
                self.write_points(self.memorygame.get_points())
            else:
                self.draw_menu_screen()
                for button in self.menu_buttons:
                    button.draw()
            if self.error_message:
                error_message = "choose players first"
                text_surface = self.smaller_font.render(error_message, True, (255, 0, 0))
                self.display.blit(text_surface, (350, 660))
            self.draw_circle()

            if self.memorygame.is_ended():
                self.draw_end_screen()
                for button in self.end_buttons:
                    button.draw()

            if self.reset_cards_flag and current_time >= self.reset_cards_time:
                for button in self.buttons:
                    button.change_picture(self.questionmark)
                self.reset_cards_flag = False
                if self.memorygame.get_match():
                    for card in self.memorygame.get_match():
                        self.remove_button(card[0], card[1])
                    if not self.check_valid_buttons():
                        self.memorygame.end()
                    self.memorygame.new_turn()
                else:
                    self.memorygame.next_turn()

            pygame.display.update()

        pygame.quit()

    def handle_buttons(self, buttons, event):

        """ Handles button events.

        Args:
            buttons: list of buttons that are gone through
            event: occurred pygame event """

        for button in buttons:
            button.handle_event(event)

    def start_game(self):

        """ Starts the memory game. """

        if self.memorygame.players != 0:
            self.memorygame.start()
            self.error_message = False
        else:
            self.error_message = True

    def back_to_menu(self):

        """ Returns to menu after the game ending screen. """

        self.memorygame.back_to_menu()

    def handle_card_click(self, row, col):

        """ Handles card clicks.
        Shows the pictures in cards and turns them back when the turn is over.

        Args:
            row: row index of the given card
            col: column index of the given card """

        turn_over = self.memorygame.choose_card(row, col, self.memorygame.get_turn())
        picture = self.memorygame.get_picture(row, col)
        button = self.buttons[(row)*9 + col]
        if self.memorygame.get_opened_cards() <= 2:
            button.change_picture(picture)

        if turn_over:
            self.reset_cards_time = pygame.time.get_ticks() + 1000
            self.reset_cards_flag = True

    def remove_button(self, row, col):

        """ Makes buttons invalid after they have been collected.

        Args:
            row: row index of the given card
            col: column index of the given card """

        index = row * 9 + col
        if 0 <= index < len(self.buttons):
            self.buttons[index].valid = False

    def check_valid_buttons(self):

        """ Checks if there are valid cards left.

        Returns:
            True if valid cards exist, False if not """

        for button in self.buttons:
            if button.valid:
                return True
        return False

    def handle_player_select(self, players):

        """ Handles player select button clicks.

        Args:
            players: how many players have been selected """

        self.memorygame.change_players(players)

    def write_points(self, points):

        """ Writes down the current point situation.

        Args:
            points: dictionary of current game points """

        for player in points:

            text = f"{player}: {points[player]}"
            x = 50 + (player-1) * 260
            y = 30

            self.display.blit(self.font.render(text, True, (0, 0, 0,)), (x, y))

    def draw_menu_screen(self):

        """ Draws menu screen excluding the buttons. """

        pygame.draw.rect(self.display, (200, 200, 200), (200, 230, 640, 500))
        pygame.draw.rect(self.display, (0, 0, 0), (200, 230, 640, 500), 5)

        self.display.blit(self.font.render("MENU", True, (0, 0, 0)), (435, 280))
        self.display.blit(self.font.render("Players:", True, (0, 0, 0)), (250, 400))

    def draw_end_screen(self):

        """ Draws game end screen excluding the buttons. """

        pygame.draw.rect(self.display, (200, 200, 200), (200, 230, 640, 500))
        pygame.draw.rect(self.display, (0, 0, 0), (200, 230, 640, 500), 5)

        self.display.blit(self.font.render("Final score", True, (0, 0, 0)), (370, 280))
        i = 1
        points = self.memorygame.get_points
        while i <= self.memorygame.get_players():
            self.display.blit(self.font.render(f"Player {i}: {points[i]}", True, (0, 0, 0)),
                                (250, 400 + (i-1)*20))
            i += 1

    def draw_circle(self):

        """ Draws a circle in a specified spot.
        Before the game starts the circle shows on selected players.
        After the game starts it shows on whose turn it is."""

        if not self.memorygame.is_started():
            if self.memorygame.players:
                x = 490 + (self.memorygame.players- 2) * 100
                y = 375

                self.display.blit(self.circle, (x, y))
        else:
            rescaled_circle = pygame.transform.scale(self.circle, (200, 80))

            x = 15 + (self.memorygame.get_turn()-1) * 260
            y = 15

            self.display.blit(rescaled_circle, (x, y))
