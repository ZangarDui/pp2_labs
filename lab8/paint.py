import pygame
import sys

# Pygame инициализациясы
pygame.init()

# Экран параметрлері
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Айнымалылар
current_color = BLACK
brush_size = 5
mode = "brush"  # brush, rectangle, circle, eraser
start_pos = None

# Бастапқы фон
screen.fill(WHITE)

# Негізгі цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle":
                end_pos = event.pos
                width = end_pos[0] - start_pos[0] # type: ignore
                height = end_pos[1] - start_pos[1]
                pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), 2)
            elif mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
    
    pygame.display.flip()

pygame.quit()
sys.exit()