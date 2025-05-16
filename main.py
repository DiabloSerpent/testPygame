import pygame
import pygame.locals as pgv
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
bounds = pygame.Rect(0, 0, 800, 600)
ticker = pygame.time.Clock()
running = False

screen.fill((255, 0, 0))

def myAtan2(x, y):
    result = math.atan2(y, x)
    '''if x != 0:
        if y == 0 and x < 0:
            result = math.pi
        else:
            result = math.atan(y/x)
    else:
        result = math.pi / 2
        if y >= 0:
            # Unnecesarily big brain coding
            result *= 3'''
    if result < 0:
        result += math.pi * 2
            
    print(f"({x}, {y}): {math.degrees(result)}")
    print("math.atan2():", math.degrees(math.atan2(y, x)))

print("Axes:")
myAtan2(1, 0)  # 0
myAtan2(-1, 0)  # 180
myAtan2(0, 1)  # 270
myAtan2(0, -1)  # 90
print("\nDiagonals:")
myAtan2(1, -1)  # 315
myAtan2(-1, -1)  # 225
myAtan2(-1, 1)  # 135
myAtan2(1, 1)  # 45

while running:
    for ev in pygame.event.get():
        if ev.type == pgv.KEYDOWN:
            if ev.key == pgv.K_ESCAPE:
                running = False
        elif ev.type == pgv.QUIT:
            running = False
    ticker.tick(60)
