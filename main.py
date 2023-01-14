import pygame

pygame.init()

screen_width = 980
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 40
#load images
bg_img = pygame.image.load('background.png')
bg = pygame.transform.scale(bg_img, (1000, 500))
dirt_img = pygame.image.load('dirt.png')
grass_img = pygame.image.load('grass.png')
grass2_img = pygame.image.load('grass2.png')
grass3_img = pygame.image.load('grass3.png')
grass4_img = pygame.image.load('grass4.png')
grass5_img = pygame.image.load('grass5.png')
grass6_img = pygame.image.load('grass6.png')
grass7_img = pygame.image.load('grass7.png')
grass8_img = pygame.image.load('grass8.png')
grass9_img = pygame.image.load('grass9.png')
grass10_img = pygame.image.load('grass10.png')
grass11_img = pygame.image.load('grass11.png')
grass12_img = pygame.image.load('grass12.png')
plant_png = pygame.image.load('plant.png')

class Player():
  def __init__(self, x, y):
    self.images_right = []
    self.images_left = []
    self.index = 0
    self.counter = 0
    for num in range(1, 4):
      img_right = pygame.image.load('running'+str(num)+'.png')
      img_right = pygame.transform.scale(img_right, (25, 45))
      img_left = pygame.transform.flip(img_right, True, False)
      self.images_right.append(img_right)
      self.images_left.append(img_left)
    self.index = 0
    self.image = self.images_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jumped = False
    self.direction = 0
    self.dx = 0
    self.dy = 0
    self.move_right = False
    self.move_left = False

  def update(self):
    dx = 0
    dy = 0
    walk_cooldown = 5
  
    #get keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and self.jumped == False:
      self.vel_y = -15
      self.jumped = True
    if key[pygame.K_SPACE] == False:
      self.jumped = False
    if key[pygame.K_LEFT]:
      dx -= 2
      self.counter += 1
      self.direction = -1
    if key[pygame.K_RIGHT]:
      dx += 2
      self.counter += 1
      self.direction = 1
    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
      self.counter = 0
      self.index = 0
      if self.direction == 1:
        self.image = self.images_right[self.index]
      if self.direction == -1:
        self.image = self.images_left[self.index]
  
  
    #handle animation
    if self.counter > walk_cooldown:
      self.counter = 0	
      self.index += 1
      if self.index >= len(self.images_right):
        self.index = 0
      if self.direction == 1:
        self.image = self.images_right[self.index]
      if self.direction == -1:
        self.image = self.images_left[self.index]
  
  
    #add gravity
    self.vel_y += 1
    if self.vel_y > 10:
      self.vel_y = 10
    dy += self.vel_y
  
    #check for collision
    for tile in world.tile_list:
      #check for collision in x direction
      if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
        dx = 0
      #check for collision in y direction
      if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
        #check if below the ground i.e. jumping
        if self.vel_y < 0:
          dy = tile[1].bottom - self.rect.top
          self.vel_y = 0
        #check if above the ground i.e. falling
        elif self.vel_y >= 0:
          dy = tile[1].top - self.rect.bottom
          self.vel_y = 0
  
  
  
  
    #update player coordinates
    self.rect.x += dx
    self.rect.y += dy
  
    if self.rect.bottom > screen_height:
      self.rect.bottom = screen_height
      dy = 0
  
    #draw player onto screen
    screen.blit(self.image, self.rect)
    

class World(): 
  def __init__(self, data):
    self.tile_list = []
    
    row_count = 0
    for row in data:
      col_count = 0
      for tile in row:
        if tile == 1:
          img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
          
        elif tile == 2:
          img = pygame.transform.scale(grass_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
          
        elif tile == 3:
          img = pygame.transform.scale(grass2_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
          
        elif tile == 4:
          img = pygame.transform.scale(grass3_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
          
        elif tile == 5:
          img = pygame.transform.scale(grass4_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
          
        elif tile == 6:
          img = pygame.transform.scale(grass5_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
  
        elif tile == 7:
          img = pygame.transform.scale(grass6_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
  
        elif tile == 8:
          img = pygame.transform.scale(grass7_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
          
        elif tile == 9:
          img = pygame.transform.scale(grass8_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
          
        elif tile == 10:
          img = pygame.transform.scale(grass9_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
  
        elif tile == 11:
          img = pygame.transform.scale(grass10_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
          
        elif tile == 12:
          img = pygame.transform.scale(grass11_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 
          
        elif tile == 13:
          img = pygame.transform.scale(grass12_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
  
        elif tile == 14:
          img = pygame.transform.scale(plant_png, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)        
        col_count += 1
      row_count += 1
  
  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])

level1_map = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
[2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 10, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 2, 6, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 9, 2, 6, 0, 0, 0, 0, 9, 13, 0, 0, 0, 1, 1, 0],
[0, 0, 9, 6, 0, 5, 1, 3, 0, 0, 0, 0, 5, 1, 0, 0, 1, 1, 1, 0],
[0, 0, 5, 3, 0, 5, 1, 10, 6, 0, 9, 2, 13, 1, 6, 0, 1, 1, 1, 0],
[2, 2, 13, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0],
[1, 1, 1, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0]]

world = World(level1_map)
player = Player(100, screen_height - 130)

run = True
while run:

	screen.blit(bg_img, (0, 0))
  
	world.draw()

	player.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
