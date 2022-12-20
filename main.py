import os
import pygame

pygame.init()

stationary = pygame.image.load(os.path.join("standing.png"))
# One way to do it - using the sprites that face left.
left = [
    pygame.image.load(os.path.join("L1.png")),
    pygame.image.load(os.path.join("L2.png")),
    pygame.image.load(os.path.join("L3.png")),
    pygame.image.load(os.path.join("L4.png"))
]

right = [
    pygame.image.load(os.path.join("R1.png")),
    pygame.image.load(os.path.join("R2.png")),
    pygame.image.load(os.path.join("R3.png")),
    pygame.image.load(os.path.join("R4.png"))
]

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Moving character test')
x = 100
y = 100
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

    if key[pygame.K_LEFT] and x > 0:
        x -= speed
        move_left = True
        move_right = False
        print('')
    elif key[pygame.K_RIGHT] and x < 500 - width:
        x += speed
        move_left = False
        move_right = True
        print('r')
    elif key[pygame.K_UP] and y > 0:
        y -= speed
        print('u')
    elif key[pygame.K_DOWN] and y < 500 - height:
        y += speed
        print('d')
    elif jump is False and key[pygame.K_SPACE]:
        jump = True
    elif jump is True:
        y -= vel_y * 2
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    else:
        move_left = False
        move_right = False

    pygame.time.delay(30)
    pygame.display.update()
    pygame.draw.rect(screen, 'black', (x, y, width, height))
    pygame.draw.circle(screen, 'black', (x + 5, y - 5), 5)
    pygame.display.update()
