import pygame


pygame.init()

screen_width = 1550
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 50)

x,y = 450, 100
x1,y1 = 450, 50
x2,y2 = 450, 0
speed = 1
h = 15
apple = pygame.image.load('img/яблоко.jpg')
apple = pygame.transform.scale(apple, (100, 100))

главны игрок = pygame.image.load('img/банан.jpg')
banana = pygame.transform.scale(banana, (100, 100))

forest = pygame.image.load('img/лесок.jpg')
forest = pygame.transform.scale(forest, (1550, 800)

пулья = pygame.image.load('img/istockphoto-120492078-612x612.jpg')
Shailushai = pygame.transform.scale(Shailushai, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and y<500-h:             #кнопка вниз
        y += speed
    if keys[pygame.K_UP] and y>0:             #кнопка вверх
        y -= speed
    if keys[pygame.K_LEFT] and x>0:             #кнопка влево
        x -= speed
    if keys[pygame.K_RIGHT] and x<1300-h:             #кнопка вправо
        x += speed



    screen.blit(forest, (0, 0))
    text = font.render("banana cat ", True, (255,255,0))
    screen.blit(text, (x, y))
    text2 = font2.render("VS", True, (255,255,255))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("apple cat", True, (230,0,0))
    screen.blit(textadsf, (x2, y2))
    screen.blit(apple, (10, 50))
    screen.blit(banana, (x, y))

    pygame.display.update()