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
u_name_id = pygame.image.load("user_name.jpg")
u_name_id = pygame.transform.scale(u_name_id, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SNAKE V2.1 by Praveen Singh Chauhan")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def user_id():
    u_confirm = False

    if os.path.exists("user_id.txt"):
        os.remove("user_id.txt")

    while not u_confirm == True:
        if (not os.path.exists("user_id.txt")):
            with open("user_id.txt", "w") as f:
                f.write(" ")

        with open("user_id.txt", "r") as f:
            user_name = f.read()
            u_name = str(user_name).upper()
            gameWindow.blit(u_name_id, (0, 0))
            # text_screen("Welcome  '", red, 70, 310)
            text_screen("'"+str(u_name) + "'", black, 100, 310)
            user_id.uname = u_name

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_a:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'a')
                    if event.key == pygame.K_b:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'b')
                    if event.key == pygame.K_c:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'c')
                    if event.key == pygame.K_d:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'd')
                    if event.key == pygame.K_e:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'e')
                    if event.key == pygame.K_f:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'f')
                    if event.key == pygame.K_g:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'g')
                    if event.key == pygame.K_h:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'h')
                    if event.key == pygame.K_i:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'i')
                    if event.key == pygame.K_j:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'j')
                    if event.key == pygame.K_k:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'k')
                    if event.key == pygame.K_l:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'l')
                    if event.key == pygame.K_m:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'm')
                    if event.key == pygame.K_n:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'n')
                    if event.key == pygame.K_o:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'o')
                    if event.key == pygame.K_p:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'p')
                    if event.key == pygame.K_q:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'q')
                    if event.key == pygame.K_r:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'r')
                    if event.key == pygame.K_s:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 's')
                    if event.key == pygame.K_t:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 't')
                    if event.key == pygame.K_u:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'u')
                    if event.key == pygame.K_v:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'v')
                    if event.key == pygame.K_w:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'w')
                    if event.key == pygame.K_x:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'x')
                    if event.key == pygame.K_y:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'y')
                    if event.key == pygame.K_z:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + 'z')
                    if event.key == pygame.K_SPACE:
                        with open("user_id.txt", "w") as f:
                            f.write(str(u_name) + ' ')
                    if event.key == pygame.K_RETURN:
                        welcome()
                    if event.key == pygame.K_BACKSPACE:
                        f.close()
                        if os.path.exists("user_id.txt"):
                            os.remove("user_id.txt")
                        if (not os.path.exists("user_id.txt")):
                            with open("user_id.txt", "w") as f:
                                f.write(" ")

            f.close()
            pygame.display.update()
            clock.tick(60)


def gamemode():
    exit_game = False

    gameWindow.blit(g_mode, (0, 0))
    text_screen(user_id.uname, green,300, 500)

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.load('wrong-answer.mp3')
                pygame.mixer.music.play()
                exit_game = True
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load('wrong-answer.mp3')
                    pygame.mixer.music.play()
                    exit_game = True
                    quit()
                if event.key == pygame.K_KP1:
                    gamemode.fps = 90
                    gamemode.velocity = 2
                    gameloop()
                elif event.key == pygame.K_KP2:
                    gamemode.fps = 90
                    gamemode.velocity = 6
                    gameloop()
                elif event.key == pygame.K_KP3:
                    gamemode.fps = 90
                    gamemode.velocity = 8
                    gameloop()
                elif event.key == pygame.K_1:
                    gamemode.fps = 90
                    gamemode.velocity = 2
                    gameloop()
                elif event.key == pygame.K_2:
                    gamemode.fps = 90
                    gamemode.velocity = 6
                    gameloop()
                elif event.key == pygame.K_3:
                    gamemode.fps = 90
                    gamemode.velocity = 8
                    gameloop()

                    welcome()

        pygame.display.update()
        clock.tick(60)


def welcome():

    exit_game = False

    while not exit_game:
        gameWindow.blit(play_game_i, (0, 0))
        text_screen("Welcome", yellow, 370, 20)
        text_screen(user_id.uname, white, 170, 80)

        for event in pygame.event.get():

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


def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        gameloop.hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    gameloop.score = 0
    init_velocity = gamemode.velocity
    snake_size = 30
    fps = gamemode.fps

    while not exit_game:

        if game_over:

            with open("hiscore.txt", "w") as f:
                f.write(str(gameloop.hiscore))
                gameWindow.blit(game_over_i,(0, 0))
                pygame.draw.rect(gameWindow, blue, [30, 35, 250, 60])
                pygame.draw.rect(gameWindow, green, [630, 35, 250, 60])
                text_screen("Score: " + str(gameloop.score) + " " *45 + "Hiscore: "+str(gameloop.hiscore), white, 50, 50)
                text_screen(user_id.uname, white, 200, 150)
                text_screen("Y o u r ", red, 500, 190)

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

                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

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

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                gameloop.score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

                if gameloop.score>int(gameloop.hiscore):
                    gameloop.hiscore = gameloop.score

            gameWindow.blit(bg_image,(0,0))
            text_screen("Score: " + str(gameloop.score) + "  Hiscore: "+str(gameloop.hiscore), red, 5, 5)
            text_screen("-" * 35 , red, 5, 25)
            pygame.draw.rect(gameWindow, aqua, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over = True

            plot_snake(gameWindow, white, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

user_id()
welcome()
