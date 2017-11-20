import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import socket
from struct import *

UDP_IP = "192.168.1.103"
print("Receiver IP: ", UDP_IP)
# UDP_PORT = 6000
UDP_PORT = 5050
print("Port: ", UDP_PORT)
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

pygame.joystick.init()
pygame.joystick.Joystick(0).init()
vertices = [[1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, -1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
            ]

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def rotation():
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    # print "received message:", data
    # print "received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12)
    '''print("received message: ",
          "%1.4f" % unpack_from('!f', data, 0), "%1.4f" % unpack_from('!f', data, 4),
          "%1.4f" % unpack_from('!f', data, 8), "%1.4f" % unpack_from('!f', data, 12),
          "%1.4f" % unpack_from('!f', data, 16), "%1.4f" % unpack_from('!f', data, 20),
          "%1.4f" % unpack_from('!f', data, 24), "%1.4f" % unpack_from('!f', data, 28),
          "%1.4f" % unpack_from('!f', data, 32))'''
    x = "%1.4f" % unpack_from('!f', data, 24)
    y = "%1.4f" % unpack_from('!f', data, 28)
    z = "%1.4f" % unpack_from('!f', data, 32)
    print(x,y,z)
    return (x, y, z)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glColor3f(1, 1, 0)
    glEnd()


def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(50, 1, 1, 100)
    glTranslatef(0, 0, -20)

    x_c = 0
    y_c = 0
    x = 0
    y = 0
    while True:
       # glTranslatef(0, 0, -100)

        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        # print "received message:", data
        # print "received message: %1.3f %1.3f %1.3f %1.3f", unpack_from ('!f', data, 0), unpack_from ('!f', data, 4), unpack_from ('!f', data, 8), unpack_from ('!f', data, 12)
        '''print("received message: ",
              "%1.4f" % unpack_from('!f', data, 0), "%1.4f" % unpack_from('!f', data, 4),
              "%1.4f" % unpack_from('!f', data, 8), "%1.4f" % unpack_from('!f', data, 12),
              "%1.4f" % unpack_from('!f', data, 16), "%1.4f" % unpack_from('!f', data, 20),
              "%1.4f" % unpack_from('!f', data, 24), "%1.4f" % unpack_from('!f', data, 28),
              "%1.4f" % unpack_from('!f', data, 32))'''
        x_m = "%1.4i" % unpack_from('!f', data, 0);
        y_m = "%1.4i" % unpack_from('!f', data, 4);
        z_m = "%1.4i" % unpack_from('!f', data, 8);

        x = "%1.4i"%unpack_from('!f', data, 24);
        y = "%1.4i" % unpack_from('!f', data, 28)
        z = "%1.4i" % unpack_from('!f', data, 32)

        y=int(y)
        x=int(x)
        z=int(z)

        x_m=int(x_m)
        y_m = int(y_m)
        z_m = int(z_m)
        glRotate(4,y*30,x*30,z*30);

      #  glTranslatef(x_m*0.0001, y_m*0.0001, -80)
        print(x_m,y_m)

        for vertex in vertices:
            vertex[0]=vertex[0]+x_m
            vertex[1]=vertex[1]+y_m
           # vertex[2] = vertex[2] + z_m
      #  glTranslatef(0,0,100)

        # glTranslatef(y_c,x_c,1)
        # glPopMatrix();
        glTranslatef(x_m,y_m,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(0)


main()


