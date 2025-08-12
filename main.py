# Imports pygame and other things needed and initiliazises the pygame 
import pygame
from random import randint
from time import sleep
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        #self.x = 400
        self.sprite = pygame.image.load('./graphics/rocket.png')
        self.rect = self.sprite.get_rect(midbottom=(400, 825))
    
    # This adds the player sprite to the screen
    def add_sprite(self):
        screen.blit(self.sprite, self.rect)

    # This allows the player to move left and right with the arrow keys
    def controls_and_movement(self):
        screen.fill('#5868a8')
        self.add_sprite()
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.x >= 895:
            self.rect.x = 0
        elif self.rect.x <= -5:
            self.rect.x = 895

class Bullet(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprite = pygame.image.load('./graphics/bullet.png')
        self.y = 630
        self.rect = self.sprite.get_rect(midbottom=(my_player.rect.x+115, self.y))

    # This adds the bullet sprite to the screen
    def add_sprite(self):
        self.rect = self.sprite.get_rect(midbottom=(my_player.rect.x+115, self.y))
        screen.blit(self.sprite, self.rect)

    # This resets the bullet position
    def reset_bullet(self):
        self.y = 630

    # This checks if the bullet goes of screen
    def check_reset_bullet(self):
        if self.y == 0: self.reset_bullet()

    # This shoots a bullet after the player presses the space bar
    def check_shoot_bullet(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.add_sprite()
            self.y -= 10
        
class Enemies(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprite = pygame.image.load('./graphics/enemy.png')
        self.rect = self.sprite.get_rect(center=(100,20))
        self.collision = None     

    # This adds the enemy sprite
    def add_sprite(self):
        screen.blit(self.sprite, self.rect)
        #print(self.rect)

    def movement(self):
        self.rect.y += 5
        #print(self.rect.y)
        if self.rect.y == 800: 
            self.rect.y = 0

    def detect_collision(self):
        if self.rect.colliderect(my_bullet.rect):
            #print('collision detected')
            self.collision = True
        else:
            #print('No collision')
            self.collision = False

class Events(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.font = pygame.font.Font('./game_font.ttf', 25)
        self.score = 0
        self.lives = 4
        #self.score_board = self.font.render(f'Score: {self.score}', False, 'white')

    # This detects if the player hits the enemy and changes the enemy's position
    def collision_reaction(self):
        if my_enemies.collision:
            self.score += 1
            my_bullet.reset_bullet()
            my_enemies.rect.y = 0
            my_enemies.rect.x = randint(10,790)

    def detect_live_loss(self):
        global game_active
        if my_enemies.rect.y == 795:
            self.lives -= 1
            if self.lives < 0: 
                self.lives = 0
                game_active = False

    # This adds the score board to the top of the screen
    def add_score_board(self):
        score_board = self.font.render(f'Score: {self.score}', False, 'white')
        screen.blit(score_board,(400,10))

    # This adds the live counter to the top of the screen
    def add_live_counter(self):
        live_counter = self.font.render(f'Lives: {self.lives}', False, 'white')
        screen.blit(live_counter,(400,35))

    # This shows the game over screen 
    def game_over(self):
        global game_active
        game_over_text = self.font.render('Game Over', False, 'white')
        restart_text = self.font.render('Press enter to restart', False, 'white')
        screen.blit(game_over_text,(365,400))
        screen.blit(restart_text,(365,425))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            print('key press detected')
            game_active = True
            self.lives = 4

    # This starts the game if the player presses enter
    def start_game(self):
        global game_active
        start_game_text = self.font.render('Press enter to start the game', False, 'white')
        screen.blit(start_game_text,(300,400))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_active = True
       
# Creates the pygame window
screen = pygame.display.set_mode((900,830))
pygame.display.set_caption('Space Shooter')
screen.fill('#5868a8')

# Creates an instance of every class needed for the game to work 
# and creates the game_active variable which checks if the game is active
game_active = False
my_player = Player()
my_bullet = Bullet()
my_enemies = Enemies()
my_events = Events()
clock = pygame.time.Clock()

# The game loop
while True:
    # Lets the player exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        #if event.type == pygame.MOUSEMOTION: print(event.pos)

    if game_active:
        my_player.add_sprite()
        my_player.controls_and_movement()
        my_bullet.check_reset_bullet()
        my_bullet.check_shoot_bullet()
        my_enemies.add_sprite()
        my_enemies.detect_collision()
        my_enemies.movement()
        my_events.collision_reaction()
        my_events.detect_live_loss()
        my_events.add_score_board()
        my_events.add_live_counter()
    else: 
        if my_events.lives == 0:
            my_events.game_over()
        else: 
            my_events.start_game()

    clock.tick(90)
    pygame.display.update()
