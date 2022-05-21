import pgzrun
from pgzrun import *

#可修改的部分
######################################

clist_row = 50#每行格子数量，最大50
clist_list = 35#每列格子数量，最大35

######################################

WIDTH = 1000
HEIGHT = 750

if clist_row > 50:
   clist_row = 50
if clist_list > 35:
   clist_list = 35
clist_number = clist_row * clist_list

_row = (1000-clist_row*20)//2
_list = (700-clist_list*20)//2+50

clist = []
clist1 = []
x1 = 0
y1 = 0
x2 = 0
y2 = 0
pos_r = [20,270]
pos_g = [20,295]
pos_b = [20,320]

flag_dot = True
flag_rect = False
flag_rubber = False
flag_color = False
flag_draw = False

for i in range(clist_number):
   clist.append([])
for i in range(clist_number):
   clist[i].append((255,255,255))

color = (255,255,255)
move_flag = 0
x = 0

r = Actor('r',[-100,-100])
g = Actor('g',[-100,-100])
b = Actor('b',[-100,-100])

def draw():
    screen.clear()
    screen.fill((255,255,255))
    for i in range(clist_number):
        if clist[i][-1] != (255,255,255):
            screen.draw.filled_rect(Rect((i%clist_row*20+_row,i//clist_row*20+_list),(20,20)),clist[i][-1])
    if flag_rect == True and flag_draw == True:
        i = 20
        j = 20
        if x2 <= x1 and y2 <= y1:
            screen.draw.filled_rect(Rect((x2+_row,y2),(x1-x2+i,y1-y2+j)),color)
        elif x1 <= x2 and y2 <= y1:
            screen.draw.filled_rect(Rect((x1+_row,y2),(x2-x1+i,y1-y2+j)),color)
        elif x2 <= x1 and y1 <= y2:
            screen.draw.filled_rect(Rect((x2+_row,y1),(x1-x2+i,y2-y1+j)),color)
        elif x1 <= x2 and y1 <= y2:
            screen.draw.filled_rect(Rect((x1+_row,y1),(x2-x1+i,y2-y1+j)),color)
    screen.draw.line((10,10),(40,10),(0,0,0))
    screen.draw.line((55,10),(195,10),(0,0,0))
    screen.draw.line((210,10),(260,10),(0,0,255))
    screen.draw.line((275,10),(325,10),(255,0,0))
    screen.draw.line((10,40),(40,40),(0,0,0))
    screen.draw.line((55,40),(195,40),(0,0,0))
    screen.draw.line((210,40),(260,40),(0,0,255))
    screen.draw.line((275,40),(325,40),(255,0,0))
    screen.draw.line((10,10),(10,40),(0,0,0))
    screen.draw.line((40,10),(40,40),(0,0,0))
    screen.draw.line((55,10),(55,40),(0,0,0))
    screen.draw.line((85,10),(85,40),(0,0,0))
    screen.draw.line((135,10),(135,40),(0,0,0))
    screen.draw.line((195,10),(195,40),(0,0,0))
    screen.draw.line((210,10),(210,40),(0,0,255))
    screen.draw.line((260,10),(260,40),(0,0,255))
    screen.draw.line((275,10),(275,40),(255,0,0))
    screen.draw.line((325,10),(325,40),(255,0,0))
    screen.draw.filled_rect(Rect((15,15),(20,20)),color)
    screen.draw.text('点', center=[70, 25], fontsize=15,color = 'black')
    screen.draw.text('矩形', center=[110, 25], fontsize=15,color = 'black')
    screen.draw.text('橡皮擦', center=[165, 25], fontsize=15,color = 'black')
    screen.draw.text('撤回', center=[235, 25], fontsize=15,color = 'blue')
    screen.draw.text('清空', center=[300, 25], fontsize=15,color = 'red')
    if flag_dot == True:
        screen.draw.text('点', center=[70, 25], fontsize=15,color = 'blue')
        screen.draw.line((55,10),(85,10),(0,0,255))
        screen.draw.line((55,40),(85,40),(0,0,255))
        screen.draw.line((55,10),(55,40),(0,0,255))
        screen.draw.line((85,10),(85,40),(0,0,255))
    elif flag_rect == True:
        screen.draw.text('矩形', center=[110, 25], fontsize=15,color = 'blue')
        screen.draw.line((85,10),(135,10),(0,0,255))
        screen.draw.line((85,40),(135,40),(0,0,255))
        screen.draw.line((85,10),(85,40),(0,0,255))
        screen.draw.line((135,10),(135,40),(0,0,255))
    elif flag_rubber == True:
        screen.draw.text('橡皮擦', center=[165, 25], fontsize=15,color = 'blue')
        screen.draw.line((135,10),(195,10),(0,0,255))
        screen.draw.line((135,40),(195,40),(0,0,255))
        screen.draw.line((135,10),(135,40),(0,0,255))
        screen.draw.line((195,10),(195,40),(0,0,255))
        
    for i in range(clist_row):
        screen.draw.line((i*20+_row+20,_list+20),(i*20+_row+20,800-_list),(0,0,0))
        if i != clist_row:
           screen.draw.text(str(i), center=[i*20+10+_row, 10+_list], fontsize=20,color = 'black')
    for i in range(clist_list):
        screen.draw.line((_row+20,i*20+_list+20),(1000-_row,i*20+_list+20),(0,0,0))
        if i != clist_list:
           screen.draw.text(str(i), center=[10+_row, i*20+10+_list], fontsize=20,color = 'black')

    if flag_color == True:
        screen.draw.line((10,10),(40,10),(0,0,255))
        screen.draw.line((10,40),(40,40),(0,0,255))
        screen.draw.line((10,10),(10,40),(0,0,255))
        screen.draw.line((40,10),(40,40),(0,0,255))
        screen.draw.filled_rect(Rect((10,60),(275,275)),(255,255,255))
        screen.draw.filled_rect(Rect((57.5,75),(180,180)),color)
        screen.draw.filled_rect(Rect((20,265),(255,10)),(255,0,0))
        screen.draw.filled_rect(Rect((20,290),(255,10)),(0,255,0))
        screen.draw.filled_rect(Rect((20,315),(255,10)),(0,0,255))

    r.draw()
    g.draw()
    b.draw()

def on_mouse_move(pos):
    global move_flag,x,color,clist,x2,y2,clist1
    
    if move_flag == 1:
        r.x += pos[0] - x
        if r.x >= 275:
            r.x = 275
        elif r.x <= 20:
            r.x = 20
        x = pos[0]
        pos_r[0] = r.x
    elif move_flag == 2:
        g.x += pos[0] - x
        if g.x >= 275:
            g.x = 275
        elif g.x <= 20:
            g.x = 20
        x = pos[0]
        pos_g[0] = g.x
    elif move_flag == 3:
        b.x += pos[0] - x
        if b.x >= 275:
            b.x = 275
        elif b.x <= 20:
            b.x = 20
        x = pos[0]
        pos_b[0] = b.x
    if flag_color == True:
        color = (int(r.x - 20),int(g.x - 20),int(b.x - 20))
        
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_dot == True and flag_color == False and flag_draw == True:
        y1 = ((pos[0]-_row) // 20) * 20
        x1 = ((pos[1]-_list) // 20) * 20
        if (x1//20)*clist_row+(y1//20) not in clist1:
            clist[(x1//20)*clist_row+(y1//20)].append(color)
            clist1.append((x1//20)*clist_row+(y1//20))
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_rect == True and flag_color == False and flag_draw == True:
        x2 = ((pos[0]-_row) // 20) * 20
        y2 = ((pos[1]-_list) // 20) * 20 + _list
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_rubber == True and flag_color == False and flag_draw == True:
        y1 = ((pos[0]-_row) // 20) * 20
        x1 = ((pos[1]-_list) // 20) * 20
        if (x1//20)*clist_row+(y1//20) not in clist1:
            clist[(x1//20)*clist_row+(y1//20)].append((255,255,255))
            clist1.append((x1//20)*clist_row+(y1//20))
    

def on_mouse_down(pos):
    global flag_dot,flag_rect,flag_rubber,flag_color,move_flag,color,clist,flag_draw,x1,y1,x2,y2,clist1
    if pos[0] > 10 and pos[0] < 40 and pos[1] > 10 and pos[1] < 40:
        flag_color = True
        r.pos = pos_r
        g.pos = pos_g
        b.pos = pos_b
    elif pos[0] >= 10 and pos[0] <= 285 and pos[1] >= 60 and pos[1] <=335:
        pass
    else:
        flag_color = False
        r.pos = [-100,-100]
        g.pos = [-100,-100]
        b.pos = [-100,-100]
    if pos[0] >= 55 and pos[0] <= 85 and pos[1] >= 10 and pos[1] <= 40:
        flag_dot = True
        flag_rect = False
        flag_rubber = False
    elif pos[0] > 85 and pos[0] <= 135 and pos[1] >= 10 and pos[1] <= 40:
        flag_rect = True
        flag_dot = False
        flag_rubber = False
    elif pos[0] > 135 and pos[0] <= 195 and pos[1] >= 10 and pos[1] <= 40:
        flag_rubber = True
        flag_dot = False
        flag_rect = False
    elif pos[0] > 210 and pos[0] <= 260 and pos[1] >= 10 and pos[1] <= 40:
        for i in clist:
            if len(i) != 1:
                i.pop(-1)
    elif pos[0] > 275 and pos[0] <= 325 and pos[1] >= 10 and pos[1] <= 40:
        for i in range(clist_number):
            clist[i] = [(255,255,255)]
    if r.collidepoint(pos):
        move_flag = 1
    elif g.collidepoint(pos):
        move_flag = 2
    elif b.collidepoint(pos):
        move_flag = 3

    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_dot == True and flag_color == False:
        y1 = ((pos[0]-_row) // 20) * 20
        x1 = ((pos[1]-_list) // 20) * 20
        flag_draw = True
        clist[(x1//20)*clist_row+(y1//20)].append(color)
        clist1.append((x1//20)*clist_row+(y1//20))
            
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_rect == True and flag_color == False:
        x1 = ((pos[0]-_row) // 20) * 20
        y1 = ((pos[1]-_list) // 20) * 20 + _list
        flag_draw = True
        x2 = x1
        y2 = y1
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_rubber == True and flag_color == False:
        y1 = ((pos[0]-_row) // 20) * 20
        x1 = ((pos[1]-_list) // 20) * 20
        flag_draw = True
        clist[(x1//20)*clist_row+(y1//20)].append((255,255,255))
        clist1.append((x1//20)*clist_row+(y1//20))
    if pos[0] <= 275 and pos[0] >= 20 and flag_color == True:
       if pos[1] <= 275 and pos[1] >= 265:
          r.x = pos[0]
          pos_r[0] = r.x
       elif pos[1] <= 305 and pos[1] >= 290:
          g.x = pos[0]
          pos_g[0] = g.x
       elif pos[1] <= 335 and pos[1] >= 320:
          b.x = pos[0]
          pos_b[0] = b.x
       color = (int(r.x - 20),int(g.x - 20),int(b.x - 20))
       

def on_mouse_up(pos):
    global move_flag,x,flag_draw,clist,x1,y1,x2,y2,clist1
    x = pos[0]
    move_flag = 0
    if pos[0] < 1000-_row and pos[0] > _row+20 and pos[1] < 800-_list and pos[1] > _list+20 and flag_rect == True and flag_color == False and flag_draw == True:
        if x2 <= x1 and y2 <= y1:
            for i in range(x2//20,(x1//20)+1):
                for j in range((y2-_list)//20,((y1-_list)//20)+1):
                    clist[j*clist_row+i].append(color)
                    clist1.append(j*clist_row+i)
        elif x1 <= x2 and y2 <= y1:
            for i in range(x1//20,(x2//20)+1):
                for j in range((y2-_list)//20,((y1-_list)//20)+1):
                    clist[j*clist_row+i].append(color)
                    clist1.append(j*clist_row+i)
        elif x2 <= x1 and y1 <= y2:
            for i in range(x2//20,(x1//20)+1):
                for j in range((y1-_list)//20,((y2-_list)//20)+1):
                    clist[j*clist_row+i].append(color)
                    clist1.append(j*clist_row+i)
        elif x1 <= x2 and y1 <= y2:
            for i in range(x1//20,(x2//20)+1):
                for j in range((y1-_list)//20,((y2-_list)//20)+1):
                    clist[j*clist_row+i].append(color)
                    clist1.append(j*clist_row+i)
    if pos[0] < 1000-_row and pos[0] > _row and pos[1] < 800-_list and pos[1] > _list+20:
        for i in range(clist_number):
            if i not in clist1:
                clist[i].append(clist[i][-1])
    flag_draw = False
    clist1.clear()

pgzrun.go()
