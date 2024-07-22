import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Пинг-Понг")

# Задание скорости обновления экрана
FPS = 60
clock = pygame.time.Clock()

# Классы для игры
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 10

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed # смещаем платформу в верх
        else:
            self.rect.y += self.speed # смещаем платформу в низ

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = 7
        self.speed_y = 7

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self):
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2
        self.speed_x *= -1

def display_score(screen, player1_score, player2_score):
    font = pygame.font.Font(None, 74)
    text = font.render(str(player1_score), True, WHITE)
    screen.blit(text, (WIDTH // 4, 10))
    text = font.render(str(player2_score), True, WHITE)
    screen.blit(text, (WIDTH * 3 // 4, 10))

def main():
    # Создание объектов
    paddle1 = Paddle(30, HEIGHT // 2 - 50)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
    ball = Ball(WIDTH // 2 - 7, HEIGHT // 2 - 7)

    player1_score = 0
    player2_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Управление первой ракеткой
        if keys[pygame.K_w] and paddle1.rect.top > 0:
            paddle1.move(up=True)
        if keys[pygame.K_s] and paddle1.rect.bottom < HEIGHT:
            paddle1.move(up=False)

        # Управление второй ракеткой
        if keys[pygame.K_UP] and paddle2.rect.top > 0:
            paddle2.move(up=True)
        if keys[pygame.K_DOWN] and paddle2.rect.bottom < HEIGHT:
            paddle2.move(up=False)

        # Движение мяча
        ball.move()

        # Проверка столкновений с верхней и нижней границами
        if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
            ball.speed_y *= -1

        # Проверка столкновений с ракетками
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        # Проверка выхода мяча за границы экрана
        if ball.rect.left <= 0:
            player2_score += 1
            ball.reset()
            time.sleep(3)  # Пауза на 3 секунды
        elif ball.rect.right >= WIDTH:
            player1_score += 1
            ball.reset()
            time.sleep(3)  # Пауза на 3 секунды

        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка объектов
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        # Отображение счета
        display_score(screen, player1_score, player2_score)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()