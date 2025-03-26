import pygame as pg,sys
import datetime as dt

pg.init()
screen = pg.display.set_mode((600,600))
mikki = pg.image.load('clock.png')
mikki = pg.transform.scale(mikki,(600,600))
minkol = pg.image.load('min_hand.png')
seckol = pg.image.load('sec_hand.png')
def sagtil(ekran,suret,uaqyt,gradus):
    ainsuret = pg.transform.rotate(suret,-(uaqyt%60)*6+gradus)
    nowsuret = ainsuret.get_rect(center = (300,300))
    ekran.blit(ainsuret,nowsuret)
while  True:
    for even in pg.event.get():
        if even.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.blit(mikki,(0,0))
    

    
    today = dt.datetime.now()

    secundes = today.second
    min = today.minute
    sagtil(screen,minkol,min,-50)
    sagtil(screen,seckol,secundes,51)
    pg.display.update()