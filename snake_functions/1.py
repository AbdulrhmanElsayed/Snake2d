import pygame
import time
import random

pygame.init()

background = pygame.image.load("Back.jpg")
background = pygame.transform.scale(background, (1100, 800))
sad_snake = pygame.image.load("Sad_snake.png")
sad_snake = pygame.transform.scale(sad_snake, (500, 300))
white = (255, 255, 255)
black = (0, 0, 0)
red = (155, 0, 0)
yellow = (200, 200, 0)
green = (34, 177, 76)
light_yellow = (255, 255, 0)
display_width = 800
display_height = 600
pygame.display.set_caption("Snake")
gameDisplay = pygame.display.set_mode((display_width, display_height))
font = pygame.font.SysFont(None, 50)


intro = True


def game_over_message(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2 - 350, display_height / 2 + 200])


def score_message(msg, score, color, x, y):
    screen_text = font.render(msg, True, color)
    screen_text2 = font.render(score, False, color)
    gameDisplay.blit(screen_text, [x, y])
    gameDisplay.blit(screen_text2, [x+120, y])


def txt_btn(txt, color, x, y):
    screen_text = font.render(txt, True, color)
    gameDisplay.blit(screen_text, [x, y])


def main_buttons(x, y, width, height, color, light_color, which_button):
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse_position[0] > x and y + height > mouse_position[1] > y:
        pygame.draw.rect(gameDisplay, light_color, (x, y, width, height))
        if click[0] == 1:
            if which_button == "Play":
                time.sleep(0.1)
                game_levels()
            if which_button == "Music":
                pass
            if which_button == "Exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, color, (x, y, width, height))


def level_buttons(x, y, width, height, color, light_color, which_button):
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse_position[0] > x and y + height > mouse_position[1] > y:
        pygame.draw.rect(gameDisplay, light_color, (x, y, width, height))
        if click[0] == 1:
            if which_button == "Easy":
                game_loop(20)
            if which_button == "Medium":
                game_loop(30)
            if which_button == "Hard":
                game_loop(50)
    else:
        pygame.draw.rect(gameDisplay, color, (x, y, width, height))


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background, [-300, -200])
        main_buttons(325, 200, 150, 50, yellow, light_yellow, which_button="Play")
        main_buttons(325, 300, 150, 50, yellow, light_yellow, which_button="Music")
        main_buttons(325, 400, 150, 50, yellow, light_yellow, which_button="Exit")
        txt_btn("Play", black, 365, 208)
        txt_btn("Music", black, 355, 308)
        txt_btn("Exit", black, 365, 408)
        pygame.display.update()


def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])


def game_levels():
    levels = True
    while levels:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(background, [-300, -200])
        level_buttons(325, 200, 150, 50, yellow, light_yellow, which_button="Easy")
        level_buttons(325, 300, 150, 50, yellow, light_yellow, which_button="Medium")
        level_buttons(325, 400, 150, 50, yellow, light_yellow, which_button="Hard")
        txt_btn("Easy", black, 365, 208)
        txt_btn("Medium", black, 338, 308)
        txt_btn("Hard", black, 365, 408)
        pygame.display.update()


def game_loop(fbs):
    #pygame.mixer.music.load('Game_over_sound.mp3')
    clock = pygame.time.Clock()
    score = 0
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    block_size = 10
    background = pygame.image.load("Back.jpg")
    background = pygame.transform.scale(background, (1200, 800))
    sad_snake = pygame.image.load("Sad_snake.png")
    sad_snake = pygame.transform.scale(sad_snake, (500, 300))
    apple = pygame.image.load("Apple.png")
    apple = pygame.transform.scale(apple, (15, 15))
    rand_x = random.randrange(block_size * 3, display_width - 3 * block_size)
    rand_y = random.randrange(block_size * 3, display_height - 3 * block_size)
    snake_list = []
    snake_len = 1
    while not gameExit:

        while gameOver == True:
            background = pygame.transform.scale(background, (1200, 800))
            gameDisplay.blit(background, [0, 0])
            gameDisplay.blit(sad_snake, [180, 50])
            score_message("Score :  ", str(score),  red, 300, 400)
            game_over_message("Game over! , press Q to quit or R to restart ", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameOver = False
                        gameExit = False
                        pygame.mixer.music.stop()
                        pygame.mixer.pause()
                        lead_x = display_width / 2
                        lead_y = display_height / 2
                        lead_x_change = 0
                        lead_y_change = 0
                        rand_x = random.randrange(0, display_width - block_size)
                        rand_y = random.randrange(0, display_height - block_size)
                        snake_list = []
                        snake_len = 1
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change == 0:
                    lead_x_change -= 11
                    lead_y_change = 0
                    break
                if event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change += 11
                    lead_y_change = 0
                    break
                if event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change -= 11
                    lead_x_change = 0
                    break
                if event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change += 11
                    lead_x_change = 0
                    break

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(background, [0, 0])

        gameDisplay.blit(apple, [rand_x, rand_y])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if snake_len < len(snake_list):
            del snake_list[0]
        for each_block in snake_list[:-1]:
            if each_block == snake_head:
                #pygame.mixer.music.load('Game_over_sound.mp3')
                #pygame.mixer.music.play(0)
                gameOver = True
        snake(block_size, snake_list)
        if (gameExit == True):
            pygame.quit()
            quit()
        else:
            score_message("Score: ", str(score), white, 630, 550)
            pygame.display.update()
        clock.tick(fbs)

        if lead_x >= display_width - 2*block_size or lead_x <= 0 or lead_y >= display_height - 2*block_size or lead_y <= 0:
           # pygame.mixer.music.load('Game_over_sound.mp3')
            #pygame.mixer.music.play(0)
            gameOver = True

        if lead_x <= rand_x + 10 and lead_x >= rand_x - 10 and lead_y <= rand_y + 10 and lead_y >= rand_y - 10:
            #pygame.mixer.music.load('Eating.mp3')
            #pygame.mixer.music.play(0)
            rand_x = random.randrange(block_size * 3, display_width - 3 * block_size)
            rand_y = random.randrange(block_size * 3, display_height - 3 * block_size)
            snake_len += 1
            score += 1

    pygame.quit()
    quit()


game_intro()
# game_loop()
