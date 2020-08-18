import sys
import pygame as pg

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


class ScreenObject:
    def __init__(self):
        pass

    def move(self):
        pass


def main():
    screen = pg.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    clock = pg.time.Clock()
    velocity = 10
    rect = pg.Rect(300, 300, 20, 20)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            # to move left
            rect.x = max(0, rect.x - velocity)
        if keys[pg.K_d]:
            # to move right
            size_x, _ = rect.size
            rect.x = min(screen.get_width() - size_x, rect.x + velocity)
        if keys[pg.K_w]:
            # to move up
            rect.y = max(0, rect.y - velocity)
        if keys[pg.K_s]:
            # to move down
            _, size_y = rect.size
            rect.y = min(screen.get_height() - size_y, rect.y + velocity)

        screen.fill((40, 40, 40))
        pg.draw.rect(screen, (150, 200, 20), rect)
        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
