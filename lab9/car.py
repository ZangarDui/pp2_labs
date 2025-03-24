import pygame, sys
from pygame.locals import *
import random, time

# Pygame инициализациясы
pygame.init()

# FPS баптау
FPS = 60
FramePerSec = pygame.time.Clock()

# Түстер
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ойын айнымалылары
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Жинаған тиындар саны
N = 5  # N тиын жинағанда жау көлігінің жылдамдығы артады

# Шрифт баптау
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон жүктеу
background = pygame.image.load("lab8/AnimatedStreet.png")

# Экран жасау
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Жау көлігі (Enemy) класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Ойыншы (Player) класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Тиын (Coin) класы
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/coin.png")
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)  # Әртүрлі салмақтағы тиындар
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Спрайттар жасау        
P1 = Player()
E1 = Enemy()
coins_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

def spawn_coin():
    new_coin = Coin()
    coins_group.add(new_coin)
    all_sprites.add(new_coin)

# Бастапқы үш тиынды жасау
for _ in range(3):
    spawn_coin()

# Жылдамдықты арттыру оқиғасы
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Ойын циклы
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Фон салу
    DISPLAYSURF.blit(background, (0, 0))

    # Ұпайлар мен тиындар санын шығару
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (10, 40))
    
    # Барлық спрайттарды жылжыту
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    # Жау көлігімен соқтығысты тексеру
    if pygame.sprite.spritecollideany(P1, [E1]): # type: ignore
        pygame.mixer.Sound('lab8/crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Тиынмен соқтығысты тексеру
    for coin in coins_group:
        if pygame.sprite.collide_rect(P1, coin):
            COINS += coin.weight  # Тиынның салмағына байланысты ұпай қосу
            coin.kill()  # Тиынды жою
            spawn_coin()  # Жаңа тиынды пайда болдыру
            if COINS % N == 0:  # N тиын жинағанда жылдамдық артады
                SPEED += 1
    
    pygame.display.update()
    FramePerSec.tick(FPS)
