# Imports pygame and initiliazises the pygame 
import pygame 
pygame.init()

class Rocket(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__()
        #self.x = 400
        self.sprite = pygame.image.load('./graphics/rocket.png')
        self.rect = self.sprite.get_rect(midbottom=(400, 825))
        #self.bullet_sprite = pygame.image.load('graphics/bullet.png')
        
    def add_sprite(self):
        screen.blit(self.sprite, self.rect)

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
        self.rect = self.sprite.get_rect(midbottom=(my_rocket.rect.x+115, self.y))

    def add_sprite(self):
        self.rect = self.sprite.get_rect(midbottom=(my_rocket.rect.x+115, self.y))
        screen.blit(self.sprite, self.rect)
        return self.rect

    def reset_bullet(self):
        if self.y == 0:
            self.y = 630

    def check_shoot_bullet(self):
        #space_down = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.add_sprite()
            self.y -= 10
        
class Enemies(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprite = pygame.image.load('./graphics/enemy.png')
        self.x = 200
        self.rect = self.sprite.get_rect(midbottom=(200,100))

    def add_sprite(self):
        #self.rect = self.sprite.get_rect(midbottom=(self.x,100))
        screen.blit(self.sprite, self.rect)

    def movement(self): 
        #self.add_sprite()
        
        if self.rect.x == 895: 
            self.rect.x = 200
            print('point reset')
        self.rect.x += 5

    def detect_collision(self):
        if self.rect.colliderect(my_bullet.rect):
            print('You hit him')

       
# Creates the pygame window
screen = pygame.display.set_mode((900,800))
pygame.display.set_caption('pygame Template')
screen.fill('#5868a8')

# Creates an instance of every class needed for the game to work
enenmy_sprite = pygame.image.load('./graphics/enemy.png').convert_alpha()
my_rocket = Rocket()
my_bullet = Bullet()
my_enemies = Enemies()
clock = pygame.time.Clock()

# Keeps the window from closing until the user exits
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        #if event.type == pygame.MOUSEMOTION: print(event.pos)

    my_rocket.add_sprite()
    my_rocket.controls_and_movement()
    my_bullet.reset_bullet()
    my_bullet.check_shoot_bullet()
    my_enemies.add_sprite()
    my_enemies.detect_collision()
    my_enemies.movement()

    clock.tick(90)
    pygame.display.update()


#pygame.quit()