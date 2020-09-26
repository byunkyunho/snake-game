import time
import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((1000, 800))

pg.key.set_repeat(1, 1)

def draw_background():
    screen.fill((255,255,255))
    for rect in range(25):
        pg.draw.rect(screen, (0,0,0), (rect*40,0, 39,39 ))
        pg.draw.rect(screen, (0,0,0), (rect*40,760, 39,39))
    for rect in range(18):
        pg.draw.rect(screen, (0,0,0),(0,40 + rect*40, 39,39 ) )
        pg.draw.rect(screen, (0,0,0),(960,40 + rect*40, 39,39 ) )

def set_game():
    global direction, snake_list, set_time, set_point_, score, change_direction
    direction = "left"
    snake_list = [[7, 10],[8, 10],[9, 10]]
    set_time = True
    set_point_ = True
    score = 0
    change_direction = True

def set_point():
    global random_x, random_y
    okay = True
    while True:
        random_point = [random.randint(1, 23), random.randint(1, 18)]
        for a in snake_list:
            if a == random_point:
                okay == False
            else:
                random_x, random_y = random_point
        if okay:
            break

def draw_text(text, font_size, x, y):
    draw_text_font = pg.font.SysFont("malgungothic", font_size)
    draw_text_text = draw_text_font.render(text, True, (0,0,0))
    screen.blit(draw_text_text, (x, y))

intro = True
game = True
running = True

while running:
    while intro:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                intro = False
            if event.type == pg.QUIT:
                game = False
                running = False
                intro = False
        screen.fill((255,255,255))
        draw_text("Press Any Key To Start", 80, 96, 242)
        pg.display.update()
    set_game()
    if running:
        game = True
    else:
        game = False
    while game:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if change_direction:
                    if event.key == pg.K_DOWN and not direction == "up":
                        direction = "down"
                        change_direction = False
                    if event.key == pg.K_UP and not direction == "down":
                        direction = "up"
                        change_direction = False
                    if event.key == pg.K_LEFT and not direction == "right":
                        direction = "left"
                        change_direction = False
                    if event.key == pg.K_RIGHT and not direction == "left":
                        direction = "right"
                        change_direction = False

            if event.type == pg.QUIT:
                game = False
                running = False

        draw_background()

        if set_point_:
            set_point()
            set_point_ = False

        pg.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random_x*40, random_y*40,39,39) )

        for a in snake_list[1:]:
            if snake_list[0] == a:
                game = False
        if snake_list[0][0] < 1 or snake_list[0][0] > 24 or snake_list[0][1] < 1 or snake_list[0][1] > 18:
            game = False

            
        if set_time:
            change_direction = True
            a_time = time.time()
            set_time = False

        if time.time() - a_time > 0.5:
            a,b = snake_list[0]
            snake_list.insert(0, [a, b])
            if direction == "left":
                snake_list[0][0] -= 1
            if direction == "right":
                snake_list[0][0] += 1
            if direction == "up":
                snake_list[0][1] -= 1
            if direction == "down":
                snake_list[0][1] += 1
            if snake_list[0] == [random_x, random_y]:
                set_point_ = True
                score += 1
            else:
                snake_list.remove(snake_list[-1])
            set_time  = True
        for snake in enumerate(snake_list):
            if snake[0] == 0:
                pg.draw.rect(screen, (255,0,0), (snake[1][0]*40,snake[1][1]*40, 39, 39))
            else:
                pg.draw.rect(screen, (78, 37, 35), (snake[1][0]*40,snake[1][1]*40, 39, 39))
        pg.display.update()
    if running:
        end = True
    else:
        end = False
    while end:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                end = False
            if event.type == pg.QUIT:
                end = False
                running = False
        screen.fill((255,255,255))
        draw_text("Score : {}".format(score), 120,258, 188)
        draw_text("Press Any Key To Start", 50, 258, 388)
        pg.display.update()
