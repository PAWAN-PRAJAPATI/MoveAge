import pygame
import serial
import struct
import pyautogui,sys
import pygame
from time import sleep
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import socket
from struct import *
import math
from pynput import keyboard

pyautogui.MINIMUM_DURATION+=0
pyautogui.MINIMUM_SLEEP=0
pyautogui.PAUSE=0
UDP_IP = "192.168.1.104"
print("Receiver IP: ", UDP_IP)
# UDP_PORT = 6000
UDP_PORT = 5050
print("Port: ", UDP_PORT)
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

gameExit = False

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys # stop listener
    global gameExit
    if (k=='-'):
        print('Key pressed: ' + k)
        gameExit=True
    elif(k=='*'):
        gameExit=False
    elif(k=='+'):
        pyautogui.click(button='left')
    elif(k=='/'):
        pyautogui.click(button='right')
    elif(k=='.'):
        pyautogui.doubleClick()




def game_loop():
    x = (400)
    y = (300)
    lis = keyboard.Listener(on_press=on_press)
    lis.start()
    while True:
        while not gameExit:



            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes+
            x_m = "%1.8f" % unpack_from('!f', data, 24);
            y_m = "%1.8f" % unpack_from('!f', data, 32);
            z_m = "%1.8f" % unpack_from('!f', data, 28);
            y_m=-float(y_m)+float(x_m)


            print(x,y)
            if(float(z_m)<0.05 and float(z_m)>-0.05):
                z_m=0
            if(float(y_m)<0.05 and float(y_m)>-0.05):
                y_m=0
            x=(float(y_m))
            y = (float(z_m))
            if(float(y_m)<0 and float(y_m)!=0):
                x=20*(-(math.exp(-float(y_m)))*(abs(float(y_m))))
            elif(float(y_m)>0):
                x = 20*((math.exp(float(y_m)))*(abs(float(y_m))))
            if(float(z_m)<0 and float(z_m)!=0):
                y =20*(-math.exp(-float(z_m)))*((abs(float(z_m))))
            elif(float(z_m)>0):
                y = 20*((math.exp(float(z_m)))*(abs(float(z_m))))
            #pyautogui.moveTo(x,y)
            #sleep(0)
            pyautogui.moveRel(x,y)

game_loop()
  # start to listen on a separate thread

