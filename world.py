from OpenGL.GL import *
from OpenGL.GLU import *

class World:
    def __init__(self):
        self.blocks = []

    def generate(self):
        # Генерация блоков (например, простая плоскость)
        for x in range(-5, 5):
            for z in range(-5, 5):
                self.blocks.append((x, 0, z))

    def draw(self):
        glBegin(GL_QUADS)
        for block in self.blocks:
            x, y, z = block
            glVertex3f(x - 0.5, y, z - 0.5)
            glVertex3f(x + 0.5, y, z - 0.5)
            glVertex3f(x + 0.5, y, z + 0.5)
            glVertex3f(x - 0.5, y, z + 0.5)
        glEnd()

# Вызов генерации мира
world = World()
world.generate()
