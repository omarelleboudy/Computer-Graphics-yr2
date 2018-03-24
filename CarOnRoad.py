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
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
#################################################################################
x=0
f=True
z=0


def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global f
    global z
    glMatrixMode(GL_MODELVIEW)

    #ROAD
    glLoadIdentity()
    glColor3f(.1, .1, .1)
    glTranslate(0, -1.80, 0)
    glScale(50, .5, 10)
    glutSolidCube(1)


    #LOWER HALF
    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1,.25,.5)
    glutSolidCube(5)
    #UPPER HALF
    glLoadIdentity()
    glColor3f(0,0,1)
    glTranslate(x,0,0)
    glTranslate(0,1.25,0)
    glScale(.5,.25,.5)
    glutSolidCube(5)

    #Tire1
    glColor(0,0,1)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)
    #Tire2
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)
    #Tire3
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)
    #Tire4
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    #LIGHT1
    glColor(1,1,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,.4)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)
    #LIGHT2
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2.2,-.3,-.4)
    glScale(.25,1,1)
    glutSolidSphere(.3,20,20)
    #Moving Forwards and Backwards
    if x > 7:
      f = False

    if x < -14:
        f = True

    if f:
        x+=.005
        z-=1
    else:
        x-=.005
        z+=1


    glFlush()



###########################

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"CarOnRoad")
myinit()
glutDisplayFunc(draw1)
glutIdleFunc(draw1)
glutMainLoop()

