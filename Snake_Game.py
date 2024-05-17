import pygame
import random
from pygame.locals import *


pygame.init()
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (32,32,32)
green = (204, 0, 102)
yellow = (0, 255, 255)

win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

def user_score(score):
    number = score_font.render("Score: " + str(score), True, red)
    window.blit(number, [0, 0])

def game_snake(snake_block, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def message(msg):
    mesg = font_style.render(msg, True, red)
    window.blit(mesg, [win_width / 20, win_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            window.fill(grey)
            message("You Lost!! Press P to Play Again or Q to Quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == 0:  # Prevents reversing direction
                        x1_change = -snake_block
                        y1_change = 0
                if event.key == pygame.K_RIGHT:
                    if x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                if event.key == pygame.K_UP:
                    if y1_change == 0:
                        x1_change = 0
                        y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    if y1_change == 0:
                        x1_change = 0
                        y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_length_list.append(snake_head)
        
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for segment in snake_length_list[:-1]:
            if segment == snake_head:
                game_close = True

        game_snake(snake_block, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
