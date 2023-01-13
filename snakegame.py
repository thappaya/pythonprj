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

game_over = False

x_axis = disp_width/2
y_axis = disp_height/2

sneki_snek = 10

x_tracker = 0
y_tracker = 0

food_x = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0
food_y = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0

sneki_snek_speed = 15

text = pygame.font.SysFont(None, 35)

def drawText(msg,color):
    m = text.render(msg,True,color) 
    disp.blit(m, [220, 265])

timer = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        print(event) #for printing all the events in pygame window, mainly for debugging
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
    pygame.draw.rect(disp, red, [food_x, food_y, sneki_snek, sneki_snek])
    pygame.display.update()
    
    timer.tick(sneki_snek_speed)

drawText("You sucked!", white)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()