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
[1, 1, 10, 6, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[4, 7, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 9, 2, 6, 0, 1, 1, 0],
[0, 0, 0, 14, 0, 9, 2, 6, 0, 0, 0, 0, 9, 13, 0, 0, 0, 1, 1, 0],
[0, 0, 9, 6, 0, 5, 1, 3, 0, 0, 0, 0, 5, 1, 0, 0, 1, 1, 1, 0],
[0, 0, 5, 3, 0, 5, 1, 10, 6, 0, 9, 2, 13, 1, 6, 0, 1, 1, 1, 0],
[2, 2, 13, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0],
[1, 1, 1, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0],
[1, 1, 1, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0],
[1, 1, 1, 3, 0, 5, 1, 1, 3, 0, 5, 1, 1, 1, 3, 0, 1, 1, 1, 0]]


world = World(level1_map)

run = True
while run:

	screen.blit(bg, (0, 0))

	world.draw()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()