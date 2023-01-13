import pygame
pygame.init()
disp = pygame.display.set_mode((600,500))

pygame.display.set_caption('A shitty snake game by PExK')

green = (0,255,0)
red = (255,0,0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event) #for printing all the events in pygame window, mainly for debugging
        if event.type==pygame.QUIT:
            game_over = True
    pygame.draw.rect(disp,green,[300,250,10,10])
    pygame.display.update()
    
pygame.quit()
quit()