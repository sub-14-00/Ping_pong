from pygame import *
from ball import*
game = True

W = 1366
H = 768
win = display.set_mode((W,H),FULLSCREEN)

class Main(sprite.Sprite):
    def __init__(self,x,y,pic,W,H,speed,face):
        super().__init__()
        self.pic = image.load(pic)
        self.pic = transform.scale(self.pic,(W,H))
        self.rect = Rect(x,y,W,H)
    def reset(self):
        win.blit(self.pic,(self.rect.x,self.rect.y))

class Ball(Main):
    def update():
        if self.face == 'right':
            self.rect.x +=10
            if self.rect.x>=W:
                self.face = 'left'
        if self.face == 'left':
            self.rect.x-=10
            if self.rect.x< 0:
                self.face = 'right'

        if self.face == 'up':
            self.rect.y+=10
            if self.rect.y>=H:
                self.face = 'dawn'
        if self.face == 'dawn':
            self.rect.y-=10
            if self.rect.y < 0:
                self.face = 'up'

        

BALL = Ball(300,300,'ball.png',40,40,50,'left')

def control():
    global game
    for e in event.get():
        if e.type == 2:
            if e.key == K_ESCAPE:
                game = False
        if e.type == 12:
            game = False



while game:
    control()
    win.fill((255,255,255))
    BALL.update()
    BALL.reset()











    display.update()
