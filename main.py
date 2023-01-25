#Name: Shambhavi Sinha 
#Date: January 25, 2022
#Program Name:  Bun Bun Hop!
#Purpose: Players will be a bunny and will have to collect all the carrots without dying to the enemy mushrooms or falling of the world. Highscore will be calculated by how many carrots are collected with each carrots being worth 5 points.

import pygame
import os

pygame.init()

#initialize time and fps
clock = pygame.time.Clock()
fps = 60

#initialize screen width and height according to tile size
screen_width = 1050
screen_height = 525

#create the screen and set a caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bun Bun Hop!')

#define game variables
tile_size = 35
carrots = 0
start_game = False
game_over = 0
menu_state = "main"
score = 0
score_count = 0

if os.path.exists('score.txt'):
	with open('score.txt', 'r') as file:
		high_score = int(file.read())
else:
	high_score = 0

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
restart_img = pygame.image.load('restart_btn.png').convert_alpha()
back_img = pygame.image.load('back_btn.png').convert_alpha()
instructions_img = pygame.image.load('instructions_btn.png').convert_alpha()

#load background image and size it to be the same as the screen width and height
background = pygame.image.load('background.png')
bg_img = pygame.transform.scale(background, (screen_width, screen_height))

#load tile images (grass, dirt)
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

#creates buttons objects
#IN: the x and y coordinate, the image of the button, and the scale (size of the button)
#OUT: button that can be put on the screen
class Button():

	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

  #draws the button to display on the screen
  #IN: the surface (screen/window)
  #OUT: a clickable button
	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draws the button onto the screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
  
		#returns the action
		return action

#creates the player object
#IN: the x and y coordinate, the images for animation, the height and width of the image
#OUT: a moveable character
class Player():
  
  def __init__(self, x, y):
    self.images_right = []
    self.images_left = []
    self.index = 0
    self.counter = 0

    #loop to load all running images
    for num in range(1, 4):
      img_right = pygame.image.load('running'+str(num)+'.png')
      img_right = pygame.transform.scale(img_right, (25, 45))

      #flips the images to get the left version
      img_left = pygame.transform.flip(img_right, True, False)
      self.images_right.append(img_right)
      self.images_left.append(img_left)

    #ghost image for when the player dies
    self.ghost_image = pygame.image.load('ghost.png')
    self.ghost_image = pygame.transform.scale(self.ghost_image, (35, 45))
    
    self.image = self.images_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jumped = False
    self.direction = 0

  #updates the player after moving left, right, or jumping
  #IN: game over variable, allowing the function to update the image when the character is dead as opposed to alive
  #OUT: a moving character with animations
  def update(self, game_over):
    dx = 0
    dy = 0
    walk_cooldown = 5
    score_count = 0

    if game_over == 0:
      #get keypresses
      key = pygame.key.get_pressed()
      if key[pygame.K_SPACE] and self.jumped == False:
        self.vel_y = -15
        score_count 
        self.jumped = True
      if key[pygame.K_SPACE] == False:
        self.jumped = False
      if key[pygame.K_LEFT]:
        dx -= 5
        self.counter += 1
        self.direction = -1
      if key[pygame.K_RIGHT]:
        dx += 5
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

  
      #check for collision with mushrooms, player dies once they collide with them
      if pygame.sprite.spritecollide(self, mushroom_group, False):
        game_over = -1  
      
      #check for collision with tiles
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

    #if player collides with the mushroom, the turn into a ghost
    elif game_over == -1:
      self.image = self.ghost_image
      if self.rect.y > 20:
        self.rect.y -= 5
    
     #draw player onto screen
    screen.blit(self.image, self.rect)

    
    if self.rect.bottom > screen_height:
      self.rect.bottom = screen_height
      game_over = -1

    #returns gave over to be used later in code
    return game_over

#creates the world using the world list
#IN: the images and the list of tiles
class World():
  def __init__(self, data):
    self.tile_list = []

    row_count = 0
    for row in data:
      col_count = 0
      for tile in row:

        #creates dirt blocks
        if tile == 1:
          img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates grass blocks
        elif tile == 2:
          img = pygame.transform.scale(grass_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates grass version 2 blocks
        elif tile == 3:
          img = pygame.transform.scale(grass2_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates grass version 3 blocks
        elif tile == 4:
          img = pygame.transform.scale(grass3_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 4 blocks
        elif tile == 5:
          img = pygame.transform.scale(grass4_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates grass version 5 blocks
        elif tile == 6:
          img = pygame.transform.scale(grass5_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates grass version 6 blocks
        elif tile == 7:
          img = pygame.transform.scale(grass6_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 7 blocks
        elif tile == 8:
          img = pygame.transform.scale(grass7_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 8 blocks
        elif tile == 9:
          img = pygame.transform.scale(grass8_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 9 blocks
        elif tile == 10:
          img = pygame.transform.scale(grass9_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 10 blocks
        elif tile == 11:
          img = pygame.transform.scale(grass10_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 11 blocks
        elif tile == 12:
          img = pygame.transform.scale(grass11_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile) 

        #creates grass version 12 blocks
        elif tile == 13:
          img = pygame.transform.scale(grass12_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)

        #creates collectiable carrots
        elif tile == 14:
          carrot = Carrot(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
          carrot_group.add(carrot)

        #reates enemy mushrooms
        elif tile == 15:
          mushroom = Enemy(col_count * tile_size, row_count * tile_size + 7)
          mushroom_group.add(mushroom)
        
        col_count += 1
      row_count += 1

  #draws the character onto the screen
  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])

#creates muchrooms
#IN: the x and y coordinate
#OUT: a mushroom
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('mushroom.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

  #updates the mushroom every second to give it the look that it is moving
	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 30:
			self.move_direction *= -1
			self.move_counter *= -1

#creates a carrot
#IN:the x and y coordinate and size
#OUT:a collectible carrot
class Carrot(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load('carrot.png')
    self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

#holds all the data for this specific level. Each different number corresponds to a different tile/carrot/or mushroom.
world_data = [
[1, 11, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1, 1, 11, 4, 4, 4, 4, 4, 4, 4, 12],
[1, 3, 0, 0, 0, 0, 0, 0, 14, 14, 14, 14, 0, 0, 0, 0, 8, 4, 4, 4, 4, 7, 0, 0, 0, 0, 0, 0, 0, 5],
[1, 10, 6, 14, 14, 14, 0, 0, 9, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
[1, 1, 10, 2, 2, 6, 0, 0, 0, 0, 0, 3, 14, 14, 14, 0, 0, 0, 0, 0, 0, 0, 14, 14, 14, 14, 0, 0, 0, 5],
[1, 1, 11, 4, 4, 7, 0, 14, 14, 14, 0, 10, 2, 2, 6, 0, 14, 0, 15, 0, 14, 9, 2, 2, 2, 6, 0, 0, 14, 5],
[1, 1, 3, 0, 0, 0, 0, 9, 2, 6, 0, 0, 0, 0, 0, 0, 9, 2, 2, 2, 2, 13, 1, 1, 1, 3, 0, 0, 2, 13],
[11, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 12, 1, 1, 1, 1, 1, 3, 14, 0, 0, 5],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 14, 14, 0, 0, 0, 0, 8, 4, 4, 4, 12, 1, 10, 6, 0, 0, 5],
[3, 0, 0, 14, 14, 0, 0, 0, 14, 0, 15, 0, 9, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 7, 0, 0, 5],
[3, 0, 0, 9, 6, 0, 0, 0, 9, 2, 2, 2, 13, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 5],
[3, 0, 0, 5, 3, 0, 0, 9, 1, 1, 1, 11, 4, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 13],
[10, 2, 2, 13, 3, 0, 0, 0, 5, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
[1, 1, 1, 1, 3, 0, 14, 14, 5, 1, 1, 3, 14, 14, 14, 0, 0, 0, 0, 14, 14, 14, 0, 0, 14, 14, 0, 15, 0, 5],
[1, 1, 1, 1, 3, 0, 9, 2, 13, 1, 1, 10, 2, 2, 2, 2, 6, 0, 0, 9, 2, 6, 0, 0, 9, 2, 2, 2, 2, 13]]

#puts the player in the starting position (the spawn)
player = Player(37, screen_height - 130)

#groups the images for enemy class and carrot class
mushroom_group = pygame.sprite.Group()
carrot_group = pygame.sprite.Group()

#score_carrot = Carrot(tile_size // 2, tile_size // 2)
#carrot_group.add(score_carrot)

#creates the world
world = World(world_data)

#creates button instances
start_button = Button(350, 100, start_img, 1)
exit_button = Button(375, 350, exit_img, 1)
restart_img = Button(375, 350, instructions_img, 1)
instructions_button = Button(260, 225, instructions_img, 1)
back_button = Button(50, 375, back_img, 1)

#font that cant be put onto the screen
font = pygame.font.SysFont("arialblack", 45)
font2 = pygame.font.SysFont("arialblack", 18)

#draws the text onto the screen using the given font and size
#IN:the font and size
#OUT:text on the console
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#starts the while loop for the main game
run = True
while run:

  #fills the screen with a blue background
  screen.fill((52, 78, 91))
  
  #check if game has started, if not then display the menu and buttons
  if start_game == False:
    
    #check menu state
    if menu_state == "main":
      
      #draw the start button
      if start_button.draw(screen):
        
        #if clicked, start_game turns true, taking players to the game
        start_game = True
        
      #draw the instructions button
      if instructions_button.draw(screen):
        
        #if clicked, the menu state changes, taking players to a different screen
        menu_state = "instructions"
        
      #if player clicks exit, the program ends
      if exit_button.draw(screen):
        run = False
        
    #check if the instructions menu is open
    if menu_state == "instructions":
      
      #draw the text on
      draw_text("This is a very simple platformer-type game. Your objective", font, 'white', 50, 90)
      draw_text("is to collect all the carrots without dying to the enemy", font, 'white', 50, 130)
      draw_text("mushrooms. Each carrot is worth 5 points. The score of the", font, 'white', 50, 170)
      draw_text("player who collected the most carrots will be displayed in your", font, 'white', 50, 210)
      draw_text("level through the highscore text. If your score beat theirs,", font, 'white', 50, 250)
      draw_text("your score will be the new high score. Good luck! :D", font, 'white', 50, 290)

      #button to take players back to main menu
      if back_button.draw(screen):
        menu_state = "main"

  else:

    screen.blit(bg_img, (0, 0))
    world.draw()
    
    if game_over == 0:
      mushroom_group.update()
			#update score
			#check if a coin has been collected
      if pygame.sprite.spritecollide(player, carrot_group, True):
        score += 5
      draw_text('Score:' + str(score), font2, 'white', 15, 10)
      clock.tick(fps)
      draw_text('Highscore:' + str(high_score), font2, 'white', 15, 25)
      clock.tick(fps)
    
    mushroom_group.draw(screen)
    carrot_group.draw(screen)
      
    game_over = player.update(game_over)
    if score > high_score:
      high_score = score
      with open('score.txt', 'w') as file:
        file.write(str(high_score))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()