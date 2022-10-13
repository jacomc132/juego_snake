from clases import Player
from clases import Display
import pygame
from random import randint
from clases import Fruit

pygame.init()

fruit_image = pygame.image.load('z_image.png')
blue1 = (216,243,220)
blue2 = (183,228,199)
blue3 = (116,198,157)
green_lima = (50,205,50)
ligth_blue = (173, 216, 230)
red = (220,20,60)
dark_green = (0,100,0)
ligth_green = (127,255,0)
yellow_green = (173,255,47)
gray = (128,128,128)
display_heigth = 900
display_width = 1600
initial_point = 0
run = True
primera_fruta = True



my_display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption("Snake game")

#Instanciación clase Player,display,fruit:
player1 = Player(50,50,my_display,red,ligth_blue)
display1 = Display(my_display,display_heigth,display_width,blue1,blue2)
fruit1 = Fruit(20,20,my_display,green_lima)

#Ejecuión constante del juego:
while run == True:
    pygame.time.delay(115)


    #Crear cuadrícula:
    display1.create_grid()
    #Crear margen:
    display1.create_margin(blue3,50,50)



    #Evento sucedido en caso de que el usuario haga click en la x posterior:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #Al presionar teclas:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player1.x<(display_width - 50):
        player1.direction = 'rigth'
    elif keys[pygame.K_LEFT] and player1.x>(initial_point + 50):
        player1.direction = 'left'
    elif keys[pygame.K_DOWN] and player1.y<(display_heigth - 50):
        player1.direction = 'down'
    elif keys[pygame.K_UP] and player1.y>(initial_point):
        player1.direction = 'up'

    #Desplazamiento de jugador:
    if player1.direction == 'rigth':
        player1.x += 50
    elif player1.direction == 'left':
        player1.x -= 50
    elif player1.direction == 'up':
        player1.y -= 50
    elif player1.direction == 'down':
        player1.y += 50


    
    #Dibujar primera fruta:
    player1.position = (player1.x,player1.y)
    if primera_fruta == True:
        fruit1.position = (500,600)
        if player1.position == fruit1.position:
            primera_fruta = False

    #Dibujar y borrar frutas siguientes:
    if player1.position == fruit1.position and primera_fruta == False:
        fruit1.create_random_cords()
        fruit1.position = (fruit1.x,fruit1.y)
        player1.score += 1

    my_display.blit(fruit_image,fruit1.position)
    
    #Añadir puntaje:
    text = display1.font.render('Score: '+str(player1.score), 1, (255,255,255))
    display1.my_display.blit(text,(1400,20))


    #Cuando player se sale de los bordes:
    if player1.x == 50 or  player1.x == 1550 or player1.y == 0 or player1.y == 850:
        run = False #task: Add gameover screen



    player1.draw_character()
    pygame.display.update()



#Romper programa
pygame.quit()