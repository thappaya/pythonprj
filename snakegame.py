# Hi again, imports!
import pygame
import time
import random
pygame.init()

# Colors, more colors!!!!!!!!
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

# Window size.
disp_width = 600
disp_height = 600

disp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('A shitty snake game by PExK')

# Snake size.
sneki_snek = 10

# Haaaaa you lost to a simple snake game.
game_over = False

# Feed me im hungy
food_x = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0
food_y = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0

# Wanna advance your S P E E D ? Adjust here.
sneki_snek_speed = 15

# Fonts and size selection.
text = pygame.font.SysFont(None, 35)
score_text = pygame.font.SysFont(None, 25)

# Functions (Yes I know).
def howbadyouredoing(score):
    value = score_text.render("Your Score: " + str(score), True, white)
    disp.blit(value, [0, 0])

def drawText(msg,color):
    m = text.render(msg,True,color) 
    disp.blit(m, [220, 265])

def our_sneki_snek(sneki_snek_tail, sneki_snek_list):
    for x in sneki_snek_list:
        pygame.draw.rect(disp, green, [x[0], x[1], sneki_snek_tail, sneki_snek_tail])

# Little guy's position.
x_axis = disp_width/2
y_axis = disp_height/2

# Little guy's movement.
x_tracker = 0
y_tracker = 0

# How cool is his tail ikr?!
sneki_snek_List = []
the_Tail = 1

# Tick tock.
timer = pygame.time.Clock()

# Tech tip: Controls lie here.
while not game_over:
    for event in pygame.event.get():   
        print(event) # mostly for debugging purposes.    
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

    # How you will lose to a simple game HA!
    if x_axis >= disp_width or x_axis < 0 or y_axis >= disp_height or y_axis < 0:
        game_over = True

    # Movement modifiers            
    x_axis += x_tracker
    y_axis += y_tracker

    # E R E C T I O N of the snake.
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
    
    # Food, more food!!!!!!!!!
    pygame.draw.rect(disp, red, [food_x, food_y, sneki_snek, sneki_snek])
    pygame.display.update()
    
    # Eating mechanisms.
    if x_axis == food_x and y_axis == food_y:
        food_x = round(random.randrange(0, disp_width - sneki_snek) / 10.0) * 10.0
        food_y = round(random.randrange(0, disp_height - sneki_snek) / 10.0) * 10.0
        the_Tail += 1
    
    # FPS determining.
    timer.tick(sneki_snek_speed)

# If you somehow lost, here you go!
drawText("You sucked!", white)
pygame.display.update()
time.sleep(5)

# FUCK THIS GAME, IMMA HEAD OUT!!!
pygame.quit()
quit()
