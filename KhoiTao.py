from ast import While
from glob import glob
from pickle import TRUE
import pygame, random, time, sys  
import threading       #Thư viện chạy đa luồng
from collections import deque  

import scipy as sp
pygame.init()     #Khởi tạo pygame



#tạo cửa sổ
gameSurface = pygame.display.set_mode((1250,650)) #kích thước cửa sổ
pygame.display.set_caption('MÊ CUNG')             #tên cửa sổ
ATDiChuyen = pygame.mixer.Sound('sfx_wing.wav')
ATAnDiem = pygame.mixer.Sound('sfx_point.wav')
ATChamTuong = pygame.mixer.Sound('sfx_hit.wav')
ATNhacNen = pygame.mixer.Sound('nen.wav')

k = 0.07    #thời gian sleep
tgstart = 0



# Các hàm chữ vẽ
def WordRUN():
    global run
    gfont = pygame.font.SysFont('consolas', 40)
    gsurf = gfont.render('BẮT ĐẦU', True, (0, 0, 0), (255, 255, 255))
    grect = gsurf.get_rect()
    grect.midtop = (590, 10)
    run = gameSurface.blit(gsurf, grect)
    pygame.display.flip()
def WordMAP(tt, x, y):
    gfont = pygame.font.SysFont('consolas', 18)
    gsurf = gfont.render("Map " + tt, True, (255, 255, 0))
    grect = gsurf.get_rect()
    grect.midtop = (x, y)
    gameSurface.blit(gsurf, grect)
    pygame.display.flip()
def WordMENU(k):
    global menu
    if k == 1:
        gfont = pygame.font.SysFont('consolas', 40)
    elif k == 2:
        gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render('CHỌN MAP', True, (0, 0, 0), (255, 255, 255))
    grect = gsurf.get_rect()
    if k == 1:
        grect.midtop = (590, 50)
    elif k == 2:
        grect.midtop = (50, 20)
    menu = gameSurface.blit(gsurf, grect)
    pygame.display.flip()
def WordTT(tt, x, y):
    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render(tt, True, (255, 255, 0))
    grect = gsurf.get_rect()
    grect.midtop = (x, y)
    gameSurface.blit(gsurf, grect)
    pygame.display.flip()
def WordLC(lc):
    global play, ss
    gfont = pygame.font.SysFont('consolas', 80)
    if lc == 1:
        gsurf = gfont.render("> CHƠI GAME", True, (255, 255, 0))
        grect = gsurf.get_rect()
        grect.midtop = (600, 120)
        play = gameSurface.blit(gsurf, grect)
        pygame.display.flip()
        return play
    if lc == 2:
        gsurf = gfont.render("> SO SÁNH THUẬT TOÁN", True, (255, 255, 0))
        grect = gsurf.get_rect()
        grect.midtop = (600, 350)
        ss = gameSurface.blit(gsurf, grect)
        pygame.display.flip()
        return ss
    return 0
def WordBA():
    global back
    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render('QUAY VỀ', True, (255,255,0), (255,0,0))
    grect = gsurf.get_rect()
    grect.midtop = (50, 20)
    back = gameSurface.blit(gsurf, grect)
    pygame.display.flip()


#hàm hỗ trợ 
def SoSanh(tt, x, y):
    tgfont = pygame.font.SysFont('consolas', 20)
    tgsurf = tgfont.render('Thời gian', True, (255, 255, 0))
    tgrect = tgsurf.get_rect()
    tgrect.midtop = (970, 380)
    gameSurface.blit(tgsurf, tgrect)

    sbfont = pygame.font.SysFont('consolas', 20)
    sbsurf = sbfont.render('Số bước', True, (255, 255, 0))
    sbrect = sbsurf.get_rect()
    sbrect.midtop = (1150, 380)
    gameSurface.blit(sbsurf, sbrect)

    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render(tt, True, (255, 255, 0))
    grect = gsurf.get_rect()
    grect.midtop = (x, y)
    gameSurface.blit(gsurf, grect)
    pygame.display.flip()

def ThoiGian(tt, x, y):
    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render(tt, True, (0,255,255))
    grect = gsurf.get_rect()
    grect.midtop = (x, y)
    gameSurface.blit(gsurf, grect)
    pygame.display.flip()

def SoBuoc(tt, x, y):
    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render(tt, True, (0, 0, 255))
    grect = gsurf.get_rect()
    grect.midtop = (x, y)
    gameSurface.blit(gsurf, grect)
    pygame.display.flip()