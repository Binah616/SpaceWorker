import pygame


# class WorkerDownSprite(pygame.sprite.Sprite):
#     def __init__(self, sheet, columns, rows, x, y):
#         super().__init__()
#         self.frames = []
#         self.cut_sheet(sheet, columns, rows)
#         self.cur_frame = 0
#         self.image = self.frames[self.cur_frame]
#         self.rect = self.rect.move(x, y)
#
#     def cut_sheet(self, sheet, columns, rows):
#         self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
#                                 sheet.get_height() // rows)
#         for j in range(rows):
#             for i in range(columns):
#                 frame_location = (self.rect.w * i, self.rect.h * j)
#                 self.frames.append(sheet.subsurface(pygame.Rect(
#                     frame_location, self.rect.size)))
#
#     def update(self):
#         self.cur_frame = (self.cur_frame + 1) % len(self.frames)
#         self.image = self.frames[self.cur_frame]
class Worker(pygame.sprite.Sprite):
    image = pygame.image.load('/Users/Stepan/Downloads/Worker.png/')

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Worker.image.blit(screen, (0, 0), (40, 40))

    


# worker = WorkerDownSprite(image, 1, 5, 40, 40)


def draw(scr):
    scr.fill((0, 0, 0))
    for y in range(21):
        for x in range(21):
            if pos[y][x] == 'W':
                pygame.draw.rect(scr, (255, 255, 255), ((x * 40, y * 40), (40, 40)), 1)
            elif pos[y][x] == 'H':
                pygame.draw.circle(scr, (255, 0, 0), (40 * x + 20, 40 * y + 20), 20, 1)
            elif pos[y][x] == 'B':
                pygame.draw.circle(scr, (255, 255, 0), (40 * x + 20, 40 * y + 20), 20, 1)
            elif pos[y][x] == 'L':
                pygame.draw.circle(scr, (0, 255, 100), (40 * x + 20, 40 * y + 20), 10)
            elif pos[y][x] == 'P':
                pygame.draw.circle(scr, (255, 0, 0), (40 * x + 20, 40 * y + 20), 20, 1)
                pygame.draw.circle(scr, (0, 255, 100), (40 * x + 20, 40 * y + 20), 10)
            elif pos[y][x] == 'X':
                pygame.draw.circle(scr, (255, 255, 0), (40 * x + 20, 40 * y + 20), 20, 1)
                pygame.draw.circle(scr, (0, 255, 100), (40 * x + 20, 40 * y + 20), 10)


states = {121: [' ', 'H', 'W'], 122: [' ', 'H', ' '], 123: [' ', 'H', 'B'], 124: [' ', 'H', 'L'], 125: [' ', 'H', 'X'],
          132: [' ', 'H', 'B'], 134: [' ', 'H', 'X'],
          141: [' ', 'P', 'W'], 142: [' ', 'P', ' '], 143: [' ', 'P', 'B'], 144: [' ', 'P', 'L'], 145: [' ', 'P', 'X'],
          152: [' ', 'P', 'B'], 154: [' ', 'P', 'X'],
          221: ['L', 'H', 'W'], 222: ['L', 'H', ' '], 223: ['L', 'H', 'B'], 224: ['L', 'H', 'L'], 225: ['L', 'H', 'X'],
          232: ['L', 'H', 'B'], 234: ['L', 'H', 'L'],
          241: ['L', 'P', 'W'], 242: ['L', 'P', ' '], 243: ['L', 'P', 'B'], 244: ['L', 'P', 'L'], 245: ['L', 'P', 'X'],
          252: ['L', 'P', 'B'], 254: ['L', 'P', 'X']}

pos = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 840
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    draw(screen)
lvl_map = open('sokoban_levels_pack.txt', 'r')
for i in range(1):
    lvl = lvl_map.readline()
for i in range(21):
    for j in range(21):
        pos[i][j] = lvl[i * 21 + j]
side = 21
fps = 30
clock = pygame.time.Clock()
while True:
    state = ''
    for i in range(side):
        for j in range(side):
            state += pos[i][j]
    if 'B' not in state:
        lvl = lvl_map.readline()
        for i in range(21):
            for j in range(21):
                pos[i][j] = lvl[i * 21 + j]
        draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    for event in pygame.event.get():
        for k in range(side ** 2):
            cur_y = k // side
            cur_x = k % side
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
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_y += 1
                after_y += 2
            if event.key == pygame.K_UP:
                next_y -= 1
                after_y -= 2
            if event.key == pygame.K_LEFT:
                next_x -= 1
                after_x -= 2
            if event.key == pygame.K_RIGHT:
                next_x += 1
                after_x += 2

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

            if level_state in states.keys():
                pos[cur_y][cur_x], pos[next_y][next_x], pos[after_y][after_x] = states[level_state]
    draw(screen)
    pygame.display.flip()
    clock.tick(fps)
print('Победа!')
