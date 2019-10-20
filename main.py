import pygame

from random import randint
from classes.Duck import Duck
from classes.DuckFactory import DuckFactory
from classes.Program import Program

pygame.init()

app = Program(1400, 900)

ducks = []
while len(ducks) < 3:
    ducks.append(DuckFactory.generate())

difficultyLevel = 1
maxDifficultyLevel = 3

playerStartLives = 3 - (difficultyLevel - 1)
duckSpeedMultiplier = 1 * (difficultyLevel * 2)
duckCountSimultaneousMax = 1 + (difficultyLevel - 1)
baseHitPoints = 1

playerScore = 0
playerRemainingLives = playerStartLives

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Mac Hunt")

background = pygame.transform.scale(pygame.image.load("bg.jpg"), (windowWidth, windowHeight))
duck = pygame.transform.scale(pygame.image.load("mac.png"), (100, 100))
gameOverBackground = pygame.image.load("game_over.png")
retryButtonBg = pygame.transform.scale(pygame.image.load("btn_bg.png"), (200, 70))
quitButtonBg = pygame.transform.scale(pygame.image.load("btn_bg.png"), (200, 70))
font = pygame.font.SysFont("arial", 32)
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play()

ducks = [Duck()]

position_x = 0
position_y = 0
mouse_x = 0
mouse_y = 0

gameOver = False
leave = False
while not leave:
    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            leave = True
    if pygame.mouse.get_pressed()[0] is 1:
        if gameOver:
            if 90 <= mouse_x <= 90 + 200 and 470 <= mouse_y <= 470 + 70:
                score = 0
                life = 3
                gameOver = False
            if 460 <= mouse_x <= 470 + 200 and 470 <= mouse_y <= 470 + 70:
                leave = True
        else:
            if position_x <= mouse_x <= position_x + 100 and position_y <= mouse_y <= position_y + 100:
                position_x = 0
                position_y = randint(0, 600 - 110)
                score = score + 1

    position_x = position_x + (1 * 4)

    if life <= 0:
        gameOver = True

    if position_x >= 800:
        position_x = -300
        position_y = randint(0, 600 - 110)
        life = life - 3

    text_score = font.render(str(score), 3, (255, 255, 255))
    text_life = font.render(str(life), 3, (255, 255, 255))
    clock.tick(60)

    if gameOver:
        window.blit(gameOverBackground, (0, 0))
        window.blit(retryButtonBg, (90, 470))
        window.blit(quitButtonBg, (460, 470))
        retryButtonText = font.render("Retry", 3, (255, 255, 255))
        quitButtonText = font.render("Quit", 3, (255, 255, 255))
        window.blit(retryButtonText, (170, 495))
        window.blit(quitButtonText, (540, 495))
    else:
        window.blit(background, (0, 0))
        window.blit(duck, (position_x, position_y))
        window.blit(text_score, (10, 10))
        window.blit(text_life, (500, 10))

    pygame.display.update()

# pygame.quit()
# quit()
