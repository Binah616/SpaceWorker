import pygame


def name_input():
    pygame.draw.rect(screen, (0, 0, 0), ((395, 387), (210, 66)))
    pygame.draw.rect(screen, (255, 255, 255), ((395, 387), (210, 66)), 2)
    font = pygame.font.SysFont('Courier new', 20)
    name_text = font.render('Enter name', True, (255, 215, 0))
    screen.blit(name_text, ((140, 80), (210, 20)))
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 190, 32)
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
                else:
                    if len(text) < 15:
                        text += event.unicode
        pygame.draw.rect(screen, (0, 0, 0), ((395, 387), (210, 66)))
        pygame.draw.rect(screen, (255, 255, 255), ((395, 387), (210, 66)), 2)
        screen.blit(name_text, ((140, 80), (210, 20)))
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, (0, 100, 255), input_box, 2)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((100, 100, 100))
    name_input()
    pygame.quit()
