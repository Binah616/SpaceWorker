import pygame
import os
import sqlite3

SIDE = 21
FPS = 30
CAGE = 40


class Button:
    def __init__(self, posit, text):
        self.x, self.y = posit
        self.font = GAME_FONT
        self.text = self.font.render(text, True, (255, 215, 0))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill((98, 76, 54))
        self.surface.blit(self.text, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def click(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                self.special()

    def show(self):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.text, (self.x, self.y))


class RestartButton(Button):
    def __init__(self, posit, text):
        super().__init__(posit, text)

    def special(self):
        global lvl_text, move_text, move_cnt
        move_cnt = 0
        move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
        new_lvl()
        worker.start_pos()
        update_all(screen)


class LoadButton(Button):
    def __init__(self, posit, text):
        super().__init__(posit, text)

    def special(self):
        global lvl, cur_name, move_cnt, cur_lvl, lvl_text, move_text, name_text
        name = name_input()
        if name != '':
            con = sqlite3.connect("Data/sokoban.db3")
            cur = con.cursor()
            res = cur.execute("""SELECT cur_level FROM players WHERE name = ?""", (name, )).fetchall()
            lvl = load_level(res[0][0])
            cur_lvl = res[0][0]
            cur_name = name
            lvl_text = GAME_FONT.render(f'Level {cur_lvl:4}', True, (255, 215, 0))
            move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
            name_text = GAME_FONT.render(f'{cur_name}', True, (255, 215, 0))
            move_cnt = 0
            new_lvl()
            worker.start_pos()
            update_all(screen)
        else:
            update_all(screen)


class Worker(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, CAGE, CAGE)
        self.image = worker_img.subsurface((0, 0), (CAGE, CAGE))
        self.frames = [[], [], [], []]
        self.cut_sheet(worker_img, 4, 5)
        self.image = self.frames[0][0]
        self.start_pos()

    def cut_sheet(self, sheet, columns, rows):
        for j in range(columns):
            for i in range(rows):
                self.frames[j].append(sheet.subsurface((j * CAGE, i * CAGE), (CAGE, CAGE)))

    def start_pos(self):
        self.rect.x = lvl.index('H') % 21 * CAGE
        self.rect.y = lvl.index('H') // 21 * CAGE
        self.image = self.frames[0][0]

    def update(self, direction, is_busy):
        dx = 0
        dy = 0
        bx = self.rect.x
        by = self.rect.y
        if direction == 0:
            dy = 4
            by += 40
        elif direction == 1:
            dx = 4
            bx += 40
        elif direction == 2:
            dx = -4
            bx -= 40
        elif direction == 3:
            dy = -4
            by -= 40
        if not is_busy:
            for i in range(1, 11):
                self.rect.y += dy
                self.rect.x += dx
                dir_num = i % 5
                self.image = self.frames[direction][dir_num]
                surface.blit(self.image, (self.rect.x, self.rect.y))
                update_all(screen)
                pygame.time.wait(60)
        else:
            mbx = bx
            mby = by
            for i in range(1, 11):
                self.rect.y += dy
                self.rect.x += dx
                mby += dy
                mbx += dx
                draw(screen)
                pygame.draw.rect(surface, (0, 0, 0), ((bx + 2, by + 2), (CAGE - 4, CAGE - 4)))
                dir_num = i % 5
                self.image = self.frames[direction][dir_num]
                surface.blit(self.image, (self.rect.x, self.rect.y))
                surface.blit(box_img, (mbx, mby))
                screen.blit(name_text, (880, 20))
                screen.blit(lvl_text, (850, 50))
                screen.blit(move_text, (850, 80))
                restart_button.show()
                load_button.show()
                pygame.display.flip()
                pygame.time.wait(75)


def load_image(name, colorkey=None):
    fullname = os.path.join('Data/sprites', name)
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
    surface.fill((0, 0, 0))
    pygame.draw.rect(scr, (98, 76, 54), ((840, 0), (160, 840)))
    for y in range(21):
        for x in range(21):
            if pos[y][x] == '*':
                scr.blit(grass_img, (x * CAGE, y * CAGE))
            elif pos[y][x] == 'W':
                scr.blit(wall_img, (x * CAGE, y * CAGE))
            elif pos[y][x] == 'L':
                pygame.draw.rect(scr, (0, 255, 100), ((CAGE * x + 1, CAGE * y + 1), (CAGE - 2, CAGE - 2)), 1)
            elif pos[y][x] == ' ':
                pygame.draw.rect(scr, (0, 0, 0), ((x * CAGE, y * CAGE), (CAGE, CAGE)))
            elif pos[y][x] == 'B':
                surface.blit(box_img, (x * CAGE, y * CAGE))
            elif pos[y][x] == 'X':
                surface.blit(box_img, (x * CAGE, y * CAGE))
                pygame.draw.rect(scr, (0, 255, 100), ((CAGE * x + 1, CAGE * y + 1), (CAGE - 2, CAGE - 2)), 1)
            elif pos[y][x] == 'P':
                pygame.draw.rect(scr, (0, 255, 100), ((CAGE * x + 1, CAGE * y + 1), (CAGE - 2, CAGE - 2)), 1)


def new_lvl():
    for i in range(21):
        for j in range(21):
            pos[i][j] = lvl[i * 21 + j]


def update_all(scr):
    draw(scr)
    all_sprites.draw(surface)
    scr.blit(name_text, (880, 20))
    scr.blit(lvl_text, (850, 50))
    scr.blit(move_text, (850, 80))
    restart_button.show()
    load_button.show()
    surface.blit(surface, size)
    pygame.display.flip()
    clock.tick(FPS)


def load_level(lvl_num):
    con = sqlite3.connect("Data/sokoban.db3")
    cur = con.cursor()
    res = cur.execute(f"""SELECT level_map FROM levels where id = {lvl_num - 1}""")
    for i in res:
        return i[0]


def name_input():
    pygame.draw.rect(screen, (0, 0, 0), ((395, 387), (210, 66)))
    pygame.draw.rect(screen, (255, 255, 255), ((395, 387), (210, 66)), 2)
    font = pygame.font.SysFont('Courier new', 20)
    name_text = font.render('Enter name', True, (255, 215, 0))
    screen.blit(name_text, ((445, 387), (210, 20)))
    clock = pygame.time.Clock()
    input_box = pygame.Rect(405, 407, 190, 32)
    text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return ''
                else:
                    if len(text) < 15:
                        text += event.unicode
        pygame.draw.rect(screen, (0, 0, 0), ((395, 387), (210, 66)))
        pygame.draw.rect(screen, (255, 255, 255), ((395, 387), (210, 66)), 2)
        screen.blit(name_text, ((445, 387), (210, 20)))
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, (0, 100, 255), input_box, 2)
        pygame.display.flip()
        clock.tick(30)


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
    pygame.mixer.init()
    pygame.mixer.music.load('Data/sountrack/Library_of_Ruina_OST_-_Yesod_Battle_1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    GAME_FONT = pygame.font.SysFont('Courier new', 24)
    size = width, height = 1000, 840
    screen = pygame.display.set_mode(size)
    surface = pygame.display.set_mode(size)
    surface.set_alpha(255)
    pygame.display.set_caption('DockWorker v1.0')
    pos = [[' ' for i in range(21)] for j in range(21)]
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    worker_img = load_image('Worker.png')
    grass_img = load_image('grass_1.png')
    wall_img = load_image('Wall.png')
    box_img = load_image('box_1.png')
    cur_lvl = 1
    lvl = load_level(cur_lvl)
    new_lvl()
    move_cnt = 0
    worker = Worker()
    worker.start_pos()
    all_sprites.add(worker)
    cur_name = 'NoName'
    lvl_text = GAME_FONT.render(f'Level {cur_lvl:4}', True, (255, 215, 0))
    move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
    name_text = GAME_FONT.render(f'{cur_name}', True, (255, 215, 0))
    restart_button = RestartButton((870, 110), 'Restart')
    load_button = LoadButton((860, 140), 'Load game')
    update_all(screen)
    while True:
        state = ''
        for i in range(SIDE):
            for j in range(SIDE):
                state += pos[i][j]
        if 'B' not in state:
            pygame.time.wait(100)
            if cur_lvl <= 100:
                move_cnt = 0
                cur_lvl += 1
                lvl = load_level(cur_lvl)
                new_lvl()
                lvl_text = GAME_FONT.render(f'Level {cur_lvl:4}', True, (255, 215, 0))
                move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
                worker.start_pos()
                update_all(screen)
            else:
                GAME_FONT = pygame.font.SysFont('Comic Sans MW', 50)
                pygame.draw.rect(screen, (0, 0, 0), ((200, 200), (600, 240)))
                end_text = GAME_FONT.render('Congratulations! You win!', True, (255, 215, 0))
                screen.blit(end_text, (275, 300))
                pygame.display.flip()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
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
                    if ((level_state % 100) // 10 == 3) or ((level_state % 100) // 10 == 5):
                        worker.update(worker_state, True)
                    else:
                        worker.update(worker_state, False)
                    pos[cur_y][cur_x], pos[next_y][next_x], pos[after_y][after_x] = STATES[level_state]
                    move_cnt += 1
                    move_text = GAME_FONT.render(f'Moves {move_cnt:4}', True, (255, 215, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                restart_button.click()
                load_button.click()
            if event.type == pygame.QUIT:
                pygame.quit()
        update_all(screen)
