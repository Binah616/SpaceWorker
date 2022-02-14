import pygame
import os

SIDE = 21
FPS = 30


class Worker(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.start_pos()
        self.image = cur_image.subsurface((0, 0), (40, 40))
        self.frames = [[], [], [], []]
        self.cut_sheet(cur_image, 4, 5)
        self.image = self.frames[0][0]

    def cut_sheet(self, sheet, columns, rows):
        for j in range(columns):
            for i in range(rows):
                self.frames[j].append(sheet.subsurface((j * 40, i * 40), (40, 40)))

    def start_pos(self):
        self.rect.x = lvl.index('H') % 21 * 40
        self.rect.y = lvl.index('H') // 21 * 40

    def update(self, direction):
        dx = 0
        dy = 0
        if direction == 0:
            dy = 4
        elif direction == 1:
            dx = 4
        elif direction == 2:
            dx = -4
        elif direction == 3:
            dy = -4
        for i in range(1, 11):
            self.rect.y += dy
            self.rect.x += dx
            dir_num = i % 5
            self.image = self.frames[direction][dir_num]
            update_all()
            pygame.time.wait(75)


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


def draw(scr):
    scr.fill((0, 0, 0))
    pygame.draw.rect(scr, (98, 76, 54), ((840, 0), (160, 840)))
    for y in range(21):
        for x in range(21):
            if pos[y][x] == '*':
                pygame.draw.rect(scr, (7*16+8,8*16+6,6*16+11), ((x * 40, y * 40), (40, 40)))
            elif pos[y][x] == 'W':
                pygame.draw.rect(scr, (255, 255, 255), ((x * 40, y * 40), (40, 40)), 1)
            elif pos[y][x] == 'L':
                pygame.draw.rect(scr, (0, 255, 100), ((40 * x + 1, 40 * y + 1), (38, 38)), 3)
            elif pos[y][x] == ' ':
                pygame.draw.rect(scr, (0, 0, 0), ((x * 40, y * 40), (40, 40)))
            elif pos[y][x] == 'B':
                pygame.draw.circle(scr, (255, 255, 0), (40 * x + 20, 40 * y + 20), 20, 4)
            elif pos[y][x] == 'X':
                pygame.draw.rect(scr, (0, 255, 100), ((40 * x + 1, 40 * y + 1), (38, 38)), 3)
                pygame.draw.circle(scr, (255, 255, 0), (40 * x + 20, 40 * y + 20), 20, 4)
            elif pos[y][x] == 'P':
                pygame.draw.rect(scr, (0, 255, 100), ((40 * x + 1, 40 * y + 1), (38, 38)), 3)


def update_all():
    draw(screen)
    all_sprites.draw(screen)
    screen.blit(lvl_text, (850, 20))
    screen.blit(move_text, (850, 50))
    pygame.display.flip()
    clock.tick(FPS)


STATES = {121: [' ', 'H', 'W'], 122: [' ', 'H', ' '], 123: [' ', 'H', 'B'], 124: [' ', 'H', 'L'], 125: [' ', 'H', 'X'],
          132: [' ', 'H', 'B'], 134: [' ', 'H', 'X'],
          141: [' ', 'P', 'W'], 142: [' ', 'P', ' '], 143: [' ', 'P', 'B'], 144: [' ', 'P', 'L'], 145: [' ', 'P', 'X'],
          152: [' ', 'P', 'B'], 154: [' ', 'P', 'X'],
          221: ['L', 'H', 'W'], 222: ['L', 'H', ' '], 223: ['L', 'H', 'B'], 224: ['L', 'H', 'L'], 225: ['L', 'H', 'X'],
          232: ['L', 'H', 'B'], 234: ['L', 'H', 'L'],
          241: ['L', 'P', 'W'], 242: ['L', 'P', ' '], 243: ['L', 'P', 'B'], 244: ['L', 'P', 'L'], 245: ['L', 'P', 'X'],
          252: ['L', 'P', 'B'], 254: ['L', 'P', 'X']}

if __name__ == '__main__':
    pygame.init()
    GAME_FONT = pygame.font.SysFont('Courier', 24)
    size = width, height = 1000, 840
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('DockWorker v1.0')
    lvl_map = open('sokoban_levels_pack.txt', 'r')
    for i in range(1):
        lvl = lvl_map.readline()
    pos = [[' ' for i in range(21)] for j in range(21)]
    for i in range(21):
        for j in range(21):
            pos[i][j] = lvl[i * 21 + j]
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    cur_image = load_image('Worker.png')
    cur_lvl = 1
    move_cnt = 0
    worker = Worker()
    worker.start_pos()
    all_sprites.add(worker)
    lvl_text = GAME_FONT.render(f'Level {cur_lvl:4}', True, (255, 215, 0))
    move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
    update_all()
    while True:
        state = ''
        for i in range(SIDE):
            for j in range(SIDE):
                state += pos[i][j]
        if 'B' not in state:
            pygame.time.wait(1000)
            lvl = lvl_map.readline()
            for i in range(21):
                for j in range(21):
                    pos[i][j] = lvl[i * 21 + j]
            cur_lvl += 1
            move_cnt = 0
            lvl_text = GAME_FONT.render(f'Level {cur_lvl:4}', True, (255, 215, 0))
            move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
            worker.start_pos()
            update_all()
        for event in pygame.event.get():
            for k in range(SIDE ** 2):
                cur_y = k // SIDE
                cur_x = k % SIDE
                if pos[cur_y][cur_x] == 'H' or pos[cur_y][cur_x] == 'P':
                    next_y = cur_y
                    next_x = cur_x
                    after_y = cur_y
                    after_x = cur_x
                    if pos[cur_y][cur_x] == 'H':
                        level_state = 100
                    else:
                        level_state = 200
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    next_y += 1
                    after_y += 2
                    worker_state = 0
                elif event.key == pygame.K_UP:
                    next_y -= 1
                    after_y -= 2
                    worker_state = 3
                elif event.key == pygame.K_LEFT:
                    next_x -= 1
                    after_x -= 2
                    worker_state = 2
                elif event.key == pygame.K_RIGHT:
                    next_x += 1
                    after_x += 2
                    worker_state = 1

                if pos[next_y][next_x] == 'W':
                    level_state += 10
                elif pos[next_y][next_x] == ' ':
                    level_state += 20
                elif pos[next_y][next_x] == 'B':
                    level_state += 30
                elif pos[next_y][next_x] == 'L':
                    level_state += 40
                elif pos[next_y][next_x] == 'X':
                    level_state += 50

                if pos[after_y][after_x] == 'W':
                    level_state += 1
                elif pos[after_y][after_x] == ' ':
                    level_state += 2
                elif pos[after_y][after_x] == 'B':
                    level_state += 3
                elif pos[after_y][after_x] == 'L':
                    level_state += 4
                elif pos[after_y][after_x] == 'X':
                    level_state += 5

                if level_state in STATES.keys():
                    worker.update(worker_state)
                    pos[cur_y][cur_x], pos[next_y][next_x], pos[after_y][after_x] = STATES[level_state]
                    move_cnt += 1
                    move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
        update_all()
print('Победа!')
