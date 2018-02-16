from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as mp
from math import *


def draw1():
    glClearColor(1,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,1,1)
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2d(0.5,0.5)
    glVertex2d(0.5,0)
    glVertex2d(-0.5,0)
    glVertex2d(-0.5,0.5)
    glEnd()



    glBegin(GL_POLYGON)
    glColor(0,0,0)
    r = 0.1
    for th in mp.arange(0, 2*pi, 0.01):
        x = r * cos(th) + 0.3
        y = r * sin(th) + 0.3

        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    r = 0.1
    for th in mp.arange(0, 2 * pi, 0.01):
        x = r * cos(th) - 0.3
        y = r * sin(th) + 0.3

        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    r = 0.1
    for th in mp.arange(0, 2 * pi, 0.01):
        x = 2*r * cos(th)
        y = 0.5*r * sin(th) + 0.1

        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1,1,1)
    glVertex2d(0.15,0)
    glVertex2d(0.15,-0.2)
    glVertex2d(-0.15,-0.2)
    glVertex2d(-0.15,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.75,-0.2)
    glVertex2d(0.75,-0.2)
    glVertex2d(0.75,-0.8)
    glVertex2d(-0.75,-0.8)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0)
    glVertex2d(-0.75, -0.2)
    glVertex2d(-0.85, -0.2)
    glVertex2d(-0.85, -0.6)
    glVertex2d(-0.75, -0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    glVertex2d(0.75, -0.2)
    glVertex2d(0.85, -0.2)
    glVertex2d(0.85, -0.6)
    glVertex2d(0.75, -0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0,0,0)
    glVertex2d(0.11,-0.8)
    glVertex2d(0.11, -1)
    glVertex2d(0.05, -1)
    glVertex2d(0.05,-0.8)


    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.12,-0.8)
    glVertex2d(-0.12, -1)
    glVertex2d(-0.05, -1)
    glVertex2d(-0.05,-0.8)


    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.11, -0.8)
    glVertex2d(0, -0.8)
    glEnd()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b";_____;")
glutDisplayFunc(draw1)
glutMainLoop()

