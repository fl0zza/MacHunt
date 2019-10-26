import pygame


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

    def __init__(self, window_width=1000, window_height=800):
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Mac Hunt")

    @staticmethod
    def create_image_from(image_path, width, height):
        return pygame.transform.scale(pygame.image.load(image_path), (width, height))

    def set_intro_screen(self):
        background_image = Program.create_image_from(self.image_path["background"]["intro"][0], self.window_width,
                                                     self.window_height)
        self.window.blit(background_image, (0, 0))

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
