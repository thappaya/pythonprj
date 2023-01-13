import pygame
import time
import random
pygame.init()

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

disp_width = 600
disp_height = 600

disp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('A shitty snake game by PExK')

sneki_snek = 10

game_over = False

food_x = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0
food_y = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0

sneki_snek_speed = 15

text = pygame.font.SysFont(None, 35)
score_text = pygame.font.SysFont(None, 25)

def howbadyouredoing(score):
    value = score_text.render("Your Score: " + str(score), True, white)
    disp.blit(value, [0, 0])

def drawText(msg,color):
    m = text.render(msg,True,color) 
    disp.blit(m, [220, 265])

def our_sneki_snek(sneki_snek_tail, sneki_snek_list):
    for x in sneki_snek_list:
        pygame.draw.rect(disp, green, [x[0], x[1], sneki_snek_tail, sneki_snek_tail])

x_axis = disp_width/2
y_axis = disp_height/2

x_tracker = 0
y_tracker = 0

sneki_snek_List = []
the_Tail = 1

timer = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():   
        print(event)             
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_tracker = -10
                y_tracker = 0
            elif event.key == pygame.K_RIGHT:
                x_tracker = 10
                y_tracker = 0
            elif event.key == pygame.K_DOWN:
                x_tracker = 0
                y_tracker = 10        
            elif event.key == pygame.K_UP:
                x_tracker = 0
                y_tracker = -10

    if x_axis >= disp_width or x_axis < 0 or y_axis >= disp_height or y_axis < 0:
        game_over = True
                
    x_axis += x_tracker
    y_axis += y_tracker

    disp.fill(black)
    pygame.draw.rect(disp, green,[x_axis, y_axis, sneki_snek, sneki_snek])
    snake_Head = []
    snake_Head.append(x_axis)
    snake_Head.append(y_axis)
    sneki_snek_List.append(snake_Head)
    if len(sneki_snek_List) > the_Tail:
        del sneki_snek_List[0]

    for x in sneki_snek_List[:-1]:
        if x == snake_Head:
            game_close = True

    our_sneki_snek(sneki_snek, sneki_snek_List)
    howbadyouredoing(the_Tail - 1)
    
    pygame.draw.rect(disp, red, [food_x, food_y, sneki_snek, sneki_snek])
    pygame.display.update()
    

    if x_axis == food_x and y_axis == food_y:
        food_x = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0
        food_y = round(random.randrange(0, disp_height - sneki_snek) / 10.0) * 10.0
        the_Tail += 1
    
    timer.tick(sneki_snek_speed)

drawText("You sucked!", white)
pygame.display.update()
time.sleep(5)

pygame.quit()
quit()
