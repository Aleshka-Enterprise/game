import pygame

import random

# Переменные
x = 50
y = 600
g = 25
shoot = 0
xs = 0
xsz = 0
ysz = 30
ys = 30
jump = 0
pos = 1
sit = 0
shift = 0
stanina = 350
HP = 350
zombi = True
xz = 1400
yz = 600
shootZ = 4
zombiHP=1000
Menu=1
trap=500

zemx=500
zemy=650
time=1


# Меню
while Menu==0:
    windows=pygame.display.set_mode((1500,800))
    menu = pygame.image.load('game.bmp')
    menu_rect = menu.get_rect(bottomright=(400, 300))
    pygame.display.update()


# Мувы
while Menu==1:

    pygame.time.delay(10)
    window = pygame.display.set_mode((1500, 800))
    pygame.draw.rect(window, (25, 150, 250), (0, 0, 1500, 800))
    pygame.draw.rect(window, (0, 250, 0), (0, 700, 1500, 100))
    if sit == 0:
        pygame.draw.rect(window, (250, 0, 0), (x, y, 50, 100))
        if pos == 0:
            pygame.draw.rect(window, (0, 0, 0), (x - 15, y + 30, 20, 5))
        if pos == 1:
            pygame.draw.rect(window, (0, 0, 0), (x + 45, y + 30, 20, 5))
    pygame.event.get()
    keys = pygame.key.get_pressed()
#Keys
    if x <= 1440:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if sit == 0:
                x += 5
                pos = 1
            else:
                x += 2
    if x<=1440:
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            if sit == 0 and (keys[pygame.K_RIGHT] and keys[pygame.K_UP]):
                pygame.draw.line(window,(0,0,0),(x+25,y+10),(x+50,y-20),(8))
                pos = 2

    if x >= 10:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if sit == 0:
                x -= 5
                pos = 0
            else:
                x -= 2
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        if sit == 0 and (keys[pygame.K_LEFT] and keys[pygame.K_UP]):
            pygame.draw.line(window, (0, 0, 0), (x + 25, y + 10), (x - 20, y - 20), (8))
            pos = 4
        else:
            pos=0
    if keys[pygame.K_UP] and (pos!=2):
        if pos !=4:
            if sit == 0 and keys[pygame.K_UP]:
                pygame.draw.line(window, (0, 0, 0), (x + 25, y + 20), (x + 25, y - 40), (8))
                pos = 3
    if keys[pygame.K_UP] and keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        pygame.draw.rect(window,(0,0,150),(x+5,y+5,40,40))
        pygame.draw.rect(window,(0,0,0),(x+35,y+50,10,10))
#
    if jump == 0 and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
        if stanina > 100:
            jump = 1
            stanina -= 100

    if jump == 1:
        y -= 2 * g
        g -= 2
        if g <= 1:
            jump = 2
    if jump == 2:
        y += 2 * g
        g += 2
        if g >= 25:
            jump = 0
            y += 48
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        sit = 1
        pygame.draw.rect(window, (250, 0, 0), (x, y + 70, 50, 30))
    else:
        sit = 0
    if stanina >= 3:
        if keys[pygame.K_x]:
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                if keys[pygame.K_RIGHT] and x < 1440 and sit != 1:
                    x += 10
                    stanina -= 3
                if keys[pygame.K_LEFT] and x > 5 and sit != 1:
                    x -= 10
                    stanina -= 3
# СТРЕЛЬБАz
    if keys[pygame.K_z] and sit != 1:
        shoot = 1
    if shoot == 1:
        if pos == 0:
            pygame.draw.rect(window, (0,0,250), ((x - xs), (y + ys), 20, 6))
            xs += 20
        if pos == 1:
            if sit == 0:
                pygame.draw.rect(window, (0,0,250), ((x + xs), (y + ys), 20, 6))
            xs += 20
        if pos == 2:
            if sit == 0:
                pygame.draw.rect(window, (0, 0, 255), ((x + xs), (y - ys), 20, 6))
            xs+=20
            ys+=20
        if pos == 3:
            if sit == 0:
                pygame.draw.rect(window,(0,0,250),(x+25,y-ys,6,20))
            ys += 20
            xs +=1
        if pos == 4:
            if sit == 0:
                pygame.draw.rect(window,(0,0,250),(x-xs,y-ys,20,6))
            xs+=20
            ys+=20

        if (xs <= 0 or xs >= 1500) or (ys<=0 or ys >= 1500):
            shoot = 0
            xs = 0
            ys = 30
    pygame.draw.rect(window,(0,0,0),(1090,40,360,50))
    pygame.draw.rect(window, (0, 250, 0), (1100, 100, stanina, 20))
    pygame.draw.rect(window, (255, 30, 0), (1100, 50, HP, 40))
    if stanina < 350:
        stanina += 1
# ЗОМБИ
    if zombi == True:
        pygame.draw.rect(window, (56, 150, 100), (xz, yz, 50, 100))
        if xz > x:
            xz -= 2
            posz = 0
        if xz < x:
            xz += 2
            posz = 1
        if shootZ!=1 and shootZ!=2 and shootZ!=3 and shootZ!=4:
            shootZ = random.randint(1, 60)
            trap=random.randint(400,900)
        if shootZ == 1:
            if posz == 0:
                pygame.draw.rect(window, (0, 0, 255), ((xz - xsz), (yz + ysz), 20, 6))
                xsz += 20
            if posz == 1:
                pygame.draw.rect(window, (0, 0, 255), ((xz + xsz), (yz + ysz), 20, 6))
                xsz += 20
            if xsz <= 0 or xsz >= 1500:
                shootZ = 0
                xsz = 0
                ysz = 30
        if shootZ == 2:
            if posz==0:
                pygame.draw.line(window, (250, 0, 0), (0 , yz+30), (xz, yz+30), (time))
                xz+=2
            if posz==1:
                pygame.draw.line(window, (250, 0, 0), (1500 , yz+30), (xz, yz+30), (time))
                xz-=2
            time+=1
            if time>=60:
                time=1
                shootZ=1
        if shootZ == 3:
            pygame.draw.rect(window, (0, 50, 0), (xz, yz, 50, 100))
            if posz==0:
                if time <=30:
                    x+=10
                    if zombiHP<=1500:
                        zombiHP+=1
                else:
                    xz-=5
            if posz==1:
                if time <=30:
                    x-=10
                    if zombiHP<=1500:
                        zombiHP+=1
                else:
                    xz+=5
            time += 1
            if time >=100:
                shootZ=1
                time=1
        if shootZ == 4:
            pygame.draw.rect(window,(128,128,128),(trap,700,50,10))
            if x<=trap+50 and x>=trap:
                if y>=650:
                    HP-=5
            time+=1
            if time >=50:
                shootZ=1




# УРОН ОТ ЗОМБИ
    if shootZ==2 and time>=35 and sit!=1:
        HP-=10
    if sit != 1:
        if xz - xsz <= x + 1 and xz - xsz >= x - 50:
            if y <= yz + 30 and y >= yz - 60:
                HP -= 50
    if sit != 1:
        if xz + xsz <= x + 1 and xz + xsz >= x - 50:
            if y <= yz + 30 and y >= yz - 60:
                HP -= 50
# ВЫСТРЕЛЫ
        if shoot == 1:
            if pos == 0:
                if x - xs <= xz + 50 and x - xs >= xz - 1:
                    if yz <= y + 30 and yz >= y - 60:
                        zombiHP-=50
        if shoot == 1:
            if pos == 1:
                if x + xs <= xz + 1 and x + xs >= xz - 50:
                    if yz <= y + 30 and yz >= y - 60:
                        zombiHP-=50
    if zombiHP<=0:
        zombi=False
        xz = 10000
        yz = 10000
    if xz >= x and xz <= x + 50:
        if yz >= y and yz <= y + 100:
            HP -= 3
            zombiHP+=15
    while HP < 0:
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 1500, 800))
        pygame.display.update()
    if x>=1430:
        gameW=('1.2')
    pygame.draw.rect(window, (200, 0, 0), (xz - 30, yz - 50, zombiHP/10, 10))
    #pygame.draw.rect(window,(0,140,0),(zemx,zemy,500,50))
    pygame.display.update()