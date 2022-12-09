import pymunk
import pygame
import pymunk.pygame_util
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pymunk.pygame_util.positive_y_is_up = True
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0,-100

body = pymunk.Body(1, 20) # Body(mass, moment, body_type)
body.position = 50,550   # body_type: DYNAMIC, KINEMATIC, STATIC
shape = pymunk.Circle(body, 10, (0,0)) # Circle(body, r, offset)
space.add(body, shape) # add(*objs)

clock = pygame.time.Clock()

vs = [(-23,26), (23,26), (0,-26)] #삼각형
moment = pymunk.moment_for_poly(1, vs) #모멘트를 자동 설정해주는 함수
body2 = pymunk.Body(1, moment)
body2.position = 100, 550
shape2 = pymunk.Poly(body2, vs)
shape2.friction   = 0. #마찰
shape2.elasticity = 0.5 #탄성력
space.add(body2, shape2)

body3 = pymunk.Body(body_type = pymunk.Body.STATIC) #바닥은 움직이지 않으니까 static
body3.position = 300, 100
shape3 = pymunk.Poly(body3,
[(-300, 0), (300, 0), (300, -2), (-300, -2)]) #직사각형 형태
shape3.friction   = 0.
shape3.elasticity = 0.5
space.add(body3, shape3)

body2.apply_impulse_at_local_point((60, 00), (0, 10)) #삼각형에 force를 가함. *local point임. func(impulse Vector, local point)


for i in range(0, 500):
    screen.fill((255,255,255))
    space.debug_draw(draw_options)
    space.step(1/50.0) # update space, step(dt)
    pygame.display.flip()
    clock.tick(50)

pygame.quit()