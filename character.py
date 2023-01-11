import os
import pygame


stationary = pygame.image.load(os.path.join("standing.png"))
# One way to do it - using the sprites that face left.
left = [None]*10
for steps in range(1,5):
    left[steps-1] = pygame.image.load(os.path.join("L" + str(steps) + ".png"))
    steps+=1

right = [None]*10
for steps in range(1,5):
    right[steps-1] = pygame.image.load(os.path.join("R" + str(steps) + ".png"))
    steps+=1

class Player():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.vel_x = 10
    self.vel_y = 10
    self.speed = 7
    self.width = 10
    self.height = 7
    move_right = False
    move_left = False
    steps = 0
    
    if steps >= 36:
        steps = 0
    if move_left:
        screen.blit(left[steps%4], (x, y))
        steps += 1
    elif move_right:
        screen.blit(right[steps%4], (x, y))
        steps += 1
    else:
        screen.blit(stationary, (x, y))

  def Input():
    jump = False
    key = pygame.key.get_pressed()
    if jump is False and key[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y * 2
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    if key[pygame.K_LEFT] and x > 0:
        x -= speed
        move_left = True
        move_right = False
    elif key[pygame.K_RIGHT] and x < 1000 - width:
        x += speed
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False



x = 50
y = 300
vel_x = 10
vel_y = 10
speed = 7
width = 10
height = 7
jump = False
move_right = False
move_left = False
steps = 0


def Animation():
    global steps
    screen.fill('white')
    if steps >= 36:
        steps = 0
    if move_left:
        screen.blit(left[steps%4], (x, y))
        steps += 1
    elif move_right:
        screen.blit(right[steps%4], (x, y))
        steps += 1
    else:
        screen.blit(stationary, (x, y))

while True:
    pygame.time.delay(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    Animation()
  
    key = pygame.key.get_pressed()
  
    if jump is False and key[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y * 2
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    if key[pygame.K_LEFT] and x > 0:
        x -= speed
        move_left = True
        move_right = False
        print('')
    elif key[pygame.K_RIGHT] and x < 1000 - width:
        x += speed
        move_left = False
        move_right = True
        print('r')

    else:
        move_left = False
        move_right = False

    pygame.time.delay(30)
    pygame.display.update()
    pygame.draw.rect(screen, 'black', (x, y, width, height))
    pygame.draw.circle(screen, 'black', (x + 5, y - 5), 5)
    pygame.display.update()