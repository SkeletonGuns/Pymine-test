import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from world import World

def check_for_opengl_errors():
    error = glGetError()
    if error != GL_NO_ERROR:
        print(f"OpenGL Error: {error}")

def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Установите цвет фона
    gluPerspective(45, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Настройка освещения vhhjgdutxyhdyjdrfxcfhg
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    clock = pygame.time.Clock()
    player = Player()
    world = World()
    world.generate()  # Генерация мира

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        player.move(keys)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        world.draw()
        player.draw()
        check_for_opengl_errors()  # Проверка ошибок OpenGL
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

