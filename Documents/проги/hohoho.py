import pygame
import random

# Инициализация
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Классическая Змейка")

# Цвета
BLUE = (0, 128, 255)
RED = (255, 0, 0)
DARK_GREY = (30, 30, 30)

# Параметры змейки
block_size = 20
x, y = WIDTH // 2, HEIGHT // 2  # Начальные координаты головы
dx, dy = 0, 0                   # Скорость (направление)
snake_body = []                 # Список всех сегментов тела
snake_length = 1                # Текущая длина

# Параметры яблока
apple_x = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
apple_y = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Управление направлением (чтобы двигалась сама)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -block_size, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = block_size, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -block_size
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, block_size

    # Движение головы
    x += dx
    y += dy

    # Проверка столкновения с границами
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        running = False

    # Логика тела
    snake_head = [x, y]
    snake_body.append(snake_head)
    
    # Удаляем лишние сегменты, чтобы змейка не росла сама по себе
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Проверка столкновения с самим собой
    for segment in snake_body[:-1]:
        if segment == snake_head:
            running = False

    # Проверка поедания яблока
    if x == apple_x and y == apple_y:
        apple_x = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
        apple_y = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0
        snake_length += 1

    # Отрисовка
    screen.fill(DARK_GREY)
    
    # Рисуем яблоко
    pygame.draw.rect(screen, RED, [apple_x, apple_y, block_size, block_size])
    
    # Рисуем всю змейку по кусочкам
    for segment in snake_body:
        pygame.draw.rect(screen, BLUE, [segment[0], segment[1], block_size, block_size])

    pygame.display.flip()
    clock.tick(15) # Скорость игры (для змейки лучше поменьше)

pygame.quit()