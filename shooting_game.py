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
p_s_x = 30
p_s_y = 50
full_s = 0
TAMA_MAX = 200
tama_no = 0
tama_f = [False]*TAMA_MAX
tama_x = [0]*TAMA_MAX
tama_y = [0]*TAMA_MAX
player_img = pygame.image.load("png/player.png")

def set_tama():
    global tama_no
    tama_f[tama_no] = True
    tama_x[tama_no] = p_x
    tama_y[tama_no] = p_y
    tama_no = (tama_no+1)%TAMA_MAX

def move_tama():
    for i in range(TAMA_MAX):
        if tama_f[i] == True:
            tama_y[i] = tama_y[i] - 36
            screen.blit(player_img, [tama_x[i], tama_y[i]])
            if tama_y[i] < 0:
                    tama_f[i] = False

def main():
    global idx, tmr, p_x, p_y, full_s, p_s_x, p_s_y
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
        if idx == 0: # title
            idx = 1
        elif idx == 1: # reset
            p_x = 1280 / 2
            p_y = 720 / 2
            idx = 2
        elif idx == 2: # play
            screen.fill(WHITE)
            pygame.draw.rect(screen, RED, [p_x-p_s_x, p_y-p_s_y, p_s_x*2, p_s_y*2])
            if key[pygame.K_RIGHT] == 1: # 移動入力
                p_x = p_x + 10
            elif key[pygame.K_LEFT] == 1:
                p_x = p_x - 10
            if key[pygame.K_UP] == 1:
                p_y = p_y - 10
            elif key[pygame.K_DOWN] == 1:
                p_y = p_y + 10
            if key[pygame.K_SPACE] == 1:
                    tama_f[tama_no] = True
                    tama_x[tama_no] = p_x
                    tama_y[tama_no] = p_y
                    tama_no = (tama_no+1)%TAMA_MAX
            if p_x < 0:
                p_x = 0
            elif p_x > 1280:
                p_x = 1280
            if p_y < 0:
                p_y = 0
            elif p_y > 720:
                p_y = 720
            screen.blit(player_img, (p_x-p_s_x, p_y-p_s_y))
            for i in range(TAMA_MAX):
                if tama_f[i] == True:
                    tama_y[i] = tama_y[i] - 36
                    screen.blit(player_img, [tama_x[i], tama_y[i]])
                    if tama_y[i] < 0:
                            tama_f[i] = False
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
