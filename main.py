import pygame


def draw(scr):
    scr.fill((0, 0, 0))
    for i in range(20):
        for j in range(20):
            if pos[i][j] == 'W':
                pygame.draw.rect(scr, (255, 255, 255), ((j * 40, i * 40), (40, 40)), 1)
            elif pos[i][j] == 'H':
                pygame.draw.circle(scr, (255, 0, 0), (40 * j + 20, 40 * i + 20), 20, 1)
            elif pos[i][j] == 'B':
                pygame.draw.circle(scr, (255, 255, 0), (40 * j + 20, 40 * i + 20), 20, 1)
            elif pos[i][j] == 'L':
                pygame.draw.circle(scr, (0, 255, 100), (40 * j + 20, 40 * i + 20), 10)
            elif pos[i][j] == 'P':
                pygame.draw.circle(scr, (255, 0, 0), (40 * j + 20, 40 * i + 20), 20, 1)
                pygame.draw.circle(scr, (0, 255, 100), (40 * j + 20, 40 * i + 20), 10)
            elif pos[i][j] == 'X':
                pygame.draw.circle(scr, (255, 255, 0), (40 * j + 20, 40 * i + 20), 20, 1)
                pygame.draw.circle(scr, (0, 255, 100), (40 * j + 20, 40 * i + 20), 10)


pos = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 'L', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
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
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    sy = i + 1
                    sx = j
                    ny = sy + 1
                    nx = sx
                    if (pos[i][j] == 'H' or pos[i][j] == 'P') and i < side - 1:
                        if pos[sy][sx] == 'B':
                            if pos[ny][nx] == ' ':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[ny][nx]
                            elif pos[ny][nx] == 'L':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = 'X', 'H', ' '
                        elif pos[sy][sx] == 'L':
                            pos[i][j], pos[sy][sx] = ' ', 'P'
                        elif pos[sy][sx] != 'W':
                            if pos[i][j] == 'P':
                                pos[i][j], pos[sy][sx] = 'L', 'H'
                            else:
                                pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_UP:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    sy = i - 1
                    sx = j
                    ny = sy - 1
                    nx = sx
                    if (pos[i][j] == 'H' or pos[i][j] == 'P') and i < side - 1:
                        if pos[sy][sx] == 'B':
                            if pos[ny][nx] == ' ':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[ny][nx]
                            elif pos[ny][nx] == 'L':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = 'X', 'H', ' '
                        elif pos[sy][sx] == 'L':
                            pos[i][j], pos[sy][sx] = ' ', 'P'
                        elif pos[sy][sx] != 'W':
                            if pos[i][j] == 'P':
                                pos[i][j], pos[sy][sx] = 'L', 'H'
                            else:
                                pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_LEFT:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    sy = i
                    sx = j - 1
                    ny = sy
                    nx = sx - 1
                    if (pos[i][j] == 'H' or pos[i][j] == 'P') and i < side - 1:
                        if pos[sy][sx] == 'B':
                            if pos[ny][nx] == ' ':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[ny][nx]
                            elif pos[ny][nx] == 'L':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = 'X', 'H', ' '
                        elif pos[sy][sx] == 'L':
                            pos[i][j], pos[sy][sx] = ' ', 'P'
                        elif pos[sy][sx] != 'W':
                            if pos[i][j] == 'P':
                                pos[i][j], pos[sy][sx] = 'L', 'H'
                            else:
                                pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_RIGHT:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    sy = i
                    sx = j + 1
                    ny = sy
                    nx = sx + 1
                    if (pos[i][j] == 'H' or pos[i][j] == 'P') and i < side - 1:
                        if pos[sy][sx] == 'B':
                            if pos[ny][nx] == ' ':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[ny][nx]
                            elif pos[ny][nx] == 'L':
                                pos[ny][nx], pos[sy][sx], pos[i][j] = 'X', 'H', ' '
                        elif pos[sy][sx] == 'L':
                            pos[i][j], pos[sy][sx] = ' ', 'P'
                        elif pos[sy][sx] != 'W':
                            if pos[i][j] == 'P':
                                pos[i][j], pos[sy][sx] = 'L', 'H'
                            else:
                                pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
    draw(screen)
    pygame.display.flip()
print('Ебать ты молодец')
