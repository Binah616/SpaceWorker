import pygame


def draw(scr):
    scr.fill((0, 0, 0))
    for y in range(20):
        for x in range(20):
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


states = {
    121: [' ', 'H', 'W'],
    122: [' ', 'H', ' '],
    123: [' ', 'H', 'B'],
    124: [' ', 'H', 'L'],
    125: [' ', 'H', 'X'],
    132: [' ', 'H', 'B'],
    134: [' ', 'H', 'X'],
    141: [' ', 'P', 'W'],
    142: [' ', 'P', ' '],
    143: [' ', 'P', 'B'],
    144: [' ', 'P', 'L'],
    145: [' ', 'P', 'X'],
    152: [' ', 'P', 'B'],
    154: [' ', 'P', 'X'],

    221: ['L', 'H', 'W'],
    222: ['L', 'H', ' '],
    223: ['L', 'H', 'B'],
    224: ['L', 'H', 'L'],
    225: ['L', 'H', 'X'],
    232: ['L', 'H', 'B'],
    234: ['L', 'H', 'L'],
    241: ['L', 'P', 'W'],
    242: ['L', 'P', ' '],
    243: ['L', 'P', 'B'],
    244: ['L', 'P', 'L'],
    245: ['L', 'P', 'X'],
    252: ['L', 'P', 'B'],
    254: ['L', 'P', 'L']
}

pos = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 'L', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'L', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    draw(screen)
side = 20
is_win = False
running = True
while running:
    state = ''
    for i in range(side):
        for j in range(side):
            state += pos[i][j]
    if 'B' not in state:
        is_win = True
        break
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
print('Победа!')
