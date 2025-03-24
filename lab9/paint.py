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
mode = "brush"  # brush, rectangle, circle, square, right_triangle, equilateral_triangle, rhombus, eraser
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
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_y:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
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
            end_pos = event.pos
            
            if mode == "rectangle":
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]
                pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), 2)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            elif mode == "square":
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side), 2)
            elif mode == "right_triangle":
                points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif mode == "equilateral_triangle":
                side = abs(end_pos[0] - start_pos[0])
                height = (3 ** 0.5 / 2) * side
                points = [
                    (start_pos[0], start_pos[1] - height / 2),
                    (start_pos[0] - side / 2, start_pos[1] + height / 2),
                    (start_pos[0] + side / 2, start_pos[1] + height / 2)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif mode == "rhombus":
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                points = [
                    (start_pos[0], start_pos[1] - height // 2),
                    (start_pos[0] - width // 2, start_pos[1]),
                    (start_pos[0], start_pos[1] + height // 2),
                    (start_pos[0] + width // 2, start_pos[1])
                ]
                pygame.draw.polygon(screen, current_color, points, 2)
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
