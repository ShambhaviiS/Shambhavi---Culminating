import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Moving character test')
x = 100
y = 100
speed = 3
width = 10
height = 7
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
        print('l')
    if key[pygame.K_RIGHT] and x<500-width:
        x += speed
        print('r')
    if key[pygame.K_UP] and y>0:
        y -= speed
        print('u')
    if key[pygame.K_DOWN] and y<500-height:
        y += speed
        print('d')
    pygame.draw.rect(screen, 'black',(x,y,width, height))
    pygame.draw.circle(screen, 'black', (x+5,y-5),5)
    pygame.display.update()

    