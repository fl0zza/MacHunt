import pygame

from classes.DuckFactory import DuckFactory


class Program:

    window_width = 0
    window_height = 0
    image_path = {
        "background": {
            "intro": [
                "images/intro.jpg"
            ],
            "playing": [
                "images/atwork.jpg"
            ],
            "gameover": [
                "images/gameover.jpg"
            ]
        },
        "duck": [
            "images/duck/mac.png",
            "images/duck/steve_head.png",
            "images/duck/steve_head2.png"
        ],
        "button_background": "images/btn_bg.png"
    }
    window = ""

    max_difficulty_level = 3
    ducks = []

    difficulty_level = 0

    base_hit_points = 0
    bonus_hit_points = 0
    duck_speed_multiplier = 0
    simultaneous_ducks_count_max = 0

    player_score = 0
    player_remaining_lives = 0

    def __init__(self, window_width=1000, window_height=800):
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Mac Hunt")

    def new_game(self, difficulty_level):
        if difficulty_level < 1:
            difficulty_level = 1
        if difficulty_level > self.max_difficulty_level:
            difficulty_level = self.max_difficulty_level
        self. difficulty_level = difficulty_level
        # Level dependant modifiers
        self.duck_speed_multiplier = 1 * (difficulty_level * 2)
        self.simultaneous_ducks_count_max = 1 + (difficulty_level - 1)
        self.base_hit_points = 1
        self.bonus_hit_points = self.base_hit_points * 2

        self.ducks = []
        self.player_score = 0
        self.player_remaining_lives = 3 - (difficulty_level - 1)

        while len(self.ducks) < self.simultaneous_ducks_count_max:
            self.ducks.append(DuckFactory.generate())

    @staticmethod
    def create_image_from(image_path, width, height):
        return pygame.transform.scale(pygame.image.load(image_path), (width, height))

    def set_intro_screen(self):
        background_image = Program.create_image_from(self.image_path["background"]["intro"][0], self.window_width,
                                                     self.window_height)
        self.window.blit(background_image, (0, 0))

        new_game_button_background = self.create_image_from(self.image_path["button_background"], 200, 70)
        quit_button_background = self.create_image_from(self.image_path["button_background"], 200, 70)

        self.window.blit(new_game_button_background, (90, 220))
        self.window.blit(new_game_button_background, (460, 470))

    def run(self):
        self.set_intro_screen()
        leave = False
        while not leave:
            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    leave = True

                pygame.display.update()

        pygame.quit()
        quit()
