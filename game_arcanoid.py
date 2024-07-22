import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


# Класс для платформы
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (WIDTH / 2) - (self.width / 2)
        self.y = HEIGHT - 30
        self.speed = 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))


# Класс для мячика
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.dx = 5 * random.choice([-1, 1])
        self.dy = -5

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Отражение от стен
        if self.x <= 0 or self.x >= WIDTH:
            self.dx = -self.dx
        if self.y <= 0:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def collide_with_paddle(self, paddle):
        if (self.y + self.radius >= paddle.y and
                paddle.x <= self.x <= paddle.x + paddle.width):
            self.dy = -self.dy

    def collide_with_block(self, block):
        if (block.x <= self.x <= block.x + block.width and
                block.y <= self.y <= block.y + block.height):
            self.dy = -self.dy
            return True
        return False


# Класс для блока
class Block:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.x = x
        self.y = y
        self.color = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# Создаем платформу, мяч и блоки
paddle = Paddle()
ball = Ball()
blocks = [Block(x * 70 + 35, y * 30 + 35) for x in range(10) for y in range(5)]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    ball.move()
    ball.collide_with_paddle(paddle)

    for block in blocks[:]:
        if ball.collide_with_block(block):
            blocks.remove(block)

    screen.fill(BLACK)
    paddle.draw(screen)
    ball.draw(screen)
    for block in blocks:
        block.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()