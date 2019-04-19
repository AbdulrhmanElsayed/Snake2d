import pygame
import time
import random

#################
pygame.init()
pygame.display.set_caption("Snake")
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (155, 0, 0)
yellow = (200, 200, 0)
green = (34, 177, 76)
light_yellow = (255, 255, 0)
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()
intro = True
apple = pygame.image.load("Apple.png")
apple = pygame.transform.scale(apple, (15, 15))
pygame.mixer.music.load("next_eposide.mp3")
pygame.mixer.music.play()


####################################
def game_intro():
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Home_gm = menues()
        Home_gm.Picture("Back.jpg", -300, -200, 1100, 800)
        Home_gm.btn_menue(325, 200, 150, 50, "Play", black, 365, 208, yellow, light_yellow, which_button="Play")
        Home_gm.btn_menue(325, 300, 150, 50, "Mute", black, 355, 308, yellow, light_yellow, which_button="Mute")
        Home_gm.btn_menue(325, 400, 150, 50, "Exit", black, 365, 408, yellow, light_yellow, which_button="Exit")
        pygame.display.update()


#########################
def levels():
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Home_gm = menues()
        Home_gm.Picture("Back.jpg", -300, -200, 1100, 800)
        Home_gm.btn_menue(325, 200, 150, 50, "Easy", black, 360, 208, yellow, light_yellow, which_button="Easy")
        Home_gm.btn_menue(325, 300, 150, 50, "Meduim", black, 335, 308, yellow, light_yellow, which_button="Meduim")
        Home_gm.btn_menue(325, 400, 150, 50, "Hard", black, 360, 408, yellow, light_yellow, which_button="Hard")
        pygame.display.update()


#########################################
##################################################
def game_over_message(msg, color):
    font = pygame.font.SysFont(None, 37)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2 - 370, display_height / 2 + 200])


##################################################################################
def score_message(msg, score, color, x, y):
    screen_text = font.render(msg, True, color)
    screen_text2 = font.render(score, False, color)
    gameDisplay.blit(screen_text, [x, y])
    gameDisplay.blit(screen_text2, [x + 120, y])


####################################################
def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])


###########################################################################################
class menues():
    def Picture(self, photo, place_x, place_y, width, height):
        self.photo = photo
        self.height = height
        self.width = width
        self.place_x = place_x
        self.place_y = place_y
        background = pygame.image.load(photo)
        background = pygame.transform.scale(background, (width, height))
        gameDisplay.blit(background, [place_x, place_y])

    def btn_menue(self, btn_x, btn_y, btn_width, btn_height, Text, txt_color, txt_x, txt_y, color, light_color,
                  which_button):
        self.btn_x = btn_x
        self.btn_y = btn_y
        self.btn_width = btn_width
        self.btn_height = btn_height
        self.Text = Text
        self.txt_x = txt_x
        self.txt_y = txt_y
        self.color = color
        self.light_color = light_color  #######
        screen_text = font.render(Text, True, txt_color)
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if btn_x + btn_width > mouse_position[0] > btn_x and btn_y + btn_height > mouse_position[1] > btn_y:
            pygame.draw.rect(gameDisplay, light_color, (btn_x, btn_y, btn_width, btn_height))
            if click[0] == 1:
                if which_button == "Play":
                    time.sleep(0.1)
                    levels()
                if which_button == "Mute":
                    pygame.mixer.music.stop()
                if which_button == "Easy":
                    game_loop(20)
                if which_button == "Meduim":
                    game_loop(35)
                if which_button == "Hard":
                    game_loop(40)
                if which_button == "Home":
                    time.sleep(0.1)
                    game_intro()
                if which_button == "Exit":
                    pygame.quit()
                    quit()
                if which_button == "Save Score":
                    add()
        else:
            pygame.draw.rect(gameDisplay, color, (btn_x, btn_y, btn_width, btn_height))

        gameDisplay.blit(screen_text, [txt_x, txt_y])


#################################################################################################################################
#########################################################################################
def game_loop(fbs):
    pygame.mixer.music.load('Game_over_sound.mp3')
    pygame.mixer.music.load('lose_sound.mp3')
    clock = pygame.time.Clock()
    apples = 0
    score = 0
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    block_size = 10  ##Each block of the snake
    background = pygame.image.load("Back.jpg")
    background = pygame.transform.scale(background, (1200, 800))
    sad_snake = pygame.image.load("Sad_snake.png")
    sad_snake = pygame.transform.scale(sad_snake, (500, 300))
    apple = pygame.image.load("Apple.png")
    apple = pygame.transform.scale(apple, (15, 15))
    big_apple = pygame.image.load("Apple.png")
    big_apple = pygame.transform.scale(big_apple, (30, 30))
    rand_x = random.randrange(block_size * 3, display_width - 3 * block_size)
    rand_y = random.randrange(block_size * 3, display_height - 3 * block_size)
    snake_list = []
    snake_len = 1
    while not gameExit:

        while gameOver == True:
            background = pygame.transform.scale(background, (1200, 800))
            gameDisplay.blit(background, [0, 0])
            gameDisplay.blit(sad_snake, [180, 50])
            score_message("Score :  ", str(score), red, 300, 400)
            game_over_message("Game over!, please Register your Name and Level and Score ", red)
            mouse_position = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            Home_gm = menues()
            Home_gm.btn_menue(310, 530, 185, 50, "Save Score", black, 310, 530, yellow, light_yellow,
                              which_button="Save Score")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_BACKSPACE:
                        pygame.mixer.music.stop()
                        gameOver = False
                        gameExit = True
                        game_intro()
                        score = 0
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

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if snake_len < len(snake_list):
            del snake_list[0]
        for each_block in snake_list[:-1]:
            if each_block == snake_head:
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.play()
                gameOver = True

        snake(block_size, snake_list)
        if (gameExit == True):
            pygame.quit()
            quit()
        else:
            score_message("Score: ", str(score), white, 630, 550)

        clock.tick(fbs)

        if lead_x >= display_width - 5 or lead_x <= 0 or lead_y >= display_height - 5 or lead_y <= 0:
            pygame.mixer.music.load('lose_sound.mp3')
            pygame.mixer.music.play()
            time.sleep(2)
            pygame.mixer.music.load('Game_over_sound.mp3')
            pygame.mixer.music.play()
            gameOver = True

        if apples % 5 == 0 and apples != 0:
            gameDisplay.blit(big_apple, [rand_x, rand_y])
            if lead_x <= rand_x + 26 and lead_x >= rand_x - 20 and lead_y <= rand_y + 26 and lead_y >= rand_y - 20:
                pygame.mixer.music.load('Eating.mp3')
                pygame.mixer.music.play(0)
                rand_x = random.randrange(block_size * 3, display_width - 3 * block_size)
                rand_y = random.randrange(block_size * 3, display_height - 3 * block_size)
                snake_len += 5
                score += 5
                apples = 0
        else:
            gameDisplay.blit(apple, [rand_x, rand_y])
            if lead_x <= rand_x + 13 and lead_x >= rand_x - 10 and lead_y <= rand_y + 13 and lead_y >= rand_y - 10:
                pygame.mixer.music.load('Eating.mp3')
                pygame.mixer.music.play(0)
                rand_x = random.randrange(block_size * 3, display_width - 3 * block_size)
                rand_y = random.randrange(block_size * 3, display_height - 3 * block_size)
                apples += 1
                snake_len += 1
                score += 1

        pygame.display.update()


###################################################################
def add():
    input_file = open("name.txt", "a")
    name = input("enter your username: ")
    level = input("enter your level: ")
    score = input("enter your score: ")
    print(name, file=raw_input()file)
    print(level, file=raw_input_file)
    print(score, file=raw
    _input_file)
    input_file.close()
    answer = input("would you like continue playing: ")
    if answer == 'yes':
        print("Enjoy with our game")
        game_intro()
    if answer == 'no':
        pygame.quit()
        quit()
    ##########################################################################
    pygame.quit()
    quit()


game_intro()




