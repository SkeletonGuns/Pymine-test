import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Player:
    def __init__(self):
        self.position = [0, 0, 0]
        self.size = 0.5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.position[0] -= 0.1
        if keys[pygame.K_RIGHT]:
            self.position[0] += 0.1
        if keys[pygame.K_UP]:
            self.position[2] -= 0.1
        if keys[pygame.K_DOWN]:
            self.position[2] += 0.1

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glBegin(GL_QUADS)
        for x in [-self.size, self.size]:
            for z in [-self.size, self.size]:
                glVertex3f(x, 0, z)
        glEnd()
        glPopMatrix()
