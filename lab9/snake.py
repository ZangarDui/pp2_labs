import pygame
import random
import sys

# Pygame инициализациясы
pygame.init()

# Экран өлшемдері
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20  # Жыланның және тамақтың өлшемі

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Экран жасау
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# FPS және жылдамдық
clock = pygame.time.Clock()
speed = 5

# Жылан параметрлері
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (BLOCK_SIZE, 0)

# Бастапқы ұпай мен деңгей
score = 0
level = 1

# Тамақ және таймер
food = None
food_timer = 0
food_weight = 1

# Тамақ генерациялау функциясы
def generate_food():
    global food_timer, food_weight
    while True:
        new_food = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                    random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
        if new_food not in snake:
            food_timer = pygame.time.get_ticks()  # Тамақтың таймерін бастау
            food_weight = random.randint(1, 3)  # Тамақтың салмағын кездейсоқ орнату
            return new_food

food = generate_food()

def game_over():
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 20))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Негізгі ойын циклы
running = True
while running:
    screen.fill(BLACK)
    
    # Оқиғаларды өңдеу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                snake_dir = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                snake_dir = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                snake_dir = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                snake_dir = (BLOCK_SIZE, 0)
    
    # Жыланды жылжыту
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Қабырғаға соғылу тексеру
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
        game_over()
    
    # Өз денесіне соғылу тексеру
    if new_head in snake:
        game_over()
    
    snake.insert(0, new_head)
    
    # Жемісті жегенін тексеру
    if new_head == food:
        score += food_weight  # Тамақтың салмағына байланысты ұпай қосу
        food = generate_food()
        
        # Деңгейді жоғарылату (әр 5 ұпай сайын)
        if score % 5 == 0:
            level += 1
            speed += 2  # Жылдамдықты арттыру
    else:
        snake.pop()
    
    # Тамақтың жоғалып кету уақытын тексеру (5 секундтан кейін жоғалады)
    if pygame.time.get_ticks() - food_timer > 5000:
        food = generate_food()
    
    # Жыланды салу
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Тамақты салу
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Ұпай және деңгей көрсету
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.flip()
    clock.tick(speed)
