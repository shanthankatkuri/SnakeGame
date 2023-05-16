import pygame
from random import *
import os
pygame.mixer.init()
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
yellow=(255,255,0)

screen_width=900
screen_height=600

#creating window
gameWindow=pygame.display.set_mode((screen_width,screen_height))

bgimg=pygame.image.load("D:\Python\pygame\snakebgimg.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
gameoverimg=pygame.image.load("D:\Python\pygame\gameoverbg.jpg")
gameoverimg=pygame.transform.scale(gameoverimg,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snake Xenzia")
pygame.display.update()


clock=pygame.time.Clock()
font=pygame.font.SysFont('none',55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size],border_radius=50)

snake_list=[]
snake_length=1

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.blit(bgimg,(0,0))
        text_screen("Welcome To Snake Xenzia",black,180,250)
        text_screen("Press SPACEBAR To Play",black,190,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('D:\Python\pygame\snakebg.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()
        pygame.display.update()
        clock.tick(30)
#game loop
def gameloop():
    #game specific variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    food_x=randint(50,screen_width-50)
    food_y=randint(50,screen_height-50)
    score=0
    init_velocity=4
    snake_size=15
    snake_list=[]
    snake_length=1

    if(not os.path.exists("D:\Python\pygame\highscore.txt")):
        with open("D:\Python\pygame\highscore.txt","w") as f:
            f.write("0")

    with open("D:\Python\pygame\highscore.txt","r") as f:
        highscore=f.read()
    fps=30
    while not exit_game:
        if game_over:
            with open("D:\Python\pygame\highscore.txt","w") as f:
               f.write(str(highscore))
            gameWindow.blit(gameoverimg,(0,0))
            text_screen(f"Press ENTER To Play Again",red,200,350)
            text_screen(f"Score:{score}",red,350,220)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load('D:\Python\pygame\snakebg.mp3')
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0

            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=10
                food_x=randint(100,screen_width-100)
                food_y=randint(100,screen_height-100)
                snake_length+=5
            if score>int(highscore):
                highscore=score

            gameWindow.fill(green)
            text_screen(f"Score:{score}         Highscore:{highscore}",white,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size],border_radius=50)


            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('D:\Python\pygame\gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('D:\Python\pygame\gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit() 
welcome()      
