import pygame

pygame.init()

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

disp = pygame.display.set_mode((600,500))
pygame.display.set_caption('A shitty snake game by PExK')

game_over = False

x_axis = 250
y_axis = 250

x_tracker = 0
y_tracker = 0

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
                
    x_axis += x_tracker
    y_axis += y_tracker
    disp.fill(black)
    pygame.draw.rect(disp, green,[x_axis, y_axis, 10, 10])
    
    pygame.display.update()
    
    timer.tick(20)

pygame.quit()
quit()