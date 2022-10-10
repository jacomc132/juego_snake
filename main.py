from clases import Player
from clases import Display
import pygame

pygame.init()

ligth_blue = (173, 216, 230)
red = (220,20,60)
dark_green = (0,100,0)
ligth_green = (127,255,0)
display_heigth = 900
display_width = 1600
initial_point = 0
run = True
my_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption("Snake game")

#Instanciación clase Player y display:
player1 = Player(50,50,my_display,red,ligth_blue)
display1 = Display(my_display,display_heigth,display_width,dark_green,ligth_green)

#Ejecuión constante del juego:
while run == True:
    pygame.time.delay(100)


    #Crear cuadrícula:
    display1.create_grid()
    #Crear margen:
    #display1.create_margin(ligth_blue,50,50)



    #Recorrer acciones ejecutadas por el usuario:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #Al presionar teclas:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player1.x<(display_width - 100):
        player1.x += 50
    elif keys[pygame.K_LEFT] and player1.x>(initial_point + 100):
        player1.x -= 50
    elif keys[pygame.K_DOWN] and player1.y<(display_heigth - 100):
        player1.y += 50
    elif keys[pygame.K_UP] and player1.y>(initial_point + 50):
        player1.y -= 50

    
    player1.draw_character()



#Romper programa
pygame.quit()