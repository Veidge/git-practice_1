import pygame
import sys

window_x = 900
window_y = 800
FPS = 60

class RotatingSprite:
    def __init__(self, image_path, position):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)
        self.angle = 0

    def update(self):
        self.angle += 1
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("You spin me right round, baby, right round")
    clock = pygame.time.Clock()

    sprite = RotatingSprite("sprite.png", (window_x // 2, window_y // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        sprite.update()
        sprite.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()