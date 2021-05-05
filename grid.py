import pygame
import os

letterX = pygame.image.load(os.path.join('resource','x.png')) #memasukkan gambar x
letterO = pygame.image.load(os.path.join('resource','o.png')) #memasukkan gambar y

class Grid:
    #membuat grid
   def __init__(self):
        self.grid_lines = [((0,200),
                            (600,200)), 
                            ((0,400),(600,400)), 
                            ((200,0),(200,600)),
                            ((400,0),(400,600))] 

        self.grid = [[0 for x in range(3)] for y in range(3)]
        #pergantian pemain
        self.switch_player = True

    #method untuk menggambar grid dan x o
   def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (130,130,130), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x,y) == "X":
                    surface.blit(letterX, (x*200, y*200))
                elif self.get_cell_value(x,y) == "O":
                    surface.blit(letterO, (x*200, y*200))

    #method untuk mengambil nilai cell
   def get_cell_value(self,x,y):
       return self.grid[y][x]

    #method untuk memasukkan nilai cell
   def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    #method untuk menentukan letak mouse
   def get_mouse(self, x, y, player):
       if self.get_cell_value(x,y) == 0: #pergantian pemain hanya terjadi jika cell bernilai 0 (belum diisi)
        self.switch_player = True
        if player == "X":
           self.set_cell_value(x,y, "X")
        elif player == "O":
           self.set_cell_value(x,y, "O")
        
       else:
            self.switch_player = False

    #method untuk print grid
   def print_grid(self):
       for row in self.grid:
           print(row)

    #method untuk cek pemenang
  # def check_winner(self,player):
       