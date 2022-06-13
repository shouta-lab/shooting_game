import tkinter
import tkinter.messagebox
import pygame
import sys
import random
import winsound

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

idx = 0
tmr = 0
p_x = 0
p_y = 0
full_s = 0

def main():
    idx, tmr, p_x, p_y, full__s
    pygame.init()
    pygame.init()
    pygame.display.set_caption("Shooting Game")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font_b = pygame.font.Font(None, 100)
    try:
        font_s_j = pygame.font.Font("font/Corporate-Logo-Rounded.ttf", 50)
    except:
        tkinter.messagebox.showerror("エラー", "フォントファイルがありません。")
        pygame.quit()
        sys.exit()
    tmr = 0
    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    if full_s == 0:
                        screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                        full_s = 1
                    else:
                        screen =pygame.display.set_mode((1280, 720))
                        full_s = 0
        key = pygame.key.get_pressed()

        if idx == 0: #title
            idx = 1
        elif idx == 1: #reset
            idx = 2
        elif idx == 2: #play
            
