import pygame
import sys
from level import level

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Moveable bakcground')
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.QUIT()
      sys.exit()

  screen.fill('white')
  level.run()

  pygame.display.update()
  clock.tick(60)