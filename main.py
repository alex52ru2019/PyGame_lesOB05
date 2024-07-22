import pygame
import random
pygame.init()

windows_size = (800, 600)
screen = pygame.display.set_mode(windows_size) # размеры окна
pygame.display.set_caption("Тестовый проект") # название окна
image1 = pygame.image.load("img/image.png") # картинка
image2 = pygame.image.load("img/klubnika.png") # картинка
image_rect1 = image1.get_rect() # прямоугольник картинки 1
image_rect2 = image2.get_rect() # прямоугольник картинки 2

speed = 5

run = True
while run:
    for event in pygame.event.get(): # обработка событий
        if event.type == pygame.QUIT: # если нажали на крестик
            run = False # завершаем цикл
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX
            image_rect1.y = mouseY

    if image_rect1.colliderect(image_rect2):
        image_rect2.x = random.randint(0, 800)
        image_rect2.y = random.randint(0, 600)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()
