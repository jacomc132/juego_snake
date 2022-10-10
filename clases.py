import pygame
#Clase que recibe altura, anchura y display para luego dibujar en este display un cuadrado en posicion 50,50.
class Player:
    def __init__(self,width,height,display,color1,color2):
        self.x = 100
        self.y = 100
        self.height = height
        self.width = width
        self.display = display
        self.color1 = color1
        self.color2 = color2
    


    def draw_character(self):
        pygame.draw.rect(self.display,self.color1,(self.x,self.y,self.width,self.height))
        pygame.display.update()
    



class Display:
    def __init__(self,my_display,display_height,display_width,color1,color2):
        self.my_display = my_display
        self.display_height = display_height
        self.display_width = display_width
        self.color1 = color1
        self.color2 =color2
    


    def create_grid(self):
        self.box_color = self.color1
        for i in range(0,self.display_height,50):
            for x in range(50,self.display_width,50):
                if self.box_color == self.color1:
                    self.box_color = self.color2
                elif self.box_color == self.color2:
                    self.box_color = self.color1
                pygame.draw.rect(self.my_display,self.box_color,(x,i,50,50))
        pygame.display.update()
    



    def create_margin(self,margin_color,margin_width,margin_heigth):
        self.margin_color = margin_color
        self.margin_width = margin_width
        self.margin_heigth = margin_heigth

        #Línea derecha:
        self.x = 0
        for y in range(0,500,50):
            pygame.draw.rect(self.my_display,self.margin_color,(self.x,y,))

        #Línea izquierda:

        #Línea abajo:

        #Línea arriba:

        

