# import various module
import pygame
import random
import os

# initializing modules
pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
new_color = (240, 200, 200)
green = (0, 102, 0)
yellow = (255, 255, 0)
blue = (0,0,255)
aqua = (0,255,255)

# global variable
fps_r = 0
init_velocity_r = 0

#  Creating Window and its values
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background images for various with resize or scaled to game window
g_mode = pygame.image.load("game_mode.jpg")
g_mode = pygame.transform.scale(g_mode, (screen_width, screen_height)).convert_alpha()
bg_image = pygame.image.load("background.jpg")
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height)).convert_alpha()
snake_bg = pygame.image.load("snake.jpg")
snake_bg = pygame.transform.scale(snake_bg, (screen_width, screen_height)).convert_alpha()
play_game_i = pygame.image.load("Welcome.jpg")
play_game_i = pygame.transform.scale(play_game_i, (screen_width, screen_height)).convert_alpha()
game_over_i = pygame.image.load("game_over.jpg")
game_over_i = pygame.transform.scale(game_over_i, (screen_width, screen_height)).convert_alpha()
p_name_id = pygame.image.load("player_name.jpg")
p_name_id = pygame.transform.scale(p_name_id, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("CLASSIC SNAKE GAME V4.0 by Praveen Singh Chauhan")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):  # every time when we want to put text in screen we use this
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):  # snake
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def player_id():   # asking player name and process for rest game

    # local variables
    p_confirm = False
    name_exced = False
    blank_name = False
    space_count = 0

    if (os.path.exists("player_id.txt")):  # resetting player file to blank
        with open("player_id.txt", "w") as f:
            f.write("")

    while not p_confirm == True:  # if press Enter key it will over
        if (not os.path.exists("player_id.txt")):  # if Player file not exist it will make new one
            with open("player_id.txt", "w") as f:
                f.write("")
        with open("player_id.txt", "r") as f:  # reading file and storing in a variable
            player_name = f.read()
            # player name process here  as player enters his/her name
            p_name = str(player_name).upper()
            gameWindow.blit(p_name_id, (0, 0))
            str(p_name).replace("  ", " ")
            text_screen("[" + str(p_name) + "] " + str(len(player_name)), black, 100, 310)
            player_id.pname = p_name

            # spaces or blank name not allowed and its messages
            if space_count > 1:
                text_screen("Double Spaces not valid, Please Enter Again", red, 20, 500)
                space_count = 0
            if blank_name == True:
                text_screen("Empby Name is not valid, Enter Your Name ", red, 20, 500)
            if name_exced == True:
                text_screen("Enter Your Name Again", aqua, 50, 250)
            else:
                text_screen("Please Enter Your Name", aqua, 50, 250)
            if int(len(p_name)) > 21:
                text_screen("Name has to be less than 21 characters", red, 20, 500)
            player_id.p_n_len = int(len(p_name))


            for event in pygame.event.get():  # open pygame events and key press identify

                if event.type == pygame.QUIT:  # if click on check box to quit
                    quit()
                if event.type == pygame.KEYDOWN:  # if any key press it will start event
                    if event.key == pygame.K_ESCAPE: # if esc key pressed
                        quit()
                    # from a to z or 0 to 9 , if any key pressed it will acknoledge and return its value as player name
                    if event.key == pygame.K_a:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'a')
                    if event.key == pygame.K_b:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'b')
                    if event.key == pygame.K_c:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'c')
                    if event.key == pygame.K_d:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'd')
                    if event.key == pygame.K_e:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'e')
                    if event.key == pygame.K_f:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'f')
                    if event.key == pygame.K_g:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'g')
                    if event.key == pygame.K_h:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'h')
                    if event.key == pygame.K_i:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'i')
                    if event.key == pygame.K_j:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'j')
                    if event.key == pygame.K_k:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'k')
                    if event.key == pygame.K_l:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'l')
                    if event.key == pygame.K_m:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'm')
                    if event.key == pygame.K_n:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'n')
                    if event.key == pygame.K_o:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'o')
                    if event.key == pygame.K_p:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'p')
                    if event.key == pygame.K_q:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'q')
                    if event.key == pygame.K_r:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'r')
                    if event.key == pygame.K_s:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 's')
                    if event.key == pygame.K_t:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 't')
                    if event.key == pygame.K_u:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'u')
                    if event.key == pygame.K_v:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'v')
                    if event.key == pygame.K_w:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'w')
                    if event.key == pygame.K_x:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'x')
                    if event.key == pygame.K_y:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'y')
                    if event.key == pygame.K_z:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + 'z')
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '1')
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '2')
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '3')
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '4')
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '5')
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '6')
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '7')
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '8')
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '9')
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        with open("player_id.txt", "w") as f:
                            f.write(str(p_name) + '0')

                    if event.key == pygame.K_SPACE:  # if space bar pressed , it handle space bar action
                        space_count += 1
                        with open("player_id.txt", "w") as f:
                            if str(p_name) == " ":
                                space_count += 1
                            if space_count ==1:
                                space_count = 0
                                f.write(str(p_name) + ' ')
                            if space_count > 1:
                                space_count += 1

                    if event.key == pygame.K_RETURN: # when enter key pressed
                        if int(len(p_name)) < 5:
                            name_exced = True
                            if os.path.exists("player_id.txt"):
                                with open("player_id.txt", "w") as f:
                                    f.write("")
                        if str(p_name) == "" or str(p_name) == " " or str(p_name) == "  "  or str(p_name) == "    ":
                            blank_name = True
                        else:
                            welcome()

                    if event.key == pygame.K_BACKSPACE: # if backspace pressed it will handle that process
                        if os.path.exists("player_id.txt"):
                            with open("player_id.txt", "w") as f:
                                f.write("")

                    if int(len(p_name)) >= 22: # if player name is more than 23 character long , it checks here
                        name_exced = True
                        if os.path.exists("player_id.txt"):
                            with open("player_id.txt", "w") as f:
                                f.write("")

            # file close , and update display and clock set to 60
            f.close()
            pygame.display.update()
            clock.tick(60)


def gamemode():  # it lets player to play game in various mode (basically three mode)
    # variable
    exit_game = False
    n_width = 500

    gameWindow.blit(g_mode, (0, 0)) # game mode or play mode screen window

    # various checking to get right position of player name in game window
    if int(player_id.p_n_len) < 9:
        n_width = 500- (int(player_id.p_n_len))+80
    elif int(player_id.p_n_len) < 15 and int(player_id.p_n_len) > 9:
        n_width = 500- (int(player_id.p_n_len))+50
    elif int(player_id.p_n_len) > 15 and int(player_id.p_n_len) < 22:
        n_width = 500 - (int(player_id.p_n_len) * 6)
    text_screen(player_id.pname, green, n_width, 480)
    text_screen("P l a y e r ", white,580, 420)

    while not exit_game:  # loop to get right mode and exit
        # event call in
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.load('wrong-answer.mp3')
                pygame.mixer.music.play()
                exit_game = True
                quit()

            # mode selection for speed and fps and send player to play the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load('wrong-answer.mp3')
                    pygame.mixer.music.play()
                    exit_game = True
                    quit()
                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    gamemode.fps = 90
                    gamemode.velocity = 2
                    gameloop()
                elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    gamemode.fps = 90
                    gamemode.velocity = 4
                    gameloop()
                elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    gamemode.fps = 90
                    gamemode.velocity = 8
                    gameloop()

                    welcome()

        pygame.display.update()
        clock.tick(60)


def welcome():  # welcome window

    exit_game = False
    n_width = 300

    while not exit_game: # as previous mentioned

        gameWindow.blit(play_game_i, (0, 0))

        # to set player name in right position
        if int(player_id.p_n_len) < 9:
            n_width = 300 - (int(player_id.p_n_len)) + 60
        elif int(player_id.p_n_len) < 15 and int(player_id.p_n_len) > 9:
            n_width = 300 - (int(player_id.p_n_len)) + 25
        elif int(player_id.p_n_len) > 15 and int(player_id.p_n_len) < 22:
            n_width = 240 - int(player_id.p_n_len)
        text_screen(player_id.pname, green, n_width, 70)
        text_screen("Welcome", yellow, 380, 20)

        for event in pygame.event.get():  # various events called in
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load('wrong-answer.mp3')
                    pygame.mixer.music.play()
                    exit_game = True
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gamemode()

        pygame.display.update()
        clock.tick(60)


def gameloop():  # main game play goes here

    # various local variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # if file not exist it will make and store  hiscore in a variable
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        gameloop.hiscore = f.read()

    # making food for snake
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    gameloop.score = 0
    init_velocity = gamemode.velocity
    snake_size = 30
    fps = gamemode.fps

    while not exit_game:

        if game_over:  # we handle game over process here  and give score with personal message
            with open("hiscore.txt", "w") as f:
                f.write(str(gameloop.hiscore))
                gameWindow.blit(game_over_i,(0, 0))
                pygame.draw.rect(gameWindow, blue, [30, 35, 250, 60])
                pygame.draw.rect(gameWindow, green, [582, 35, 300, 60])
                text_screen("Score: " + str(gameloop.score) + " " *40 + "Hiscore: "+str(gameloop.hiscore), white, 50, 50)

                # player name position process
                if int(player_id.p_n_len) < 9:
                    n_width = 520
                elif int(player_id.p_n_len) < 15 and int(player_id.p_n_len) > 9:
                    n_width = 450
                elif int(player_id.p_n_len) > 15 and int(player_id.p_n_len) < 22:
                    n_width = 320
                text_screen(player_id.pname, white, n_width, 130)
                text_screen("Y o u r ", red, 550, 190)

            # various event call
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.load('wrong-answer.mp3')
                        pygame.mixer.music.play()
                        exit_game = True
                        quit()

                    if event.key == pygame.K_RETURN:  # if enter key pressed it will take back to welcome window to play again
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    quit()

                if event.type == pygame.KEYDOWN: # here we handle up, down, left and right key movement
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.load('wrong-answer.mp3')
                        pygame.mixer.music.play()
                        exit_game = True
                        quit()
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        gameloop.score +=10

            # snake speed and position
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:  # snake eats its food
                gameloop.score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

                if int(gameloop.score)>int(gameloop.hiscore):  # score and hiscore
                    gameloop.hiscore = gameloop.score

            # main game window message like score, hiscore and player name
            gameWindow.blit(bg_image,(0,0))
            text_screen("Score: " + str(gameloop.score) + "  Hiscore: "+str(gameloop.hiscore), red, 5, 5)
            text_screen("Player : "+ str(player_id.pname)+" ", red, 5,550)
            pygame.draw.rect(gameWindow, aqua, [food_x, food_y, snake_size, snake_size])

            # snake head making process
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            # controlling snake length
            if len(snk_list)>snk_length:
                del snk_list[0]

            # controlling snake movement in right way, not itself
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            # controlling if snake moves away from game window
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over = True

            # plotting snake with its variables
            plot_snake(gameWindow, white, snk_list, snake_size)

        # updating display and clock
        pygame.display.update()
        clock.tick(fps)
    # quit the game
    pygame.quit()
    quit()

player_id() # player name function runs from here to start the game
# Classic Snake Game code ends here
