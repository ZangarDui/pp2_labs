import pygame as pg,sys

pg.init()
screen = pg.display.set_mode((600,400))
clock = pg.time.Clock()
coord = [400,400]
radius = 20
while True:
    for even in pg.event.get():
        if even.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((255,255,255))

    pg.draw.circle(screen,(255,0,0),(coord[0],coord[1]),radius)

    pressed = pg.key.get_pressed()  
    if pressed[pg.K_UP]:
        if coord[1] - radius- 20 >= 0:
            coord[1] -= 20
    if pressed[pg.K_DOWN]:
        if coord[1] + radius + 20 <= 400:
            coord[1] += 20
    if pressed[pg.K_RIGHT]:
        if coord[0] + radius + 20 <= 600:
            coord[0] += 20
    if pressed[pg.K_LEFT]:
        if coord[0] - radius- 20 >= 0:
            coord[0] -= 20

    clock.tick(60)
    pg.display.update() 