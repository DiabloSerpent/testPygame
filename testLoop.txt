import pygame
import pygame.locals as pgv

pygame.init()

screen = pygame.display.set_mode((800, 600))
bounds = pygame.Rect(0, 0, 800, 600)
ticker = pygame.time.Clock()
running = True

screen.fill((255, 0, 0))


class Message:
    def __init__(self, msg):
        self.font = pygame.font.Font(None, 60)
        self.msg = msg
        self.rect = pygame.Rect((0, 0), self.font.size(msg))
        self.image = pygame.Surface((0, 0))

    def create_image(self, text, background):
        self.image = self.font.render(self.msg, 0, text, background)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


esc = pygame.font.Font(None, 60)
esc_msg = "ESCAPE WHILE YOU STILL CAN"
esc_rect = pygame.Rect((0, 0), esc.size(esc_msg))
esc_rect.center = bounds.center
esc_image = esc.render(esc_msg, 0, (0, 255, 0), (255, 0, 0))

screen.blit(esc_image, esc_rect)

srsly = pygame.font.Font(None, 60)
srsly_msg = "EPA ESC APE"
srsly_rect = pygame.Rect((0, 0), srsly.size(srsly_msg))
srsly_rect.center = bounds.center
srsly_rect.move_ip(0, 100)
srsly_image = esc.render(srsly_msg, 0, (0, 0, 255), (255, 0, 0))

screen.blit(srsly_image, srsly_rect)

esc2 = Message("ESC")
esc2.rect.center = bounds.center
esc2.rect.move_ip(0, -150)
esc2.create_image((0, 0, 255), (255, 0, 0))

esc2.draw(screen)

pygame.display.flip()


while running:
    for ev in pygame.event.get():
        if ev.type == pgv.KEYDOWN:
            if ev.key == pgv.K_ESCAPE:
                running = False
        elif ev.type == pgv.QUIT:
            running = False
    ticker.tick(60)
