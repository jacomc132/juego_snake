import pygame
from random import choice
#Clase que recibe altura, anchura y display para luego dibujar en este display un cuadrado en posicion 50,50.
class Player:
    def __init__(self, width, height, display, color1, color2):
        self.x = 300
        self.y = 300
        self.position = (self.x,self.y)
        self.height = height
        self.width = width
        self.display = display
        self.color1 = color1
        self.color2 = color2
        self.score = 0
        self.direction = 'none'
        self.game_over = False
        self.previous_positions = []
        self.last_position = 0
        self.body_count = 0
        self.body_index = 0
        self.body_positions = []
        
        
        
    

        #Dibujar cabeza serpiente:
    def draw_character(self):
        pygame.draw.rect(self.display, self.color1,(self.x, self.y, self.width, self.height))

    



    def snake_body(self,color):
        self.body_positions.clear()
        self.last_position = len(self.previous_positions)-1
        self.body_index = self.last_position - self.body_count
        while self.body_index < self.last_position:
            x = self.previous_positions[self.body_index][0]
            y = self.previous_positions[self.body_index][1]
            pygame.draw.rect(self.display, color,(x, y, self.width, self.height))
            self.body_positions.append((x,y))
            self.body_index += 1
            
    



class Display:
    def __init__(self,my_display,display_height,display_width,color1,color2):
        self.my_display = my_display
        self.display_height = display_height
        self.display_width = display_width
        self.color1 = color1
        self.color2 =color2
        self.font = pygame.font.SysFont('comicsans',40,True)
    


    def create_grid(self):
        self.box_color = self.color1
        for i in range(0,self.display_height,50):
            for x in range(50,self.display_width,50):
                if self.box_color == self.color1:
                    self.box_color = self.color2
                elif self.box_color == self.color2:
                    self.box_color = self.color1
                pygame.draw.rect(self.my_display,self.box_color,(x,i,50,50))
        
    



    def create_margin(self, margin_color, margin_width, margin_heigth):
        self.margin_color = margin_color
        self.margin_width = margin_width
        self.margin_heigth = margin_heigth

        #Línea derecha:
        self.x = self.display_width - 50
        for y in range(0,self.display_height,50):
            pygame.draw.rect(self.my_display,self.margin_color,(self.x,y,self.margin_heigth,self.margin_width))
        

        #Línea izquierda:
        self.x = 50
        for y in range(0,self.display_height,50):
            pygame.draw.rect(self.my_display,self.margin_color,(self.x,y,self.margin_heigth,self.margin_width))


        #Línea abajo:
        self.y = self.display_height - 50
        for x in range(50,self.display_width,50):
            pygame.draw.rect(self.my_display,self.margin_color,(x,self.y,self.margin_heigth,self.margin_width))


        #Línea arriba:
        self.y = 0
        for x in range(50,self.display_width,50):
            pygame.draw.rect(self.my_display,self.margin_color,(x,self.y,self.margin_heigth,self.margin_width))



    def print_gameover_image(self,image,coords):
        self.my_display.blit(image,coords)







class Fruit:
    def __init__(self, width, heigth, display, color):
        self.width = width
        self.heigth = heigth
        self.display = display
        self.color = color
        self.x_positions = []
        self.y_positions = []
        self.x = 250
        self.y = 450
        self.position = (self.x,self.y)




    def create_random_cords(self):
        self.x_positions = [i for i in range(100,1550,50)]
        self.y_positions = [i for i in range(50,850,50)]
        self.x = choice(self.x_positions)
        self.y = choice(self.y_positions)
        
        


class Button:
    
    def __init__(self, width, heigth, display, color1,color2, x, y):
        self.width = width
        self.heigth = heigth
        self.display = display
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y 
        self.font = pygame.font.SysFont('comicsans',40,True)
        self.x_positions = [x for x in range(self.x, (self.x+self.width) ,1)]
        self.y_positions = [y for y in range(self.y, (self.y+self.heigth),1)]


    def draw_button(self):
        #Dibujar box con hover y sin hover:
        if pygame.mouse.get_pos()[0] in self.x_positions and pygame.mouse.get_pos()[1] in self.y_positions:
            pygame.draw.rect(self.display, self.color2,(self.x, self.y, self.width, self.heigth))
        else:
            pygame.draw.rect(self.display, self.color1,(self.x, self.y, self.width, self.heigth))
        #Texto del cuadrado:
        text = self.font.render('RETRY', 1, (255,255,255))
        self.display.blit(text, (self.x +45, self.y+40))



