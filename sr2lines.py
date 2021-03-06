#Gabriel Quiroz
#19255
#27/07/2021
#Graficas
import struct

def char(c):
    #1 byte (char)
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes (short)
    return struct.pack('=h', w)

def dword(d):
    #4 bytes (long)
    return struct.pack('=l', d)

def color(r, g, b):
    # Acepta valores de 0 a 1
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])


color1 = color(0,0,0)
color2 = color(1,1,1)

#Funciones implementadas
class Renderer(object):
    #Glinit
    def __init__(self, width, height):
        self.punto_color = color2
        self.bitmap_color = color1
        self.glCreateWindow(width, height)
    #GlCreateWindow
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0,0, width, height)
    #GlViewPort
    def glViewport(self, x, y, width, height):
        self.vpX = int(x)
        self.vpY = int(y)
        self.vpWidth = int(width)
        self.vpHeight = int(height)

    #glClearColor
    def glClearColor(self, r, g, b):
        self.bitmap_color = color(r, g, b)
    #glClear
    def glClear(self):
        self.pixels = [[ self.bitmap_color for y in range(self.height)]
                       for x in range(self.width)]
    
    def glPoint(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[int(x)][int(y)] = color or self.punto_color

    def glColor(self, r, g, b):
        self.punto_color = color(r,g,b)
    
    #glVertex
    def glVertex(self, x, y, color = None):
        x = int( (x + 1) * (self.vpWidth / 2) + self.vpX )
        y = int( (y + 1) * (self.vpHeight / 2) + self.vpY)


        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[int(x)][int(y)] = color or self.punto_color
            
    #glFinish
    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Bitmap
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
                    
    def glLine(self, v0x, v0y, v1x, v1y, color = None):

        x0 = int( (v0x + 1) * (self.vpWidth / 2) + self.vpX)
        x1 = int( (v1x + 1) * (self.vpWidth / 2) + self.vpX)
        y0 = int( (v0y + 1) * (self.vpHeight / 2) + self.vpY)
        y1 = int( (v1y + 1) * (self.vpHeight / 2) + self.vpY)

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y, x, color)
            else:
                self.glPoint(x, y, color)

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1
                
                
                

          
width = int(input("Ingresa el ancho de la imagen:\n"))
height = int(input("Ingresa el alto de la imagen:\n"))
print("-----------------------Color del bitmap----------------------------")
bitmap1 = float(input("Ingresa un valor de 0 a 1:\n"))
bitmap2 = float(input("Ingresa un valor de 0 a 1:\n"))
bitmap3 = float(input("Ingresa un valor de 0 a 1:\n"))
print("-----------------------Color de la linea----------------------------")
punto1 = float(input("Ingresa un valor de 0 a 1:\n"))
punto2 = float(input("Ingresa un valor de 0 a 1:\n"))
punto3 = float(input("Ingresa un valor de 0 a 1:\n"))
x2 = int(input("Ingresa la x de -1 a 1 donde se ubicara x1:\n"))
y2 = int(input("Ingresa la y de -1 a 1 donde se ubicara y1:\n"))
x3 = int(input("Ingresa la x de -1 a 1 donde se ubicara x2:\n"))
y3 = int(input("Ingresa la y de -1 a 1 donde se ubicara y2:\n"))
r = Renderer(width, height)
r.glClearColor(bitmap1,bitmap2,bitmap3)
r.glColor(punto1,punto2,punto3)
r.glLine(x2,y2,x3,y3)
r.glFinish('gabriel.bmp')
print("Se ha creado el archivo 'gabriel.bmp'")
