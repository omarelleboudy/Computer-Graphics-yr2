from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
#################################################################################
def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT)
    # glOrtho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
############################################################################
def draw1():

    #FIRST CHAIR
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1,1,1)
    glLineWidth(2)
    glTranslate(1,0,0)
    glScale(3,.25,3)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    # glLoadIdentity()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1,1,1)
    glTranslate(-.25,0,-3.25)
    glScale(3,2.5,.5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(-.31, -1.5, 1.20)
    glScale(1, 5, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(2.20, -1.5, 1.20)
    glScale(1, 5, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(1.75, -1.5, -2.20)
    glScale(1, 3.8, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()


    #SECOND CHAIR

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1,1,1)
    glLineWidth(2)
    glTranslate(5.2,0,0)
    glScale(2.5,.25,3)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(4.5, 0, -3.25)
    glScale(3, 2.5, .5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(6.2, -1.5, 1.20)
    glScale(1, 5, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(4, -1.5, 1.20)
    glScale(1, 5, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(6, -1.5, -2.20)
    glScale(1, 3.8, 1)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()





    glFlush()





###########################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Chairs")
glutDisplayFunc(draw1)
# glutIdleFunc(draw1)
myinit()
glutMainLoop()




