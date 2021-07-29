#! /usr/bin/python
#Gabriel Quiroz 19255
#Gráficas
#Lab1

import struct

def char(c):
  # char
  return struct.pack('=c', c.encode('ascii'))

def word(w):
  # short
  return struct.pack('=h', w)

def dword(w):
  # long
  return struct.pack('=l', w)


def color(r, g, b):
  return bytes([b, g, r])

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)


class Renderer(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.current_color = WHITE
    self.clear()

  def clear(self):
    self.framebuffer = [
      [BLACK for x in range(self.width)]
      for y in range(self.height)
    ]
  
  def write(self, filename):
    f = open(filename, 'bw')

    # file header 14
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + 3*(self.width*self.height)))
    f.write(dword(0))
    f.write(dword(14 + 40))

    # info header 40
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(3*(self.width*self.height)))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    
    # bitmap
    for y in range(self.height):
      for x in range(self.width):
        f.write(self.framebuffer[y][x])

    f.close()
  
  def render(self):
    self.write('lab1GQ.bmp')

  def point(self, x, y, color = None):
    self.framebuffer[y][x] = color or self.current_color
    
  def glVertex(self,x, y):
    if(x>0):
        xw = int((x+1) * (vw[2]/2)  + vw[0]) - 1

    else:
        xw = int((x+1) * (vw[2]/2)  + vw[0])


    if(y>0):
        yw = int((y+1) * (vw[3]/2) + vw[1]) -1

    else:
        yw = int((y+1) * (vw[3]/2) + vw[1]) 

    return ([xw, yw])

  def line(self, x0, y0, x1, y1):
      dy = abs(y1 - y0)
      dx = abs(x1 - x0)

      steep = dy > dx

      if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

      offset = 0 * 2 * dx
      threshold = 0.5 * 2 * dx
      y = y0

      # y = mx + b
      points = []
      for x in range(x0, x1):
        if steep:
          r.glVertex(y, x)
        else:
          r.glVertex(x, y)

        offset += (dy/dx) * 2 * dx
        if offset >= threshold:
          y += 1 if y0 < y1 else -1
          threshold += 1 * 2 * dx
          
          

r = Renderer(1024, 768)
r.current_color = color(255, 255, 255)
r.line(100,200,300,400)
r.render()
