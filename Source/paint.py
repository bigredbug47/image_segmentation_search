import pygame
import sys
import os
import Tkinter
import tkFileDialog
from main_process import main
from pygame.locals import *
import cv2

try:
    import android
except ImportError:
    android = None

file_flag = 0
dir_mainfolder = "a"
dir_result = "b"
dir_kmean = "c"
windowSurface = pygame.display.set_mode((480, 320))

kmean_flag = 0
click_color = 2
## Colors list
GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)

pygame.init()

## font setup
menu_font = pygame.font.SysFont("Arial", 18)
menu_text = menu_font.render("Paint", True, BLACK)

kmean_text = menu_font.render("KMEAN", True,BLACK)
otsu_text = menu_font.render("MEANSHIFT", True,BLACK)
fill_text = menu_font.render("FILL", True,BLACK)
test_text = menu_font.render("SByImage", True, BLACK)
open_text = menu_font.render("OPEN",True,BLACK)
search_text = menu_font.render("SEARCH", True, BLACK)

draw = False
brush_size = 10
brush_color = GREEN

menu_rect = pygame.Rect(0, 0, 100, 320)
screen_rect = pygame.Rect(100, 0, 380, 320)
green_rect = pygame.Rect(5, 55, 20, 20)
red_rect = pygame.Rect(27, 55, 20, 20)
blue_rect = pygame.Rect(49, 55, 20, 20)
pink_rect = pygame.Rect(71, 55, 20, 20)
light_blue_rect = pygame.Rect(5, 77, 20, 20)
yellow_rect = pygame.Rect(27, 77, 20, 20)
orange_rect = pygame.Rect(49, 77, 20, 20)
purple_rect = pygame.Rect(71, 77, 20, 20)
dark_green_rect = pygame.Rect(5, 99, 20, 20)
black_rect = pygame.Rect(27, 99, 20, 20)
white_rect = pygame.Rect(49, 99, 20, 20)
pretty_blue_rect = pygame.Rect(71, 99, 20, 20)

kmean_rect = pygame.Rect(5, 140, 90, 25)
otsu_rect = pygame.Rect(5, 170, 90, 25)
fill_rect = pygame.Rect(5, 200, 90, 25)
open_rect = pygame.Rect(5, 230, 90, 25)
test_rect = pygame.Rect(5, 260, 90, 25)
search_rect = pygame.Rect(5, 290, 90, 25)
save_flag = False
file_number = 1

green_flag = False
red_flag = False
blue_flag = False
pink_flag = False
yellow_flag = False
lightblue_flag = False
orange_flag = False
purple_flag = False
darkgreen_flag = False
white_flag = False
black_flag = False
prettyblue_flag = False

green_check = 0
red_check = 0
blue_check = 0
pink_check = 0
yellow_check = 0
lightblue_check = 0
orange_check = 0
purple_check = 0
darkgreen_check = 0
white_check = 0
black_check = 0
prettyblue_check = 0

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False
        
    # Drawing dot when mousebuttondown
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100:
        pygame.draw.circle(windowSurface, brush_color, mouse_pos, brush_size)
        if(green_flag == True and green_check == 0):
            green_check = 1
            click_color = click_color + 1
        elif(red_flag == True and red_check == 0):
            red_check = 1
            click_color = click_color + 1
        elif(blue_flag == True and blue_check == 0):
            blue_check = 1
            click_color = click_color + 1
        elif(pink_flag == True and pink_check == 0):
            pink_check = 1
            click_color = click_color + 1
        elif(yellow_flag == True and yellow_check == 0):
            yellow_check = 1
            click_color = click_color + 1
        elif(lightblue_flag == True and lightblue_check == 0):
            lightblue_check = 1
            click_color = click_color + 1
        elif(orange_flag == True and orange_check == 0):
            orange_check = 1
            click_color = click_color + 1
        elif(purple_flag == True and purple_check == 0):
            purple_check = 1
            click_color = click_color + 1
        elif(darkgreen_flag == True and darkgreen_check == 0):
            darkgreen_check = 1
            click_color = click_color + 1
        elif(white_flag == True and white_check == 0):
            white_check = 1
            click_color = click_color + 1
        elif(black_flag == True and black_check == 0):
            black_check = 1
            click_color = click_color + 1
        elif(prettyblue_flag == True and prettyblue_check == 0):
            prettyblue_check = 1
            click_color = click_color + 1
        save_flag = False

    # collision detection for COLOR
    if draw == True:    
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
            green_flag = True
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
            green_flag = False
            red_flag = True
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
            green_flag = False
            red_flag = False
            blue_flag = True
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = True
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = True
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = True
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = True
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = True
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = True
            white_flag = False
            black_flag = False
            prettyblue_flag = False
        if white_rect.collidepoint(mouse_pos):
            brush_color = WHITE
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = True
            black_flag = False
            prettyblue_flag = False
        if black_rect.collidepoint(mouse_pos):
            brush_color = BLACK
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = True
            prettyblue_flag = False
        if pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = PRETTY_BLUE
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = True

    ## collision detection for FILL
    if draw == True:
        if fill_rect.collidepoint(mouse_pos):
            pygame.draw.rect(windowSurface, brush_color, screen_rect)
            green_flag = False
            red_flag = False
            blue_flag = False
            pink_flag = False
            yellow_flag = False
            lightblue_flag = False
            orange_flag = False
            purple_flag = False
            darkgreen_flag = False
            white_flag = False
            black_flag = False
            prettyblue_flag = False
            green_check = 0
            red_check = 0
            blue_check = 0
            pink_check = 0
            yellow_check = 0
            lightblue_check = 0
            orange_check = 0
            purple_check = 0
            darkgreen_check = 0
            white_check = 0
            black_check = 0
            prettyblue_check = 0

            click_color = 1
            
    ## collision detection for test
    if draw == True:
        if test_rect.collidepoint(mouse_pos):
            root = Tkinter.Tk()
            root.withdraw()
            file_path = tkFileDialog.askopenfilename()
            print file_path
            file_flag = 1

    ## Collision detection for OPEN
    if draw == True:
        if open_rect.collidepoint(mouse_pos):
            root = Tkinter.Tk()
            root.withdraw()
            dir_mainfolder = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
            dir_kmean = dir_mainfolder + "/img_kmean"
            dir_result = dir_mainfolder + "/img_result"
            dir_rank = dir_mainfolder + "/img_rank"
            dir_otsu = dir_mainfolder + "/otsu"
            dir_thresh = dir_mainfolder + "/img_meanshift"
            dir_kmean_handwrite = dir_mainfolder + "/img_kmean_handwrite"
            dir_otsu_handwrite = dir_mainfolder + "/img_otsu_handwrite"
            if not os.path.exists(dir_kmean):
                os.makedirs(dir_kmean)
            if not os.path.exists(dir_result):
                os.makedirs(dir_result)
            if not os.path.exists(dir_rank):
                os.makedirs(dir_rank)
            if not os.path.exists(dir_otsu):
                os.makedirs(dir_otsu)
            if not os.path.exists(dir_thresh):
                os.makedirs(dir_thresh)
            if not os.path.exists(dir_kmean_handwrite):
                os.makedirs(dir_kmean_handwrite)
            if not os.path.exists(dir_otsu_handwrite):
                os.makedirs(dir_otsu_handwrite)
    ## Collision detection for SEARCH 
    if draw == True and save_flag == False:
        if search_rect.collidepoint(mouse_pos):
            search_surface = pygame.Surface((380, 320))
            search_surface.blit(windowSurface, (0, 0), (100, 0, 380, 320))
            try:
                with open("saved_files/PaintImage_" + str(file_number) + ".png"):
                    file_number = file_number + 1
                    save_flag = True
            except IOError:
                save_flag = True
            if (file_flag == 0): 
                pygame.image.save(search_surface, dir_result + "/0.jpg")
            else:
                file_img = cv2.imread(file_path)
                print file_img
                cv2.imwrite(dir_result + "/0.jpg",file_img)
            print click_color
            ##Call main function in k_mean_001.py
            main(dir_mainfolder, click_color, kmean_flag)
    
    ## Collision detection for KMEAN
    if draw == True:
        if kmean_rect.collidepoint(mouse_pos):
            kmean_flag = 1

    ## Collision detection for KMEAN
    if draw == True:
        if otsu_rect.collidepoint(mouse_pos):
            kmean_flag = 0

    # rect for button 
    pygame.draw.rect(windowSurface, GRAY, menu_rect)
    windowSurface.blit(menu_text, (10, 20))
    pygame.draw.rect(windowSurface, DARK_GRAY, kmean_rect)
    windowSurface.blit(kmean_text, (10, 140))
    pygame.draw.rect(windowSurface, DARK_GRAY, otsu_rect)
    windowSurface.blit(otsu_text, (10, 170))
    pygame.draw.rect(windowSurface, DARK_GRAY, fill_rect)
    windowSurface.blit(fill_text, (10, 200))
    pygame.draw.rect(windowSurface, DARK_GRAY, open_rect)
    windowSurface.blit(open_text, (10, 230))
    pygame.draw.rect(windowSurface, DARK_GRAY, test_rect)
    windowSurface.blit(test_text, (10, 260))   
    pygame.draw.rect(windowSurface, DARK_GRAY, search_rect)
    windowSurface.blit(search_text, (10, 290))

    # rect for brush_color
    pygame.draw.rect(windowSurface, GREEN, green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, green_rect, border)
    pygame.draw.rect(windowSurface, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, red_rect, border)
    pygame.draw.rect(windowSurface, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, blue_rect, border)
    pygame.draw.rect(windowSurface, PINK, pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, pink_rect, border)
    pygame.draw.rect(windowSurface, LIGHT_BLUE, light_blue_rect)
    if brush_color == LIGHT_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, light_blue_rect, border)
    pygame.draw.rect(windowSurface, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, yellow_rect, border)
    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)
    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)
    pygame.draw.rect(windowSurface, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, dark_green_rect, border)
    pygame.draw.rect(windowSurface, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, purple_rect, border)
    pygame.draw.rect(windowSurface, WHITE, white_rect)
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, white_rect, border)
    pygame.draw.rect(windowSurface, BLACK, black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BROWN, black_rect, border)
    pygame.draw.rect(windowSurface, PRETTY_BLUE, pretty_blue_rect)
    if brush_color == PRETTY_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, pretty_blue_rect, border)
 
    pygame.display.update()
