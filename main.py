import pygame
import pygame.locals as pgv

pygame.init()

screen = pygame.display.set_mode((800, 600))
bounds = pygame.Rect(0, 0, 800, 600)

screen.fill((255, 0, 0))

esc = pygame.font.Font(None, 60)
esc_msg = "ESCAPE WHILE YOU STILL CAN"
esc_rect = pygame.Rect((0, 0), esc.size(esc_msg))
esc_rect.center = bounds.center
esc_image = esc.render(esc_msg, 0, (0, 255, 0), (255, 0, 0))

screen.blit(esc_image, esc_rect)
pygame.display.flip()


while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pgv.K_ESCAPE]:
        break
