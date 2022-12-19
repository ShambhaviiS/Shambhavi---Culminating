import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Moving character test')
x = 100
y = 100
speed = 7
width = 10
height = 7
vel_x = 10
vel_y = 10
jump = False
while True:
    pygame.time.delay(10)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill('white')
    key  = pygame.key.get_pressed()
  
    if key[pygame.K_LEFT] and x>0:
      
        x -= speed
        print('')
    if key[pygame.K_RIGHT] and x<1000-width:
        x += speed
        print('r')
    if key[pygame.K_UP] and y>0:
        y -= speed
        print('u')
    if key[pygame.K_DOWN] and y<450-height:
        y += speed
        print('d')

    if jump is False and key[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y*2
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(30)
    pygame.display.update()
    pygame.draw.rect(screen, 'black',(x,y,width, height))
    pygame.draw.circle(screen, 'black', (x+5,y-5),5)
    pygame.display.update()

    