import pygame


def draw(scr):
    scr.fill((0, 0, 0))
    for i in range(20):
        for j in range(20):
            if pos[i][j] == 'W':
                pygame.draw.rect(scr, (255, 255, 255), ((j * 40, i * 40), (40, 40)), 1)
            elif pos[i][j] == '0':
                pygame.draw.circle(scr, (255, 0, 0), (40 * j + 20, 40 * i + 20), 20, 1)
            elif pos[i][j] == 'B':
                pygame.draw.circle(scr, (255, 255, 0), (40 * j + 20, 40 * i + 20), 20, 1)
            elif pos[i][j] == 'L':
                pygame.draw.circle(scr, (0, 255, 100), (40 * j + 20, 40 * i + 20), 10)


pos = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'L', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
       [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' '],
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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    if pos[i][j] == '0' and i < side - 1:
                        sy = i + 1
                        sx = j
                        if pos[sy][sx] == 'B':
                            print('mini_success')
                            if pos[sy + 1][sx] == ' ':
                                print('success')
                                pos[sy + 1][sx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[sy + 1][sx]
                        elif pos[sy][sx] != 'W':
                            pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_UP:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    if pos[i][j] == '0' and i > 0:
                        sy = i - 1
                        sx = j
                        if pos[sy][sx] == 'B':
                            print('mini_success')
                            if pos[sy - 1][sx] == ' ':
                                print('success')
                                pos[sy - 1][sx], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[sy - 1][sx]
                        elif pos[sy][sx] != 'W':
                            pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_LEFT:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    if pos[i][j] == '0' and j > 0:
                        sy = i
                        sx = j - 1
                        if pos[sy][sx] == 'B':
                            print('mini_success')
                            if pos[sy][sx - 1] == ' ':
                                print('success')
                                pos[sy][sx - 1], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[sy][sx - 1]
                        elif pos[sy][sx] != 'W':
                            pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
            if event.key == pygame.K_RIGHT:
                for k in range(side ** 2):
                    i = k // side
                    j = k % side
                    if pos[i][j] == '0' and j < side - 1:
                        sy = i
                        sx = j + 1
                        if pos[sy][sx] == 'B':
                            print('mini_success')
                            if pos[sy][sx + 1] == ' ':
                                print('success')
                                pos[sy][sx + 1], pos[sy][sx], pos[i][j] = pos[sy][sx], pos[i][j], pos[sy][sx + 1]
                        elif pos[sy][sx] != 'W':
                            pos[i][j], pos[sy][sx] = pos[sy][sx], pos[i][j]
                        break
    draw(screen)
    pygame.display.flip()
