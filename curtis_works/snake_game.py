#import
import pygame
import time
import random

#screen
window_x = 720
window_y = 480

#colors
black = pygame.Color(0, 0, 0)
light_blue = pygame.Color(153, 204, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)

#functions
def fpos(x):
    x = x // 10
    x = x * 10

#variables 
score = 0
snake_speed = 15
    
fruit_position = [[random.randrange(1, fpos(window_x)), random.randrange(1, fpos(window_y))], [random.randrange(1, fpos(window_x)), random.randrange(1, fpos(window_y))]]
fruit_spawn = [True, True]

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render("Your Score is: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    time.sleep(2)
    pygame.quit()
    quit()

#game
pygame.init()

pygame.display.set_caption("snek game ;)")
game_window = pygame.display.set_mode((window_x,window_y))

fps = pygame.time.Clock()

#snakepos
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

direction = "RIGHT"
change_to = direction


while True:
    if fruit_position[1] == fruit_position[0]:
        fruit_position[1] = [random.randrange(1, fpos(window_x)), random.randrange(1, fpos(window_y))]

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
        
        # +y <-> -y +x <-> -x
    if direction == "UP": 
        snake_position[1] -= 10
    if direction == "DOWN": 
        snake_position[1] += 10
    if direction == "LEFT": 
        snake_position[0] -= 10
    if direction == "RIGHT": 
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score+=10
        fruit_spawn[0] = False
    elif snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score+=10
        fruit_spawn[1] = False
    else:
        snake_body.pop

    if not fruit_spawn[0]:
        fruit_position = [random.randrange(1, fpos(window_x)), random.randrange(1, fpos(window_y))]
        fruit_spawn[0] = True
    if not fruit_spawn[1]:
        fruit_position = [random.randrange(1, fpos(window_x)), random.randrange(1, fpos(window_y))]
        fruit_spawn[1] = True
    game_window.fill(black)

    #refer to snakepos
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(int(fruit_position[0][0]), int(fruit_position[0][1]), 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(int(fruit_position[1][0]), int(fruit_position[1][1]), 10, 10))

    #refer to game over: conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
        
    #display
    show_score(1, white, "times new roman", 20)
    pygame.display.update()
    fps.tick(snake_speed)
