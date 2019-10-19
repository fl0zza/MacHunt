import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode( (800,600) )
pygame.display.set_caption("Mon super jeu vidéo")

background = pygame.image.load("bg.jpg")
duck = pygame.image.load("mac.png")
duck = pygame.transform.scale(duck, (100, 100))
gameOverBackground = pygame.image.load("game_over.png")
retryButtonBg = pygame.transform.scale(pygame.image.load("btnBg.png"), (200, 70))
quitButtonBg = pygame.transform.scale(pygame.image.load("btnBg.png"), (200, 70))
#pygame.mixer.init()
#pygame.mixer.music.load("playing.mp3")
#pygame.mixer.music.play()
position_x = 0
position_y = 0

font = pygame.font.SysFont("arial", 32)
clock = pygame.time.Clock()

score = 0
life = 3

gameOver = False
leave = False
while not leave:
  for event in pygame.event.get():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      leave = True
  #print(mouse_x, mouse_y)
  if pygame.mouse.get_pressed()[0] is 1:
    if gameOver:
      if (mouse_x >= 90 
      and mouse_x <= 90 + 200
      and mouse_y >= 470 
      and mouse_y <= 470 + 70):
        score = 0
        life = 3
        gameOver = False
      if (mouse_x >= 460 
      and mouse_x <= 470 + 200
      and mouse_y >= 470 
      and mouse_y <= 470 + 70):
        leave = True
        
    else:
      if (mouse_x >= position_x 
      and mouse_x <= position_x + 100
      and mouse_y >= position_y 
      and mouse_y <= position_y + 100):
        position_x = 0
        position_y = randint(0, 600 - 110)
        score = score + 1

  position_x = position_x + (1 * 4)

  if life <= 0 :
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
    window.blit(retryButtonBg, (90,470))
    window.blit(quitButtonBg, (460,470))
    retryButtonText = font.render("Retry", 3, (255, 255, 255))
    quitButtonText = font.render("Quit", 3, (255, 255, 255))
    window.blit(retryButtonText, (170,495))
    window.blit(quitButtonText, (540,495))
  else:
    window.blit(background, (0, 0))  
    window.blit(duck, (position_x, position_y))
    window.blit(text_score, (10, 10))
    window.blit(text_life, (500, 10))

  pygame.display.update()


#pygame.quit()
#quit()