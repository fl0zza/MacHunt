import pygame

from classes.Program import Program


class Duck:

    isBonus = False
    positionX = 0
    positionY = 0
    image = ""

    def __init__(self, is_bonus=False):
        self.image = pygame.transform.scale(pygame.image.load("mac.jpg"),
                                            (Program.windowWidth, Program.windowHeight))
        self.isBonus = is_bonus
        if self.isBonus:
            self.image = pygame.transform.scale(pygame.image.load("steve_head.jpg"),
                                                (Program.windowWidth, Program.windowHeight))

