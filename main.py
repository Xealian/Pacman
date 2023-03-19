import pygame as pg 
from random import randint
pg.init()
tiles=30
window=pg.display.set_mode((tiles*28,tiles*29))
pg.display.set_icon(pg.image.load("left.png"))
pg.display.set_caption('pacman')
class Game_sprite():
    def __init__(self, image, x,y , w,h, speed):
        self.image=pg.transform.scale(pg.image.load(image),(w,h))
        self.w=w
        self.h=h
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(Game_sprite):
    def control(self, walls):
        global timer, coins
        for i in coins:
            if pg.sprite.collide_rect(self, i):
                coins.remove(i)

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= self.speed
            if timer % 7 == 0:
                self.image = pg.transform.scale(
                pg.image.load('left.png'), (self.w, self.h)
    ) 
            if timer % 14 == 0:
                    self.image = pg.transform.scale(
                    pg.image.load('left2.png'), (self.w, self.h)
    )
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x += self.speed

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += self.speed
            if timer % 7 == 0:
                self.image = pg.transform.scale(
                pg.image.load('right.png'), (self.w, self.h)
    )
            if timer % 14==0:
                self.image = pg.transform.scale(
                pg.image.load('right2.png'), (self.w, self.h)
    )
            for i in walls:
                if pg.sprite.collide_rect(self, i):
                    self.rect.x-= self.speed

 

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= self.speed

            if timer % 7 == 0:
                self.image = pg.transform.scale(
                pg.image.load('up.png'), (self.w, self.h)
    )
            if timer % 14==0:
                self.image = pg.transform.scale(
                pg.image.load('up2.png'), (self.w, self.h)
    )
            for i in walls:
                if pg.sprite.collide_rect(self, i):
                    self.rect.y+=self.speed

 

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += self.speed
            if timer % 7 == 0:
                self.image = pg.transform.scale(
                pg.image.load("down.png"), (self.w, self.h)
    )
            if timer % 14==0:
                self.image = pg.transform.scale(
                pg.image.load("down2.png"), (self.w, self.h)
    )
            for i in walls:
                if pg.sprite.collide_rect(self, i):
                    self.rect.y -= self.speed 

        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.rect.x<0:
            self.rect.x=tiles * 27

        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.rect.x>tiles*28:
            self.rect.x=0

class Enemy(Game_sprite):
    def __init__(self,img,x,y,w,h,speed,diraction):
        super().__init__(img,x,y,w,h,speed)
        self.diraction=diraction
    def move(self):
        global walls

        if self.diraction==0:
            self.rect.x+=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x-=self.speed
                    self.diraction=randint(2,3)
            if self.rect.x>tiles*28:
                self.diraction=1

        if self.diraction==1:
            self.rect.x-=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x+=self.speed
                    self.diraction=randint(2,3)
            if self.rect.x<0:
                self.diraction=0

        if self.diraction==2:
            self.rect.y-=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y+=self.speed
                    self.diraction=randint(0,1)
            if self.rect.y<0:
                self.diraction=3

        if self.diraction==3:
            self.rect.y+=self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y-=self.speed
                    self.diraction=randint(0,1)
            if self.rect.y>tiles*28:
                self.diraction=2

list_wall=[
'1111111111111111111111111111',
'1000000000000110000000000001',
'1011110111110110111110111101',
'1011110111110110111110111101',
'1011110111110110111110111101',
'1000000000000000000000000001',
'1011110110111111110110111101',
'1011110110111111110110111101',
'1000000110000110000110000001',
'1111110110100000010110111111',
'1111110110111001110110111111',
'1111110110100000010110111111',
'0000000000100000010000000000',
'1111110110100000010110111111',
'1111110110111111110110111111',
'1111110110000000000110111111',
'1111110110111111110110111111',
'1111110110111111110110111111',
'1000000000000110000000000001',
'1011110111110110111110111101',
'1011110111110110111110111101',
'1000110000000000000000110001',
'1110110110111111110110110111',
'1110110110111111110110110111',
'1000000110000110000110000001',
'1011111111110110111111111101',
'1011111111110110111111111101',
'1000000000000110000000000001',
'1111111111111111111111111111',
]
walls=[]
floors=[]
coins = []
enemies=[]
enemies_img=['blue.png','red.png','yellow.png']
for i in range(3):
    enemies.append(Enemy(enemies_img[i],tiles*13,tiles*13,tiles,tiles,tiles//10,2))

for i in range(len(list_wall)):
    for j in range(len(list_wall[i])):
        print(list_wall[i][j])
        if list_wall[i][j]=='1':
            walls.append(Game_sprite('wall.jpg',j*tiles,i*tiles,tiles,tiles,0))
        if list_wall[i][j]=='0':
            floors.append(
            (Game_sprite('floor.jpg',j*tiles,i*tiles,tiles,tiles,0))
            )
            coins.append(
            (Game_sprite('coin.png',j*tiles+tiles//4,i*tiles+tiles//4,tiles//2,tiles//2,0))
            )
player=Player('right.png',tiles,tiles,tiles,tiles,tiles//9)
timer=1
game=True
game_over='gameover.png'
while game:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            exit()
    pg.time.Clock().tick(120)
    for i in walls:
        i.reset()
    for i in floors:
        i.reset()
    for i in coins:
        i.reset()
    for i in enemies:
        i.reset()
        i.move()
        if pg.sprite.collide_rect(i,player):
            game=False
    if len(coins)==0:
        game_over='ez.png'
        game=False
    timer +=1
    player.reset()
    player.control(walls)
    pg.display.flip()
back=Game_sprite(game_over,0,0,tiles*28,tiles*29,0)
while 1:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            exit()
    pg.time.Clock().tick(120)
    back.reset()
    pg.display.flip()