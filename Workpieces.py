import pygame
import os


class Worker(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cur_image.subsurface((0, 0), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 40
        self.image = cur_image.subsurface((0, 0), (40, 40))

    def update(self, direction):
        dx = 0
        dy = 0
        if direction == 0:
            dy = 1
        elif direction == 1:
            dx = 1
        elif direction == 2:
            dx = -1
        elif direction == 3:
            dy = -1
        for i in range(1, 41, 1):
            self.rect.y += dy
            self.rect.x += dx
            dir_num = i % 5
            self.image = cur_image.subsurface((direction * 40, dir_num * 40), (40, 40))
            draw(screen)
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.wait(80)


def draw(scr):
    scr.fill((127, 127, 127))


def load_image(name, colorkey=None):
    fullname = os.path.join('/Users/Stepan/Desktop', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    cur_image = load_image('Worker.png')
    worker = Worker()
    all_sprites.add(worker)
    draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    worker.update(3)
                if event.key == pygame.K_RIGHT:
                    worker.update(1)
                if event.key == pygame.K_DOWN:
                    worker.update(0)
                if event.key == pygame.K_LEFT:
                    worker.update(2)
                draw(screen)
                all_sprites.draw(screen)
                pygame.display.flip()
