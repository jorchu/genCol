import pygame as py
import sys
import random
import pyperclip

all_to_list = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15,
        'g':16,
        'h': 17
        
    }


dec_to_list = {
        0:0,
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15: 'f',
        16: 'g',
        17: 'h'
    }        



def conversor(num, based, to):
    if based != 10:
      number = num
      pow = len(number) - 1
      decimal = 0
      pos = 0

      for i in range(len(number)):
          decimal +=  all_to_list[number[pos]] * based ** pow
          pow -= 1
          pos += 1
  

    else:
        decimal = int(num)
    
    base = 0
    xp =  to ** base
    convert_num = [0]
    i = 0
    pos = 0
    while decimal -i * xp >= 0:
            if i == to:
                i = 0
                base +=1
                xp = to ** base
                convert_num.append(0)
            else:
                i += 1
    while base >= 0:
        if decimal -i * xp < 0:
            i -= 1
            convert_num[pos] = dec_to_list[i]
            decimal -= xp * i
            base -= 1
            xp = to ** base
            i = 0
            pos += 1
        else:
            i += 1

    str_convert = ''

    for i in range(len(convert_num)):
        str_convert += str(convert_num[i])
        
    return str_convert 

py.init()

size = 1200,650
screen = py.display.set_mode(size)
screen.fill((255,255,255))
font = py.font.SysFont('Arial', 35)
r = 255
g = 255
b = 255
hexa = 'ffffff'


input_prop = (40, 20, 210, 100, [0,0,0])
hex_prop = (input_prop[0], input_prop[1]+130, 210, 100, [0,0,0])
bin_prop = (hex_prop[0], hex_prop[1]+130, 210, 100, [0,0,0])
copy_hex_prop = (bin_prop[0], bin_prop[1]+130, 210, 100, [0,0,0])
copy_bin_prop = (copy_hex_prop[0], copy_hex_prop[1]+130, 210, 100, [0,0,0])

red_bar_prop = ((300,70), (300+511, 70), 15, [300+511, 70], 15, (100,0,0), (0,0,0), (255,0,0))
green_bar_prop = ((300,red_bar_prop[0][1]+130), (300+511, red_bar_prop[1][1]+130), 15, [300+511, red_bar_prop[3][1]+130], 15, (0,100,0), (0,0,0), (0,255,0))
blue_bar_prop = ((300, green_bar_prop[0][1]+130), (300+511, green_bar_prop[1][1]+130), 15, [300+511, green_bar_prop[3][1]+130], 15, (0,0,100), (0,0,0), (0,0,255))

red_hex_prop = (red_bar_prop[1][0]+30, red_bar_prop[1][1]-40, 100, 80, [0,0,0])
green_hex_prop = (red_hex_prop[0], red_hex_prop[1]+red_hex_prop[3]+50, 100, 80, [0,0,0])
blue_hex_prop = (green_hex_prop[0], green_hex_prop[1]+green_hex_prop[3]+50, 100, 80, [0,0,0])

red_bin_prop = (red_hex_prop[0]+red_hex_prop[2]+30, red_hex_prop[1], 100, 80, [0,0,0])
green_bin_prop = (red_bin_prop[0], red_bin_prop[1]+red_bin_prop[3]+50, 100, 80, [0,0,0])
blue_bin_prop = (green_bin_prop[0], green_bin_prop[1]+green_bin_prop[3]+50, 100, 80, [0,0,0])

def conver(red, green, blue):
    global hexa
    hex = ''
    colors = [red, green, blue]
    frag = ''
    for i in range(len(colors)):
        frag = conversor(colors[i], 10, 16)
        if len(frag) < 2:
            frag = '0' + str(colors[i])
        
        hex += frag
        frag = ''
    hexa = hex

def gen_aleatory_color():
    global hexa, r, g, b
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    r = red
    g = green
    b = blue
    
    conver(red, green, blue)

def copy_hexa():
    pyperclip.copy(hexa)

def copy_bin():
    pyperclip.copy(f'{r}, {g}, {b}')


class button:
    def __init__(self, propieties):
        self.width = propieties[2] 
        self.height = propieties[3]
        self.x = propieties[0]
        self.y = propieties[1]
        self.color = propieties[4]
        self.size = (self.x, self.y, self.width, self.height)
        
    def draw(self, pos, text, do =0):
        if not(pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height)):
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        elif do:
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        else:
            py.draw.rect(screen, (50,50,50), self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))

    def click(self, pos, func=''):
        if pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height):
            if func:
                func()

class barra:
    def __init__(self, propieties):
        self.str_l = propieties[0] 
        self.end_l = propieties[1]
        self.width_l = propieties[2]
        self.pos_c = propieties[3]
        self.radius = propieties[4]
        self.line_color = propieties[5]
        self.circle_clolor = propieties[6]
        self.line_color2 = propieties[7]
        self.end_l2 = self.pos_c
    def draw(self):
        py.draw.line(screen, self.line_color, self.str_l, self.end_l, self.width_l)
        py.draw.line(screen, self.line_color2,self.str_l, self.pos_c, self.width_l)
        py.draw.circle(screen, self.circle_clolor, self.pos_c, self.radius)

    def auto_pos(self, col):
        self.pos_c[0] = col * 2 + 300
        self.end_l2 = self.pos_c
    
    def gen_col(self, pos, push, col):
        global r, g, b
        if pos[0] in range(self.str_l[0], self.end_l[0]) and pos[1] in range(self.str_l[1]-15, self.str_l[1] + self.width_l+10) and self.str_l[0] <= pos[0] <= self.end_l[0] and push[0]:
            position = pos[0] - 300
            if col == 0:
                r = position // 2
            elif col == 1:
                g = position // 2
            else:
                b = position // 2

            conver(r, g, b)
            


red_bin_btn = button(red_bin_prop)
green_bin_btn = button(green_bin_prop)
blue_bin_btn = button(blue_bin_prop)

red_hex_btn = button(red_hex_prop)
green_hex_btn = button(green_hex_prop)
blue_hex_btn = button(blue_hex_prop)

red_bar = barra(red_bar_prop)
green_bar = barra(green_bar_prop)
blue_bar = barra(blue_bar_prop)

input_btn = button(input_prop)
hex_btn = button(hex_prop)
bin_btn = button(bin_prop)
copy_hex_btn = button(copy_hex_prop)
copy_bin_btn = button(copy_bin_prop)


while True:
    screen.fill((int(r), int(g), int(b)))
    pos = py.mouse.get_pos()
    push = py.mouse.get_pressed()
    for e in py.event.get():
        if e.type == py.QUIT:
            sys.exit()
        if e.type == py.MOUSEBUTTONDOWN and e.button == 1:
            input_btn.click(pos, gen_aleatory_color)
            copy_hex_btn.click(pos, copy_hexa)
            copy_bin_btn.click(pos, copy_bin)

    input_btn.draw(pos, 'Aleatory')
    hex_btn.draw(pos, hexa, 1)
    bin_btn.draw(pos, f'{r},{g},{b}',1)
    copy_hex_btn.draw(pos, 'Copy hex')
    copy_bin_btn.draw(pos, 'Copy bin')

    red_bar.draw()
    green_bar.draw()
    blue_bar.draw()

    red_bar.auto_pos(int(r))
    green_bar.auto_pos(int(g))
    blue_bar.auto_pos(int(b))

    red_bar.gen_col(pos, push, 0)
    green_bar.gen_col(pos, push, 1)
    blue_bar.gen_col(pos, push, 2)

    red_hex_btn.draw(pos, hexa[0:2],1)
    green_hex_btn.draw(pos, hexa[2:4],1)
    blue_hex_btn.draw(pos, hexa[4:6],1)

    red_bin_btn.draw(pos, str(r), 1)
    green_bin_btn.draw(pos, str(g), 1)
    blue_bin_btn.draw(pos, str(b), 1)

    py.display.flip()

