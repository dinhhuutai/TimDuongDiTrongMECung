from ast import While
from glob import glob
from pickle import TRUE
import pygame, random, time, sys  
import threading       #Thư viện chạy đa luồng
from collections import deque     

import scipy as sp
pygame.init()     #Khởi tạo pygame


#load hình ảnh
m = 20 #kích thước các hình khi chạy chính 
def LoadImg():
    global m, Imgwall, Imgstart, Imgend, Imgdauchan, Imgmui
    Imgwall = pygame.transform.scale(pygame.image.load('wall.jpg'),(m, m))         #hình gạch để xây tường
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))         #hình con cáo làm điểm nguồn 
    Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))           #hình chùm nho làm điểm đích
    Imgdauchan = pygame.transform.scale(pygame.image.load('dauchan.png'),(m, m))   #hình dấu chân những điểm đã duyệt
    Imgmui = pygame.transform.scale(pygame.image.load('mui.png'),(m, m))           #hình khói vào danh sách open chuẩn bị duyệt

#Map 
grid1 = [
"+++++++++++++++++++++++++",
"+e+             +     + +",
"+ +++++ +++++++ +++++ + +",
"+ + +   +       +     + +",
"+ + + +++++ + +++ ++ ++ +",
"+ +      ++ +      +    +",
"+ ++++++ +  + + +++++ +++",
"+s       ++++++ +   + + +",
"++++++++++      + +   + +",
"+ +     +++++ + + + + + +",
"+ + +++       + + + + + +",
"+   + ++ ++++++ + + + + +",
"+ +   +       + + + + + +",
"+ ++ ++++++++++ + + + + +",
"+ +  +          + + +   +",
"+ + ++ ++++++++++++ +++ +",
"+ +  + + +          +   +",
"++++ + + ++++++ + +++ +++",
"+    + +        +  +    +",
"+++++++++++++++++++++++++",
]


grid2 = [
"+++++++++++++++++++++++++",
"+              +        +",
"+    +  +   +  +    +++++",
"+ ++++ ++++++ +++ +     +",
"+ +  +      +     +  ++ +",
"+    +   ++++++   +  +  +",
"+  +++++    +   ++++++  +",
"+  +e+ +  + +++++    +  +",
"+ ++ + ++ + +   +++ +++++",
"+  + +    +   +++ +     +",
"+  + ++   +++     +  ++ +",
"+     +   +    +     +  +",
"+ ++    ++++++++ +++ ++++",
"+  + +         +  +  +  +",
"++ ++++++   +     +  ++ +",
"+  +  + + +++  ++ ++    +",
"+ ++  + + + + ++  +  +  +",
"+    ++     +  ++++++++ +",
"+s +  +  +  +     +     +",
"+++++++++++++++++++++++++",
]

grid3 = [
"+++++++++++++++++++++++++",
"+  +           +        +",
"+  +   ++++  + + +   ++ +",
"+  +++++     + + +++++  +",
"+  +   + +++++   + + +  +",
"+    + + +   +++++ +    +",
"+ +  +   +         ++++ +",
"+ +++++ ++ +  ++++ +    +",
"+  +       +  + e+   +  +",
"+  +  + +++++ +  +++++  +",
"+ +++++ +  +  +  + + ++ +",
"+  +  + + ++ ++    + +  +",
"+     + +          +    +",
"+ +++ ++++ +++++++ +  + +",
"+   + +     +    +   ++ +",
"+ + +    +  +  + + +  + +",
"+++ ++++ +  +  + + +  + +",
"+   +    + +++ + + + ++++",
"+s+      +     +   +    +",
"+++++++++++++++++++++++++",
]

grid4 = [
"+++++++++++++++++++++++++",
"+ +    +       +  +     +",
"+   +  ++ ++++++    + + +",
"+++++   + +    + ++++ + +",
"+   +++ + + +  e    +++ +",
"+ +     + + + ++++  +   +",
"+ ++ ++++   + +  ++ +++ +",
"+ +  +    +++ +  +      +",
"+ +++++++ + + + ++ ++++ +",
"+    +      + +    +  + +",
"++++   + ++++ ++++ +    +",
"+    + +    +    + ++ +++",
"+++  +   +    +  +      +",
"+   ++++ ++++ ++++ + ++ +",
"+ +    + + +  +    +  + +",
"+ ++++ + + + ++++ +++ + +",
"+ +  +++ +         +  + +",
"+ ++     ++++++s++++ ++ +",
"+    +   +         +    +",
"+++++++++++++++++++++++++",
]

grid5 = [
"+++++++++++++++++++++++++",
"+ +      +   + +   +    +",
"+   + +      +   +   +  +",
"+  ++++ ++++++ ++++++++ +",
"+  +  +     +     + + + +",
"+  + +++++    +  ++     +",
"+  +   +   +++++  +++++ +",
"+ ++++ +++ +          + +",
"+      +   ++++ +++   + +",
"+  +++++ +++  +  +  + + +",
"+  +       + +++ + ++++++",
"++ + +++++       +   +  +",
"+  +   + + ++ + ++++ +  +",
"+  +++++    + +    + ++ +",
"+ ++   ++++ + ++++    + +",
"+    +      +  e+   +   +",
"+ +++++++++++++++ + +++++",
"+ +  + +  +     + + +   +",
"+s     +     +    +     +",
"+++++++++++++++++++++++++",
]

grid6 = [
"+++++++++++++++++++++++++",
"+            +++  +   + +",
"+++++++++ ++ + ++   +   +",
"+       + +  + +  +++++++",
"+ +++ ++++++ + +        +",
"+ + +        +   + ++++++",
"+ + + ++++  s    +      +",
"+ +        + + +++++ + ++",
"+ + +++ ++ + +       +  +",
"+ +  +   + + +++++++ ++ +",
"+ + ++ + + + +       +  +",
"+ + ++ + + + + +++++++ ++",
"+    + + +++++          +",
"++++ + + +   + + ++ +++++",
"+    + +   + e +  +     +",
"+ ++ +++++ ++++++ +++++ +",
"+ +               + +   +",
"+ ++++++ ++++++++ + + + +",
"+ +       +       +   + +",
"+++++++++++++++++++++++++",
]

grid7 = [
"+++++++++++++++++++++++++",
"+ +     +        +      +",
"+ + +++ + ++++++ + ++++ +",
"+ +  +  + +      + + +  +",
"+ +     + +  +++++ + +  +",
"+ +++ ++++++ +   +   ++++",
"+ +        + + + +++ +  +",
"+ + ++++++ + +++  +     +",
"+ +  s+  + +   +  + +++ +",
"+     +  +e+ ++++ +   + +",
"+ +++ ++ +    + + +++++ +",
"+ + +    ++++ +      +  +",
"+ + + +       +++++  +  +",
"+ + + +++ +++++   +  +  +",
"+   + + +   +     + +++ +",
"+ +++ +     +++++ +     +",
"+  +  + + +++        +  +",
"++ ++ +++     + ++++++ ++",
"+   +   +  +  +      +  +",
"+++++++++++++++++++++++++",
]

grid8 = [
"+++++++++++++++++++++++++",
"+s     +        +       +",
"+ ++++ ++ +++++ + ++++  +",
"+  + +    +   + + + +   +",
"+ ++ + ++++   +   +   + +",
"+  +   +    +++ +++++++ +",
"+++++  + ++++ + +     + +",
"+      +      + +  ++++ +",
"+ + ++++ ++++ ++++  +   +",
"+ +    + +  +       + + +",
"+ +  + + + ++++++e+++++ +",
"++++++ + +  + + + + +   +",
"+    + ++++ + + + +   + +",
"+ +           +       + +",
"+ +++++ ++ ++++ +++ +++++",
"+ +   +  +       +  +   +",
"+ ++  +  +  + ++ + ++++ +",
"+  + ++ +++++  + + +  + +",
"+  +        +  + +      +",
"+++++++++++++++++++++++++",
]

grid9 = [
"+++++++++++++++++++++++++",
"+         +       +     +",
"+ + +++++ + +++++ + +++++",
"+ + +     + +       +   +",
"+ + + +++ + + +++++ + + +",
"+ + + + +   + +     + + +",
"+   + + +++++ + +++++ + +",
"+++++ +       + +     + +",
"+   + ++++ +    + +++ + +",
"+ + +  +   ++++++   + + +",
"+ + ++ + +++    +++++ + +",
"+ + +  +    e++ +       +",
"+ ++++ +++++ +    +++++ +",
"+ +     +    ++++ +     +",
"+ +++++ ++++++ +  + +++++",
"+ +          + ++++  +  +",
"+ + + ++++ + +       +  +",
"+ +++ +  + +++++ +++ +  +",
"+s       +  +           +",
"+++++++++++++++++++++++++",
]

grid10 = [
"+++++++++++++++++++++++++",
"+ e ++++       + +      +",
"+ +      +++++ + + +  + +",
"+ ++++++++   + + + ++++ +",
"+ +        +++ +   +    +",
"+ ++++++++   +   ++++++ +",
"+       ++++ ++ ++      +",
"+ +++++ +       ++ ++++ +",
"+         +++++  + +    +",
"++++++++++++++++ ++++++++",
"+         + +  +        +",
"+++++++ + + ++ + ++++ +++",
"+ +     + +    +    + +s+",
"+ + + +++ + + +++ + + + +",
"+ + + + +   +  +  + + + +",
"+ + + + + + ++ + ++ + + +",
"+ + +     + +     + + + +",
"+ +++++++ +++ +++++++ + +",
"+         +    +        +",
"+++++++++++++++++++++++++",
]



#tạo cửa sổ
gameSurface = pygame.display.set_mode((1250,650)) #kích thước cửa sổ
pygame.display.set_caption('MÊ CUNG')             #tên cửa sổ
ATDiChuyen = pygame.mixer.Sound('sfx_wing.wav')
ATAnDiem = pygame.mixer.Sound('sfx_point.wav')
ATChamTuong = pygame.mixer.Sound('sfx_hit.wav')
ATNhacNen = pygame.mixer.Sound('nen.wav')

k = 0.07    #thời gian sleep

#====================== CT1 =====================
def setup_maze(grid, v, t):                          # Hàm tạo mê cung
    global start_x, start_y, end_x, end_y      # Các biến toàn cục : start_x, start_y là vị trí x, y của điểm bắt đầu : end_x, end_y là vị trí x, y của điểm kết thúc
    for y in range(len(grid)):                 # đọc từng dòng 
        for x in range(len(grid[y])):          # đọc từng ô trong dòng
            character = grid[y][x]             # gán kí tự trên grid vị trí x, y cho biến character
            screen_x = v + (x * (m+2))         # Mỗi ô vuông có kích thước là 21, khoảng cách các ô = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #Dấu cộng là hình bức tường
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #Vẽ hình ảnh bức tường lên cửa sổ
                walls.append((screen_x, screen_y))                                #Thêm vị trí các bức tường vào biến walls

            if character == " " or character == "e":  #ô trống hoặc e là vị trí trống đánh dấu đi được
                path.append((screen_x, screen_y))     # thêm các vị trí đi được vào biến path

            if character == "e":                      # e là điểm đích 
                end_x, end_y = screen_x, screen_y     # gán vị trí đích cho biến toàn cục
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #Vẽ điểm đích lên cửa sổ

            if character == "s":                       #s là điểm nguồn
                start_x, start_y = screen_x, screen_y     # gán vị trí nguồn cho biến toàn cục
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #vẽ điểm nguồn lên cửa sổ



def search(x,y):      #Hàm chạy tìm đường đi trong mê cung - BFS   
    global k
    # x: điểm nguồn    y: điểm đích
    frontier.append((x, y))                              #thêm vào danh sách duyệt
    solution[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(frontier) > 0:                             # exit while loop when frontier queue equals zero
        true = True

        for event in pygame.event.get():                 #Lấy các sự kiện
            if event.type == pygame.QUIT:                #Nếu nhấn nút x trên cửa sổ
                pygame.quit()                            #lệnh tắt cửa sổ
                sys.exit()
            if event.type == pygame.KEYDOWN:             #Sự kiện nhấn bàn phím
                if event.key == pygame.K_UP:             # Nhấn nút up trên bàn phím 
                    if k >= 0.03:                        # k là biến sleep toàn cục
                        k = k - 0.03                     # giảm k để chương trình chạy nhanh hơn
                if event.key == pygame.K_DOWN:           #Nhấn nút down trên bàn phím
                    k = k + 0.03                         # tăng k để chương trình chạy chậm lại
                if event.key == pygame.K_SPACE:          #Khi nhấn space dừng màn hình
                    while true:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    true = False

        time.sleep(k)
        x, y = frontier.popleft()        # lấy phần tử đầu trong danh sách duyệt

        if x == end_x and y == end_y:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRoute(end_x, end_y)
            tg = time.time() - tgstart
            ThoiGian(str(round(tg, 4)), 970, 420)
            break

        if(x - (m+2), y) in path and (x - (m+2), y) not in visited:      # Kiểm tra bên trái có đường đi không
            cell = (x - (m+2), y)
            solution[cell] = x, y                                        #Thêm vị trí vào danh sách đường đi
            gameSurface.blit(Imgmui, pygame.Rect(x - (m+2), y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
            pygame.display.flip()                                        #Cập nhật toàn bộ nội dung cửa sổ

            frontier.append(cell)                 # Thêm vào danh sách duyệt
            visited.add((x - (m+2), y))           # thêm vào danh sách đã đi và đang trong danh sách duyệt

        if (x, y - (m+2)) in path and (x, y - (m+2)) not in visited:  # Kiểm tra phía trên có đường đi không
            cell = (x, y - (m+2))
            solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x, y - (m+2), m, m))
            pygame.display.flip()

            frontier.append(cell)
            visited.add((x, y - (m+2)))

        if(x + (m+2), y) in path and (x + (m+2), y) not in visited:   # Kiểm tra đường đi phía dưới
            cell = (x + (m+2), y)
            solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x + (m+2), y, m, m))
            pygame.display.flip()
            
            frontier.append(cell)
            visited.add((x + (m+2), y))

        if(x, y + (m+2)) in path and (x, y + (m+2)) not in visited:  # Kiểm tra có đường di bên phải?
            cell = (x, y + (m+2))
            solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x, y + (m+2), m, m))
            pygame.display.flip()

            frontier.append(cell)
            visited.add((x, y + (m+2)))
        
        if (x != start_x or y != start_y) and (x != end_x or y != end_y):
            gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
            gameSurface.blit(Imgdauchan, pygame.Rect(x, y, m, m))  #Tải hình ảnh vị trí đang duyệt lên cửa sổ 
            pygame.display.flip()


def backRoute(x, y):    #Hàm duyệt lại đường đi khi tìm được điểm đích - x: end_x,  y: end_y
    gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
    gameSurface.blit(Imgend, pygame.Rect(end_x, end_y, m, m))
    pygame.display.flip()
    i = 0
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        time.sleep(0.03)
        x, y = solution[x, y]               # "key value" now becomes the new key
        i += 1
        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
        gameSurface.blit(Imgstart, pygame.Rect(x, y, m, m))
        pygame.display.flip()
    SoBuoc(str(i), 1150, 420)


#=====================================  CT2   ================================
def setup_maze1(grid, v, t):                          # Hàm tạo mê cung
    global start_x1, start_y1, end_x1, end_y1         # Các biến toàn cục : start_x, start_y là vị trí x, y của điểm bắt đầu : end_x, end_y là vị trí x, y của điểm kết thúc
    for y in range(len(grid)):                        # đọc từng dòng 
        for x in range(len(grid[y])):                 # đọc từng ô trong dòng
            character = grid[y][x]                    # gán kí tự trên grid vị trí x, y cho biến character
            screen_x = v + (x * (m+2))                # Mỗi ô vuông có kích thước là 21, khoảng cách các ô = 3
            screen_y = t + (y * (m+2))                # move to the y location of the screen starting at 288

            if character == "+":
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))
                walls1.append((screen_x, screen_y))

            if character == " " or character == "e":
                path1.append((screen_x, screen_y))

            if character == "e":
                end_x1, end_y1 = screen_x, screen_y
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))

            if character == "s":
                start_x1, start_y1 = screen_x, screen_y
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))



def search1(x,y):               #Hàm chạy tìm đường đi trong mê cung - DFS
    global k

    frontier1.append((x, y))
    solution1[x,y] = x,y

    while len(frontier1) > 0:          # exit while loop when frontier queue equals zero
        true = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if k >= 0.03:
                        k = k - 0.03
                if event.key == pygame.K_DOWN:
                    k = k + 0.03
                if event.key == pygame.K_SPACE:
                    while true:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    true = False

        time.sleep(k)
        x, y = frontier1.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if x == end_x1 and y == end_y1:
            backRoute1(end_x1, end_y1)
            tg = time.time() - tgstart
            ThoiGian(str(round(tg, 4)), 970, 465)
            break

        if(x - (m+2), y) in path1 and (x - (m+2), y) not in visited1:  # check the cell on the left
            cell = (x - (m+2), y)
            solution1[cell] = x, y  
            gameSurface.blit(Imgmui, pygame.Rect(x - (m+2), y, m, m))
            pygame.display.flip()

            frontier1.appendleft(cell)   # add cell to frontier list
            visited1.add((x - (m+2), y))  # add cell to visited list

        if (x, y - (m+2)) in path1 and (x, y - (m+2)) not in visited1:  # check the cell up
            cell = (x, y - (m+2))
            solution1[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x, y - (m+2), m, m))
            pygame.display.flip()

            frontier1.appendleft(cell)
            visited1.add((x, y - (m+2)))

        if(x + (m+2), y) in path1 and (x + (m+2), y) not in visited1:   # check the cell on the  right
            cell = (x + (m+2), y)
            solution1[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x + (m+2), y, m, m))
            pygame.display.flip()
            
            frontier1.appendleft(cell)
            visited1.add((x + (m+2), y))

        if(x, y + (m+2)) in path1 and (x, y + (m+2)) not in visited1:  # check the cell down
            cell = (x, y + (m+2))
            solution1[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(x, y + (m+2), m, m))
            pygame.display.flip()

            frontier1.appendleft(cell)
            visited1.add((x, y + (m+2)))
        
        if (x != start_x1 or y != start_y1) and (x != end_x1 or y != end_y1):
            gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
            gameSurface.blit(Imgdauchan, pygame.Rect(x, y, m, m))
            pygame.display.flip()


def backRoute1(x, y):
    gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
    gameSurface.blit(Imgend, pygame.Rect(end_x1, end_y1, m, m))
    pygame.display.flip()
    i = 0
    while (x, y) != (start_x1, start_y1):    # stop loop when current cells == start cell
        time.sleep(0.03)
        x, y = solution1[x, y]               # "key value" now becomes the new key
        i += 1
        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
        gameSurface.blit(Imgstart, pygame.Rect(x, y, m, m))
        pygame.display.flip()
    SoBuoc(str(i), 1150, 465)


#=====================   CT3    =======================
class NodeUCS:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f


def setup_maze2(grid, v, t):                          # Hàm tạo mê cung
    global start_x2, start_y2, end_x2, end_y2      # Các biến toàn cục : start_x, start_y là vị trí x, y của điểm bắt đầu : end_x, end_y là vị trí x, y của điểm kết thúc
    for y in range(len(grid)):                 # đọc từng dòng 
        for x in range(len(grid[y])):          # đọc từng ô trong dòng
            character = grid[y][x]             # gán kí tự trên grid vị trí x, y cho biến character
            screen_x = v + (x * (m+2))         # Mỗi ô vuông có kích thước là 21, khoảng cách các ô = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #Dấu cộng là hình bức tường
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #Vẽ hình ảnh bức tường lên cửa sổ
                walls2.append((screen_x, screen_y))                                #Thêm vị trí các bức tường vào biến walls

            if character == " " or character == "e":  #ô trống hoặc e là vị trí trống đánh dấu đi được
                path2.append((screen_x, screen_y))     # thêm các vị trí đi được vào biến path

            if character == "e":                      # e là điểm đích 
                end_x2, end_y2 = screen_x, screen_y     # gán vị trí đích cho biến toàn cục
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #Vẽ điểm đích lên cửa sổ

            if character == "s":                       #s là điểm nguồn
                start_x2, start_y2 = screen_x, screen_y     # gán vị trí nguồn cho biến toàn cục
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #vẽ điểm nguồn lên cửa sổ

def Hx2(x, y, end_x2, end_y2):
    return abs(end_x2 - x)/(m + 2) + abs(end_y2 - y)/(m + 2)

def LayPhanTuTotNhat2():
    min = open2[0]
    for i in open2:
        if i.f < min.f:
            min = i
    open2.remove(min)
    return min

def KtCoTrongOpen2(NodeUCSCon):
    for i in open2:
        if NodeUCSCon.x == i.x and NodeUCSCon.y == i.y:
            return True
    return False

def Kt1_2(NodeUCSCon):
    kt = 0
    for i in open2:
        if NodeUCSCon.x == i.x and NodeUCSCon.y == i.y:
            if NodeUCSCon.f < i.f:
                return kt
        kt+=1
    return False

def KtCoTrongClose2(NodeUCSCon):
    for i in close2:
        if NodeUCSCon.x == i.x and NodeUCSCon.y == i.y:
            return True
    return False

def Kt2_2(NodeUCSCon):
    kt = 0
    for i in close2:
        if NodeUCSCon.x == i.x and NodeUCSCon.y == i.y:
            if NodeUCSCon.f < i.f:
                return kt
        kt+=1
    return False


def search2(x,y):      #Hàm chạy tìm đường đi trong mê cung - BFS   
    global k
    # x: điểm nguồn    y: điểm đích
    g = 0
    h = 0
    f = g + h
    open2.append(NodeUCS(x, y, g, h, f))                              #thêm vào danh sách duyệt
    solution2[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(open2) > 0:                             # exit while loop when open queue equals zero
        true = True

        for event in pygame.event.get():                 #Lấy các sự kiện
            if event.type == pygame.QUIT:                #Nếu nhấn nút x trên cửa sổ
                pygame.quit()                            #lệnh tắt cửa sổ
                sys.exit()
            if event.type == pygame.KEYDOWN:             #Sự kiện nhấn bàn phím
                if event.key == pygame.K_UP:             # Nhấn nút up trên bàn phím 
                    if k >= 0.03:                        # k là biến sleep toàn cục
                        k = k - 0.03                     # giảm k để chương trình chạy nhanh hơn
                if event.key == pygame.K_DOWN:           #Nhấn nút down trên bàn phím
                    k = k + 0.03                         # tăng k để chương trình chạy chậm lại
                if event.key == pygame.K_SPACE:          #Khi nhấn space dừng màn hình
                    while true:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    true = False

        time.sleep(k)
        # for i in open2:
        #     print(i.f, end='  ')
        # print(end='  -----  ')
        nodeUCSCha = LayPhanTuTotNhat2()        # lấy phần tử đầu trong danh sách duyệt
        close2.append(nodeUCSCha)
        # print(nodeUCSCha.f)

        if nodeUCSCha.x == end_x2 and nodeUCSCha.y == end_y2:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRoute2(end_x2, end_y2)
            tg = time.time() - tgstart
            ThoiGian(str(round(tg, 4)), 970, 510)
            break

        if(nodeUCSCha.x - (m+2), nodeUCSCha.y) in path2 and (nodeUCSCha.x - (m+2), nodeUCSCha.y) not in visited2:      # Kiểm tra bên trái có đường đi không
            xcon = nodeUCSCha.x - (m+2)
            ycon = nodeUCSCha.y
            gcon = nodeUCSCha.g + 1
            hcon = 0
            fcon = gcon + hcon
            nodeUCSCon = NodeUCS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen2(nodeUCSCon):
                if Kt1_2(nodeUCSCon) != False:
                    open2[Kt1_2(nodeUCSCon)] = nodeUCSCon
                    cell = (nodeUCSCha.x - (m+2), nodeUCSCha.y)
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if KtCoTrongClose2(nodeUCSCon):
                if Kt2_2(nodeUCSCon) != False:
                    open2.append(nodeUCSCon)
                    close2.remove(nodeUCSCon)
                    cell = (nodeUCSCha.x - (m+2), nodeUCSCha.y)
                    solution[cell] = nodeUCSCha.x, nodeUCSCha.y
            if not(KtCoTrongOpen2(nodeUCSCon) and KtCoTrongClose2(nodeUCSCon)):
                open2.append(nodeUCSCon)
                cell = (nodeUCSCha.x - (m+2), nodeUCSCha.y)
                solution2[cell] = nodeUCSCha.x, nodeUCSCha.y


            # cell = (x - (m+2), y)
            # solution[cell] = x, y                                        #Thêm vị trí vào danh sách đường đi
            gameSurface.blit(Imgmui, pygame.Rect(nodeUCSCha.x - (m+2), nodeUCSCha.y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
            pygame.display.flip()                                        #Cập nhật toàn bộ nội dung cửa sổ

            # open.append(cell)                 # Thêm vào danh sách duyệt
            visited2.add((nodeUCSCha.x - (m+2), nodeUCSCha.y))           # thêm vào danh sách đã đi và đang trong danh sách duyệt

        if (nodeUCSCha.x, nodeUCSCha.y - (m+2)) in path2 and (nodeUCSCha.x, nodeUCSCha.y - (m+2)) not in visited2:  # Kiểm tra phía trên có đường đi không
            xcon = nodeUCSCha.x
            ycon = nodeUCSCha.y - (m+2)
            gcon = nodeUCSCha.g + 1
            hcon = 0
            fcon = gcon + hcon
            nodeUCSCon = NodeUCS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen2(nodeUCSCon):
                if Kt1_2(nodeUCSCon) != False:
                    open2[Kt1_2(nodeUCSCon)] = nodeUCSCon
                    cell = (nodeUCSCha.x, nodeUCSCha.y - (m+2))
                    solution[cell] = nodeUCSCha.x, nodeUCSCha.y
            if KtCoTrongClose2(nodeUCSCon):
                if Kt2_2(nodeUCSCon) != False:
                    open2.append(nodeUCSCon)
                    close2.remove(nodeUCSCon)
                    cell = (nodeUCSCha.x, nodeUCSCha.y - (m+2))
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if not(KtCoTrongOpen2(nodeUCSCon) and KtCoTrongClose2(nodeUCSCon)):
                open2.append(nodeUCSCon)
                cell = (nodeUCSCha.x, nodeUCSCha.y - (m+2))
                solution2[cell] = nodeUCSCha.x, nodeUCSCha.y


            # cell = (x, y - (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeUCSCha.x, nodeUCSCha.y - (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited2.add((nodeUCSCha.x, nodeUCSCha.y - (m+2)))

        if(nodeUCSCha.x + (m+2), nodeUCSCha.y) in path2 and (nodeUCSCha.x + (m+2), nodeUCSCha.y) not in visited2:   # Kiểm tra đường đi phía dưới

            xcon = nodeUCSCha.x + (m+2)
            ycon = nodeUCSCha.y
            gcon = nodeUCSCha.g + 1
            hcon = 0
            fcon = gcon + hcon
            nodeUCSCon = NodeUCS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen2(nodeUCSCon):
                if Kt1_2(nodeUCSCon) != False:
                    open2[Kt1_2(nodeUCSCon)] = nodeUCSCon
                    cell = (nodeUCSCha.x + (m+2), nodeUCSCha.y)
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if KtCoTrongClose2(nodeUCSCon):
                if Kt2_2(nodeUCSCon) != False:
                    open2.append(nodeUCSCon)
                    close2.remove(nodeUCSCon)
                    cell = (nodeUCSCha.x + (m+2), nodeUCSCha.y)
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if not(KtCoTrongOpen2(nodeUCSCon) and KtCoTrongClose2(nodeUCSCon)):
                open2.append(nodeUCSCon)
                cell = (nodeUCSCha.x + (m+2), nodeUCSCha.y)
                solution2[cell] = nodeUCSCha.x, nodeUCSCha.y


            # cell = (x + (m+2), y)
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeUCSCha.x + (m+2), nodeUCSCha.y, m, m))
            pygame.display.flip()
            
            # open.append(cell)
            visited2.add((nodeUCSCha.x + (m+2), nodeUCSCha.y))

        if(nodeUCSCha.x, nodeUCSCha.y + (m+2)) in path2 and (nodeUCSCha.x, nodeUCSCha.y + (m+2)) not in visited2:  # Kiểm tra có đường di bên phải?

            xcon = nodeUCSCha.x
            ycon = nodeUCSCha.y + (m+2)
            gcon = nodeUCSCha.g + 1
            hcon = 0
            fcon = gcon + hcon
            nodeUCSCon = NodeUCS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen2(nodeUCSCon):
                if Kt1_2(nodeUCSCon) != False:
                    open2[Kt1_2(nodeUCSCon)] = nodeUCSCon
                    cell = (nodeUCSCha.x, nodeUCSCha.y + (m+2))
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if KtCoTrongClose2(nodeUCSCon):
                if Kt2_2(nodeUCSCon) != False:
                    open2.append(nodeUCSCon)
                    close2.remove(nodeUCSCon)
                    cell = (nodeUCSCha.x, nodeUCSCha.y + (m+2))
                    solution2[cell] = nodeUCSCha.x, nodeUCSCha.y
            if not(KtCoTrongOpen2(nodeUCSCon) and KtCoTrongClose2(nodeUCSCon)):
                open2.append(nodeUCSCon)
                cell = (nodeUCSCha.x, nodeUCSCha.y + (m+2))
                solution2[cell] = nodeUCSCha.x, nodeUCSCha.y


            # cell = (x, y + (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeUCSCha.x, nodeUCSCha.y + (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited2.add((nodeUCSCha.x, nodeUCSCha.y + (m+2)))
        
        if (nodeUCSCha.x != start_x2 or nodeUCSCha.y != start_y2) and (nodeUCSCha.x != end_x2 or nodeUCSCha.y != end_y2):
            gameSurface.fill((0, 0, 0), pygame.Rect(nodeUCSCha.x, nodeUCSCha.y, m, m))
            gameSurface.blit(Imgdauchan, pygame.Rect(nodeUCSCha.x, nodeUCSCha.y, m, m))  #Tải hình ảnh vị trí đang duyệt lên cửa sổ 
            pygame.display.flip()


def backRoute2(x, y):    #Hàm duyệt lại đường đi khi tìm được điểm đích - x: end_x,  y: end_y
    gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
    gameSurface.blit(Imgend, pygame.Rect(end_x2, end_y2, m, m))
    pygame.display.flip()
    i = 0
    while (x, y) != (start_x2, start_y2):    # stop loop when current cells == start cell
        time.sleep(0.03)
        x, y = solution2[x, y]               # "key value" now becomes the new key
        i += 1
        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
        gameSurface.blit(Imgstart, pygame.Rect(x, y, m, m))
        pygame.display.flip()
    SoBuoc(str(i), 1150, 510)

#==========================  CT4   =============================
class NodeGR:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f

def setup_maze3(grid, v, t):                          # Hàm tạo mê cung
    global start_x3, start_y3, end_x3, end_y3      # Các biến toàn cục : start_x, start_y là vị trí x, y của điểm bắt đầu : end_x, end_y là vị trí x, y của điểm kết thúc
    for y in range(len(grid)):                 # đọc từng dòng 
        for x in range(len(grid[y])):          # đọc từng ô trong dòng
            character = grid[y][x]             # gán kí tự trên grid vị trí x, y cho biến character
            screen_x = v + (x * (m+2))         # Mỗi ô vuông có kích thước là 21, khoảng cách các ô = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #Dấu cộng là hình bức tường
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #Vẽ hình ảnh bức tường lên cửa sổ
                walls3.append((screen_x, screen_y))                                #Thêm vị trí các bức tường vào biến walls

            if character == " " or character == "e":  #ô trống hoặc e là vị trí trống đánh dấu đi được
                path3.append((screen_x, screen_y))     # thêm các vị trí đi được vào biến path

            if character == "e":                      # e là điểm đích 
                end_x3, end_y3 = screen_x, screen_y     # gán vị trí đích cho biến toàn cục
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #Vẽ điểm đích lên cửa sổ

            if character == "s":                       #s là điểm nguồn
                start_x3, start_y3 = screen_x, screen_y     # gán vị trí nguồn cho biến toàn cục
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #vẽ điểm nguồn lên cửa sổ


def Hx3(x, y, end_x3, end_y3):
    return abs(end_x3 - x)/(m + 2) + abs(end_y3 - y)/(m + 2)

def LayPhanTuTotNhat3():
    min = open3[0]
    for i in open3:
        if i.f < min.f:
            min = i
    open3.remove(min)
    return min

def KtCoTrongOpen3(NodeGRCon):
    for i in open3:
        if NodeGRCon.x == i.x and NodeGRCon.y == i.y:
            return True
    return False

def Kt1_3(NodeGRCon):
    k = 0
    for i in open3:
        if NodeGRCon.x == i.x and NodeGRCon.y == i.y:
            if NodeGRCon.f < i.f:
                return k
        k+=1
    return False

def KtCoTrongClose3(NodeGRCon):
    for i in close3:
        if NodeGRCon.x == i.x and NodeGRCon.y == i.y:
            return True
    return False

def Kt2_3(NodeGRCon):
    k = 0
    for i in close3:
        if NodeGRCon.x == i.x and NodeGRCon.y == i.y:
            if NodeGRCon.f < i.f:
                return k
        k+=1
    return False


def search3(x,y):      #Hàm chạy tìm đường đi trong mê cung - BFS   
    global k
    # x: điểm nguồn    y: điểm đích
    g = 0
    h = Hx3(x, y, end_x3, end_y3)
    f = g + h
    open3.append(NodeGR(x, y, g, h, f))                              #thêm vào danh sách duyệt
    solution3[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(open3) > 0:                             # exit while loop when open queue equals zero
        true = True

        for event in pygame.event.get():                 #Lấy các sự kiện
            if event.type == pygame.QUIT:                #Nếu nhấn nút x trên cửa sổ
                pygame.quit()                            #lệnh tắt cửa sổ
                sys.exit()
            if event.type == pygame.KEYDOWN:             #Sự kiện nhấn bàn phím
                if event.key == pygame.K_UP:             # Nhấn nút up trên bàn phím 
                    if k >= 0.03:                        # k là biến sleep toàn cục
                        k = k - 0.03                     # giảm k để chương trình chạy nhanh hơn
                if event.key == pygame.K_DOWN:           #Nhấn nút down trên bàn phím
                    k = k + 0.03                         # tăng k để chương trình chạy chậm lại
                if event.key == pygame.K_SPACE:          #Khi nhấn space dừng màn hình
                    while true:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    true = False

        time.sleep(k)
        # for i in open:
        #     print(i.f, end='  ')
        # print(end='  -----  ')
        nodeGRCha = LayPhanTuTotNhat3()        # lấy phần tử đầu trong danh sách duyệt
        close3.append(nodeGRCha)
        # print(nodeGRCha.f)

        if nodeGRCha.x == end_x3 and nodeGRCha.y == end_y3:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRoute3(end_x3, end_y3)
            tg = time.time() - tgstart
            ThoiGian(str(round(tg, 4)), 970, 555)
            break

        if(nodeGRCha.x - (m+2), nodeGRCha.y) in path3 and (nodeGRCha.x - (m+2), nodeGRCha.y) not in visited3:      # Kiểm tra bên trái có đường đi không
            xcon = nodeGRCha.x - (m+2)
            ycon = nodeGRCha.y
            gcon = nodeGRCha.g
            hcon = Hx3(xcon, ycon, end_x3, end_y3)
            fcon = gcon + hcon
            nodeGRCon = NodeGR(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen3(nodeGRCon):
                if Kt1_3(nodeGRCon) != False:
                    open3[Kt1_3(nodeGRCon)] = nodeGRCon
                    cell = (nodeGRCha.x - (m+2), nodeGRCha.y)
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if KtCoTrongClose3(nodeGRCon):
                if Kt2_3(nodeGRCon) != False:
                    open3.append(nodeGRCon)
                    close3.remove(nodeGRCon)
                    cell = (nodeGRCha.x - (m+2), nodeGRCha.y)
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if not(KtCoTrongOpen3(nodeGRCon) and KtCoTrongClose3(nodeGRCon)):
                open3.append(nodeGRCon)
                cell = (nodeGRCha.x - (m+2), nodeGRCha.y)
                solution3[cell] = nodeGRCha.x, nodeGRCha.y


            # cell = (x - (m+2), y)
            # solution[cell] = x, y                                        #Thêm vị trí vào danh sách đường đi
            gameSurface.blit(Imgmui, pygame.Rect(nodeGRCha.x - (m+2), nodeGRCha.y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
            pygame.display.flip()                                        #Cập nhật toàn bộ nội dung cửa sổ

            # open.append(cell)                 # Thêm vào danh sách duyệt
            visited3.add((nodeGRCha.x - (m+2), nodeGRCha.y))           # thêm vào danh sách đã đi và đang trong danh sách duyệt

        if (nodeGRCha.x, nodeGRCha.y - (m+2)) in path3 and (nodeGRCha.x, nodeGRCha.y - (m+2)) not in visited3:  # Kiểm tra phía trên có đường đi không
            xcon = nodeGRCha.x
            ycon = nodeGRCha.y - (m+2)
            gcon = nodeGRCha.g
            hcon = Hx3(xcon, ycon, end_x3, end_y3)
            fcon = gcon + hcon
            nodeGRCon = NodeGR(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen3(nodeGRCon):
                if Kt1_3(nodeGRCon) != False:
                    open3[Kt1_3(nodeGRCon)] = nodeGRCon
                    cell = (nodeGRCha.x, nodeGRCha.y - (m+2))
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if KtCoTrongClose3(nodeGRCon):
                if Kt2_3(nodeGRCon) != False:
                    open3.append(nodeGRCon)
                    close3.remove(nodeGRCon)
                    cell = (nodeGRCha.x, nodeGRCha.y - (m+2))
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if not(KtCoTrongOpen3(nodeGRCon) and KtCoTrongClose3(nodeGRCon)):
                open3.append(nodeGRCon)
                cell = (nodeGRCha.x, nodeGRCha.y - (m+2))
                solution3[cell] = nodeGRCha.x, nodeGRCha.y


            # cell = (x, y - (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeGRCha.x, nodeGRCha.y - (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited3.add((nodeGRCha.x, nodeGRCha.y - (m+2)))

        if(nodeGRCha.x + (m+2), nodeGRCha.y) in path3 and (nodeGRCha.x + (m+2), nodeGRCha.y) not in visited3:   # Kiểm tra đường đi phía dưới

            xcon = nodeGRCha.x + (m+2)
            ycon = nodeGRCha.y
            gcon = nodeGRCha.g
            hcon = Hx3(xcon, ycon, end_x3, end_y3)
            fcon = gcon + hcon
            nodeGRCon = NodeGR(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen3(nodeGRCon):
                if Kt1_3(nodeGRCon) != False:
                    open3[Kt1_3(nodeGRCon)] = nodeGRCon
                    cell = (nodeGRCha.x + (m+2), nodeGRCha.y)
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if KtCoTrongClose3(nodeGRCon):
                if Kt2_3(nodeGRCon) != False:
                    open3.append(nodeGRCon)
                    close3.remove(nodeGRCon)
                    cell = (nodeGRCha.x + (m+2), nodeGRCha.y)
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if not(KtCoTrongOpen3(nodeGRCon) and KtCoTrongClose3(nodeGRCon)):
                open3.append(nodeGRCon)
                cell = (nodeGRCha.x + (m+2), nodeGRCha.y)
                solution3[cell] = nodeGRCha.x, nodeGRCha.y


            # cell = (x + (m+2), y)
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeGRCha.x + (m+2), nodeGRCha.y, m, m))
            pygame.display.flip()
            
            # open.append(cell)
            visited3.add((nodeGRCha.x + (m+2), nodeGRCha.y))

        if(nodeGRCha.x, nodeGRCha.y + (m+2)) in path3 and (nodeGRCha.x, nodeGRCha.y + (m+2)) not in visited3:  # Kiểm tra có đường di bên phải?

            xcon = nodeGRCha.x
            ycon = nodeGRCha.y + (m+2)
            gcon = nodeGRCha.g
            hcon = Hx3(xcon, ycon, end_x3, end_y3)
            fcon = gcon + hcon
            nodeGRCon = NodeGR(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen3(nodeGRCon):
                if Kt1_3(nodeGRCon) != False:
                    open3[Kt1_3(nodeGRCon)] = nodeGRCon
                    cell = (nodeGRCha.x, nodeGRCha.y + (m+2))
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if KtCoTrongClose3(nodeGRCon):
                if Kt2_3(nodeGRCon) != False:
                    open3.append(nodeGRCon)
                    close3.remove(nodeGRCon)
                    cell = (nodeGRCha.x, nodeGRCha.y + (m+2))
                    solution3[cell] = nodeGRCha.x, nodeGRCha.y
            if not(KtCoTrongOpen3(nodeGRCon) and KtCoTrongClose3(nodeGRCon)):
                open3.append(nodeGRCon)
                cell = (nodeGRCha.x, nodeGRCha.y + (m+2))
                solution3[cell] = nodeGRCha.x, nodeGRCha.y


            # cell = (x, y + (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeGRCha.x, nodeGRCha.y + (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited3.add((nodeGRCha.x, nodeGRCha.y + (m+2)))
        
        if (nodeGRCha.x != start_x3 or nodeGRCha.y != start_y3) and (nodeGRCha.x != end_x3 or nodeGRCha.y != end_y3):
            gameSurface.fill((0, 0, 0), pygame.Rect(nodeGRCha.x, nodeGRCha.y, m, m))
            gameSurface.blit(Imgdauchan, pygame.Rect(nodeGRCha.x, nodeGRCha.y, m, m))  #Tải hình ảnh vị trí đang duyệt lên cửa sổ 
            pygame.display.flip()


def backRoute3(x, y):    #Hàm duyệt lại đường đi khi tìm được điểm đích - x: end_x,  y: end_y
    gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
    gameSurface.blit(Imgend, pygame.Rect(end_x3, end_y3, m, m))
    pygame.display.flip()
    i = 0
    while (x, y) != (start_x3, start_y3):    # stop loop when current cells == start cell
        time.sleep(0.03)
        x, y = solution3[x, y]               # "key value" now becomes the new key
        i += 1
        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
        gameSurface.blit(Imgstart, pygame.Rect(x, y, m, m))
        pygame.display.flip()
    SoBuoc(str(i), 1150, 555)


#========================== CT5  ===================
class NodeAS:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f

def setup_maze4(grid, v, t):                          # Hàm tạo mê cung
    global start_x4, start_y4, end_x4, end_y4      # Các biến toàn cục : start_x, start_y là vị trí x, y của điểm bắt đầu : end_x, end_y là vị trí x, y của điểm kết thúc
    for y in range(len(grid)):                 # đọc từng dòng 
        for x in range(len(grid[y])):          # đọc từng ô trong dòng
            character = grid[y][x]             # gán kí tự trên grid vị trí x, y cho biến character
            screen_x = v + (x * (m+2))         # Mỗi ô vuông có kích thước là 21, khoảng cách các ô = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #Dấu cộng là hình bức tường
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #Vẽ hình ảnh bức tường lên cửa sổ
                walls4.append((screen_x, screen_y))                                #Thêm vị trí các bức tường vào biến walls

            if character == " " or character == "e":  #ô trống hoặc e là vị trí trống đánh dấu đi được
                path4.append((screen_x, screen_y))     # thêm các vị trí đi được vào biến path

            if character == "e":                      # e là điểm đích 
                end_x4, end_y4 = screen_x, screen_y     # gán vị trí đích cho biến toàn cục
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #Vẽ điểm đích lên cửa sổ

            if character == "s":                       #s là điểm nguồn
                start_x4, start_y4 = screen_x, screen_y     # gán vị trí nguồn cho biến toàn cục
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #vẽ điểm nguồn lên cửa sổ


def Hx4(x, y, end_x4, end_y4):
    return abs(end_x4 - x)/(m + 2) + abs(end_y4 - y)/(m + 2)

def LayPhanTuTotNhat4():
    min = open4[0]
    for i in open4:
        if i.f < min.f:
            min = i
    open4.remove(min)
    return min

def KtCoTrongOpen4(NodeASCon):
    for i in open4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            return True
    return False

def Kt1_4(NodeASCon):
    k = 0
    for i in open4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            if NodeASCon.f < i.f:
                return k
        k+=1
    return False

def KtCoTrongClose4(NodeASCon):
    for i in close4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            return True
    return False

def Kt2_4(NodeASCon):
    k = 0
    for i in close4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            if NodeASCon.f < i.f:
                return k
        k+=1
    return False


def search4(x,y):      #Hàm chạy tìm đường đi trong mê cung - A*   
    global k
    # x: điểm nguồn    y: điểm đích
    g = 0
    h = Hx4(x, y, end_x4, end_y4)
    f = g + h
    open4.append(NodeAS(x, y, g, h, f))                              #thêm vào danh sách duyệt
    solution4[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(open4) > 0:                             # exit while loop when open queue equals zero
        true = True

        for event in pygame.event.get():                 #Lấy các sự kiện
            if event.type == pygame.QUIT:                #Nếu nhấn nút x trên cửa sổ
                pygame.quit()                            #lệnh tắt cửa sổ
                sys.exit()
            if event.type == pygame.KEYDOWN:             #Sự kiện nhấn bàn phím
                if event.key == pygame.K_UP:             # Nhấn nút up trên bàn phím 
                    if k >= 0.03:                        # k là biến sleep toàn cục
                        k = k - 0.03                     # giảm k để chương trình chạy nhanh hơn
                if event.key == pygame.K_DOWN:           #Nhấn nút down trên bàn phím
                    k = k + 0.03                         # tăng k để chương trình chạy chậm lại
                if event.key == pygame.K_SPACE:          #Khi nhấn space dừng màn hình
                    while true:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    true = False

        time.sleep(k)
        # for i in open:
        #     print(i.f, end='  ')
        # print(end='  -----  ')
        nodeASCha = LayPhanTuTotNhat4()        # lấy phần tử đầu trong danh sách duyệt
        close4.append(nodeASCha)
        # print(nodeASCha.f)

        if nodeASCha.x == end_x4 and nodeASCha.y == end_y4:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRoute4(end_x4, end_y4)
            tg = time.time() - tgstart
            ThoiGian(str(round(tg, 4)), 970, 600)
            break

        if(nodeASCha.x - (m+2), nodeASCha.y) in path4 and (nodeASCha.x - (m+2), nodeASCha.y) not in visited4:      # Kiểm tra bên trái có đường đi không
            xcon = nodeASCha.x - (m+2)
            ycon = nodeASCha.y
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x - (m+2), nodeASCha.y)
                solution4[cell] = nodeASCha.x, nodeASCha.y


            # cell = (x - (m+2), y)
            # solution[cell] = x, y                                        #Thêm vị trí vào danh sách đường đi
            gameSurface.blit(Imgmui, pygame.Rect(nodeASCha.x - (m+2), nodeASCha.y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
            pygame.display.flip()                                        #Cập nhật toàn bộ nội dung cửa sổ

            # open.append(cell)                 # Thêm vào danh sách duyệt
            visited4.add((nodeASCha.x - (m+2), nodeASCha.y))           # thêm vào danh sách đã đi và đang trong danh sách duyệt

        if (nodeASCha.x, nodeASCha.y - (m+2)) in path4 and (nodeASCha.x, nodeASCha.y - (m+2)) not in visited4:  # Kiểm tra phía trên có đường đi không
            xcon = nodeASCha.x
            ycon = nodeASCha.y - (m+2)
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x, nodeASCha.y - (m+2))
                solution4[cell] = nodeASCha.x, nodeASCha.y


            # cell = (x, y - (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeASCha.x, nodeASCha.y - (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited4.add((nodeASCha.x, nodeASCha.y - (m+2)))

        if(nodeASCha.x + (m+2), nodeASCha.y) in path4 and (nodeASCha.x + (m+2), nodeASCha.y) not in visited4:   # Kiểm tra đường đi phía dưới

            xcon = nodeASCha.x + (m+2)
            ycon = nodeASCha.y
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x + (m+2), nodeASCha.y)
                solution4[cell] = nodeASCha.x, nodeASCha.y


            # cell = (x + (m+2), y)
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeASCha.x + (m+2), nodeASCha.y, m, m))
            pygame.display.flip()
            
            # open.append(cell)
            visited4.add((nodeASCha.x + (m+2), nodeASCha.y))

        if(nodeASCha.x, nodeASCha.y + (m+2)) in path4 and (nodeASCha.x, nodeASCha.y + (m+2)) not in visited4:  # Kiểm tra có đường di bên phải?

            xcon = nodeASCha.x
            ycon = nodeASCha.y + (m+2)
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x, nodeASCha.y + (m+2))
                solution4[cell] = nodeASCha.x, nodeASCha.y


            # cell = (x, y + (m+2))
            # solution[cell] = x, y
            gameSurface.blit(Imgmui, pygame.Rect(nodeASCha.x, nodeASCha.y + (m+2), m, m))
            pygame.display.flip()

            # open.append(cell)
            visited4.add((nodeASCha.x, nodeASCha.y + (m+2)))
        
        if (nodeASCha.x != start_x4 or nodeASCha.y != start_y4) and (nodeASCha.x != end_x4 or nodeASCha.y != end_y4):
            gameSurface.fill((0, 0, 0), pygame.Rect(nodeASCha.x, nodeASCha.y, m, m))
            gameSurface.blit(Imgdauchan, pygame.Rect(nodeASCha.x, nodeASCha.y, m, m))  #Tải hình ảnh vị trí đang duyệt lên cửa sổ 
            pygame.display.flip()


def backRoute4(x, y):    #Hàm duyệt lại đường đi khi tìm được điểm đích - x: end_x,  y: end_y
    gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
    gameSurface.blit(Imgend, pygame.Rect(end_x4, end_y4, m, m))
    pygame.display.flip()
    i = 0
    while (x, y) != (start_x4, start_y4):    # stop loop when current cells == start cell
        time.sleep(0.03)
        x, y = solution4[x, y]               # "key value" now becomes the new key
        i += 1
        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
        gameSurface.blit(Imgstart, pygame.Rect(x, y, m, m))
        pygame.display.flip()
    SoBuoc(str(i), 1150, 600)






def KhoiTao():
    global walls4, path4, visited4, open4, close4, solution4
    global walls3, path3, visited3, open3, close3, solution3
    global walls2, path2, visited2, open2, close2, solution2
    global walls, walls1, path, path1, visited, visited1, frontier, frontier1, solution, solution1
    walls = []              #Danh sách vị trí các bức tường
    path = []               #Danh sách vị trí các đường đi
    visited = set()         #Danh sách các vị trí đã đi và đang trong danh sách duyệt
    frontier = deque()      #Danh sách các vị trí chuẩn bị duyệt
    solution = {}           #Danh sách các vị trí đường đi duyệt ngược lại - khi tìm được điểm đích

    walls1 = []
    path1 = []
    visited1 = set()
    frontier1 = deque()
    solution1 = {}

    walls2 = []
    path2 = []
    visited2 = set()
    open2 = deque()
    close2 = deque()
    solution2 = {}

    walls3 = []
    path3 = []
    visited3 = set()
    open3 = deque()
    close3 = deque()
    solution3 = {}

    walls4 = []
    path4 = []
    visited4 = set()
    open4 = deque()
    close4 = deque()
    solution4 = {}



def MENU():    # Hàm Menu
    global m, map1, map2, map3, map4, map5, map6, map7, map8, map9, map10
    WordMENU(1)
    WordBA()

    m = 5             # Kích thước các map khi ở menu 
    LoadImg()         
    x, y = 45, 150    #vị trí các map trên menu
    kc = 230          #Khoảng cách giữa các menu

    setup_maze(grid1, x, y)                        #Vẽ map
    map1 = [x, y + 7*20, x + 7*25, y]              #Vị trí map
    WordMAP('1', map1[0] + 3.5*25, map1[1] + 10)

    setup_maze(grid2, x + kc, y)
    map2 = [x + kc, y + 7*20, x + kc + 7*25, y]
    WordMAP('2', map2[0] + 3.5*25, map2[1] + 10)

    setup_maze(grid3, x + kc*2, y)
    map3 = [x + kc*2, y + 7*20, x + kc*2 + 7*25, y]
    WordMAP('3', map3[0] + 3.5*25, map3[1] + 10)

    setup_maze(grid4, x + kc*3, y)
    map4 = [x + kc*3, y + 7*20, x + kc*3 + 7*25, y]
    WordMAP('4', map4[0] + 3.5*25, map4[1] + 10)

    setup_maze(grid5, x + kc*4, y)
    map5 = [x + kc*4, y + 7*20, x + kc*4 + 7*25, y]
    WordMAP('5', map5[0] + 3.5*25, map5[1] + 10)

    setup_maze(grid6, x, y + kc)
    map6 = [x, y + kc + 7*20, x + 7*25, y + kc]
    WordMAP('6', map6[0] + 3.5*25, map6[1] + 10)

    setup_maze(grid7, x + kc, y + kc)
    map7 = [x + kc, y + kc + 7*20, x + kc + 7*25, y + kc]
    WordMAP('7', map7[0] + 3.5*25, map7[1] + 10)

    setup_maze(grid8, x + kc*2, y + kc)
    map8 = [x + kc*2, y + kc + 7*20, x + kc*2 + 7*25, y + kc]
    WordMAP('8', map8[0] + 3.5*25, map8[1] + 10)

    setup_maze(grid9, x + kc*3, y + kc)
    map9 = [x + kc*3, y + kc + 7*20, x + kc*3 + 7*25, y + kc]
    WordMAP('9', map9[0] + 3.5*25, map9[1] + 10)

    setup_maze(grid10, x + kc*4, y + kc)
    map10 = [x + kc*4, y + kc + 7*20, x + kc*4 + 7*25, y + kc]
    WordMAP('10', map10[0] + 3.5*25, map10[1] + 10)

    pygame.display.flip()

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
    if lc == 2:
        gsurf = gfont.render("> SO SÁNH THUẬT TOÁN", True, (255, 255, 0))
        grect = gsurf.get_rect()
        grect.midtop = (600, 350)
        ss = gameSurface.blit(gsurf, grect)
    pygame.display.flip()
def WordBA():
    global back
    gfont = pygame.font.SysFont('consolas', 20)
    gsurf = gfont.render('QUAY VỀ', True, (255,255,0), (255,0,0))
    grect = gsurf.get_rect()
    grect.midtop = (50, 20)
    back = gameSurface.blit(gsurf, grect)
    pygame.display.flip()

#Hàm vẽ 2 map so sánh
def VeMAP(grid):
    setup_maze(grid, 60, 90)
    setup_maze1(grid, 440, 90)
    setup_maze2(grid, 60, 380)
    setup_maze3(grid, 440, 380)
    setup_maze4(grid, 820, 90)
    pygame.display.flip()

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


def BFS():
    search(start_x, start_y)

def DFS():
    search1(start_x1, start_y1)

def UCS():
    search2(start_x2, start_y2)

def GREEDY():
    search3(start_x3, start_y3)

def ASTAR():
    search4(start_x4, start_y4)


def search4play(x,y):      #Hàm chạy tìm đường đi trong mê cung - A*
    global k
    # x: điểm nguồn    y: điểm đích
    g = 0
    h = Hx4(x, y, end_x4, end_y4)
    f = g + h
    open4.append(NodeAS(x, y, g, h, f))                              #thêm vào danh sách duyệt
    solution4[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(open4) > 0:
        nodeASCha = LayPhanTuTotNhat4()        # lấy phần tử đầu trong danh sách duyệt
        close4.append(nodeASCha)

        if nodeASCha.x == end_x4 and nodeASCha.y == end_y4:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRouteplay(end_x4, end_y4, x, y)
            break

        if(nodeASCha.x - (m+2), nodeASCha.y) in path4 and (nodeASCha.x - (m+2), nodeASCha.y) not in visited4:      # Kiểm tra bên trái có đường đi không
            xcon = nodeASCha.x - (m+2)
            ycon = nodeASCha.y
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x - (m+2), nodeASCha.y)
                solution4[cell] = nodeASCha.x, nodeASCha.y
            visited4.add((nodeASCha.x - (m+2), nodeASCha.y))           # thêm vào danh sách đã đi và đang trong danh sách duyệt

        if (nodeASCha.x, nodeASCha.y - (m+2)) in path4 and (nodeASCha.x, nodeASCha.y - (m+2)) not in visited4:  # Kiểm tra phía trên có đường đi không
            xcon = nodeASCha.x
            ycon = nodeASCha.y - (m+2)
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x, nodeASCha.y - (m+2))
                solution4[cell] = nodeASCha.x, nodeASCha.y
            visited4.add((nodeASCha.x, nodeASCha.y - (m+2)))

        if(nodeASCha.x + (m+2), nodeASCha.y) in path4 and (nodeASCha.x + (m+2), nodeASCha.y) not in visited4:   # Kiểm tra đường đi phía dưới

            xcon = nodeASCha.x + (m+2)
            ycon = nodeASCha.y
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x + (m+2), nodeASCha.y)
                solution4[cell] = nodeASCha.x, nodeASCha.y
            visited4.add((nodeASCha.x + (m+2), nodeASCha.y))

        if(nodeASCha.x, nodeASCha.y + (m+2)) in path4 and (nodeASCha.x, nodeASCha.y + (m+2)) not in visited4:  # Kiểm tra có đường di bên phải?

            xcon = nodeASCha.x
            ycon = nodeASCha.y + (m+2)
            gcon = nodeASCha.g + 1
            hcon = Hx4(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpen4(nodeASCon):
                if Kt1_4(nodeASCon) != False:
                    open4[Kt1_4(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongClose4(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpen4(nodeASCon) and KtCoTrongClose4(nodeASCon)):
                open4.append(nodeASCon)
                cell = (nodeASCha.x, nodeASCha.y + (m+2))
                solution4[cell] = nodeASCha.x, nodeASCha.y
            visited4.add((nodeASCha.x, nodeASCha.y + (m+2)))

def backRouteplay(x, y, start_x4, start_y4):
    while (x, y) != (start_x4, start_y4):
        x1, y1 = x, y
        x, y = solution4[x, y]
        way[x, y] = x1, y1


#Hàm play - cho người chơi
def PLAY(grid):
    global way
    #ATNhacNen.play()
    gameSurface.fill((0, 0, 0))
    WordMENU(2)
    setup_maze4(grid, 325, 100)
    x, y = start_x4, start_y4
    path4.append((x, y))
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
    pygame.display.flip()
    Imglight = pygame.transform.scale(pygame.image.load('bongden.png'),(100, 100))
    light = gameSurface.blit(Imglight, pygame.Rect(900, 150, 100, 100))
    Imgmuitenr = pygame.transform.scale(pygame.image.load('mui_ten_right.png'),(m, m))
    Imgmuitenl = pygame.transform.scale(pygame.image.load('mui_ten_left.png'),(m, m))
    Imgmuitenu = pygame.transform.scale(pygame.image.load('mui_ten_up.png'),(m, m))
    Imgmuitend = pygame.transform.scale(pygame.image.load('mui_ten_down.png'),(m, m))
    way = {}
    sbd = 0
    true = True
    x_next = y_next = 0
    while true:
        gfont = pygame.font.SysFont('consolas', 30)
        gsurf = gfont.render('Số bước di chuyển: {0}'.format(sbd), True, (255,255,0))
        grect = gsurf.get_rect()
        grect.midtop = (600, 50)
        Diem = gameSurface.blit(gsurf, grect)
        pygame.display.flip()
        for event in pygame.event.get():          #Lấy các sự kiện
            if event.type == pygame.QUIT:         #Lệnh thoát cửa sổ
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:       # Sự kiện nhấp chuột
                spot = event.pos                         # Lấy vị trí nhập chuột
                if spot[0] > menu.left and spot[0] < menu.right and spot[1] > menu.top and spot[1] < menu.bottom:  #Nếu vị trí nhấp chuột trong vị trí chữ menu thì quay lại MENU
                        gameSurface.fill((0, 0, 0))
                        true = False
                if spot[0] > light.left and spot[0] < light.right and spot[1] > light.top and spot[1] < light.bottom: #Bấm hướng dẫn
                    visited4.clear()
                    open4.clear()
                    close4.clear()
                    solution4.clear()
                    way.clear()
                    search4play(x, y)
                    x_next, y_next = way[x, y]
                    if x_next < x and y_next == y:
                        gameSurface.blit(Imgmuitenl, pygame.Rect(x_next, y_next, m, m))
                    if x_next > x and y_next == y:
                        gameSurface.blit(Imgmuitenr, pygame.Rect(x_next, y_next, m, m))
                    if x_next == x and y_next > y:
                        gameSurface.blit(Imgmuitend, pygame.Rect(x_next, y_next, m, m))
                    if x_next == x and y_next < y:
                        gameSurface.blit(Imgmuitenu, pygame.Rect(x_next, y_next, m, m))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:   # Lên
                    if(x, y - (m+2)) in path4:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.fill((0, 0, 0), pygame.Rect(x_next, y_next, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x, y - (m+2), m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x, y - (m+2)
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_DOWN: # Xuống
                    if(x, y + (m+2)) in path4:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.fill((0, 0, 0), pygame.Rect(x_next, y_next, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x, y + (m+2), m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x, y + (m+2)
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_LEFT: # Trái
                    if(x - (m+2), y) in path4:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.fill((0, 0, 0), pygame.Rect(x_next, y_next, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x - (m+2), y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x - (m+2), y
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_RIGHT: # Phải
                    if(x + (m+2), y) in path4:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.fill((0, 0, 0), pygame.Rect(x_next, y_next, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x + (m+2), y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x + (m+2), y
                        sbd += 1
                    else:
                        ATChamTuong.play()
        gameSurface.fill((0, 0, 0), pygame.Rect(Diem.left, Diem.top, Diem.right - Diem.left, Diem.bottom - Diem.top))
        if x == end_x4 and y == end_y4:
            ATAnDiem.play()
            #ATNhacNen.stop()
            gameSurface.fill((0, 0, 0))
            true = False


#Hàm cho 2 chương trình cùng chạy - so sánh
def MAIN(grid):
    #ATNhacNen.play()
    global start_x, start_y, start_x1, start_y1, end_x, end_y, end_x1, end_y1, tgstart
    global start_x2, start_y2, end_x2, end_y2
    global start_x3, start_y3, end_x3, end_y3
    global start_x4, start_y4, end_x4, end_y4
    gameSurface.fill((0, 0, 0))
    WordRUN()
    WordMENU(2)
    WordTT('BFS', 200, 72)
    WordTT('DFS', 600, 72)
    WordTT('A*', 1000, 72)
    WordTT('UCS', 200, 362)
    WordTT('GREEDY', 600, 362)
    VeMAP(grid)
    SoSanh('BFS', 840, 420)
    SoSanh('DFS', 840, 465)
    SoSanh('UCS', 840, 510)
    SoSanh('GREEDY', 840, 555)
    SoSanh('A*', 840, 600)

    kt = 50
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(kt, kt))
    start = gameSurface.blit(Imgstart, pygame.Rect(1100, 10, kt, kt))

    Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(kt, kt))
    end = gameSurface.blit(Imgend, pygame.Rect(1180, 10, kt, kt))
    pygame.display.flip()

    true = True
    while true:
        for event in pygame.event.get():          #Lấy các sự kiện
            if event.type == pygame.QUIT:         #Lệnh thoát cửa sổ
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:       # Sự kiện nhấp chuột
                spot = event.pos                         # Lấy vị trí nhập chuột
                if spot[0] > run.left and spot[0] < run.right and spot[1] > run.top and spot[1] < run.bottom:  #Nếu vị trí nhấp chuột trong vị trí chữ RUN thì chạy chương trình
                    tgstart = time.time()
                    thread1 = threading.Thread(target = BFS, args = ())
                    thread2 = threading.Thread(target = DFS, args = ())
                    thread3 = threading.Thread(target = UCS, args = ())
                    thread4 = threading.Thread(target = GREEDY, args = ())
                    thread5 = threading.Thread(target = ASTAR, args = ())

                    thread1.start()                        # Cho 2 chương trình chạy gần như cùng lúc 
                    thread2.start()
                    thread3.start()
                    thread4.start()
                    thread5.start()

                    thread1.join()
                    thread2.join()
                    thread3.join()
                    thread4.join()
                    thread5.join()
                    pygame.display.flip()
                if spot[0] > menu.left and spot[0] < menu.right and spot[1] > menu.top and spot[1] < menu.bottom:  #Nếu vị trí nhấp chuột trong vị trí chữ menu thì quay lại MENU
                    gameSurface.fill((0, 0, 0))
                    ATNhacNen.stop()
                    true = False
                #tự chọn điểm start
                if spot[0] > start.left and spot[0] < start.right and spot[1] > start.top and spot[1] < start.bottom: #Nhấp vào hình ảnh start đề thay đổi vị trí start
                    lc = true
                    while lc:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONUP:        #Sự kiện nhấp chuột
                                spot = event.pos                          #Lấy vị trí nhấp chuột
                                res = []
                                for q in range(1, 4):
                                    for p in range(1, 4):
                                        res.append((spot[0] - q, spot[1] - p))
                                for re in res:
                                    # Khi nhấn chuột trên map 1
                                    if re in path:                        #Kiểm tra vị trí nhấp chuột có hợp lí để đặt điểm nguồn không?
                                        tmpx, tmpy = re[0], re[1]
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x, start_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x1, start_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x2, start_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x3, start_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x4, start_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+760, re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        path.append((start_x, start_y))
                                        start_x, start_y = re[0], re[1]
                                        path.remove((start_x, start_y))

                                        path1.append((start_x1, start_y1))
                                        start_x1, start_y1 = re[0]+380, re[1]
                                        path1.remove((start_x1, start_y1))

                                        path2.append((start_x2, start_y2))
                                        start_x2, start_y2 = re[0], re[1]+290
                                        path2.remove((start_x2, start_y2))

                                        path3.append((start_x3, start_y3))
                                        start_x3, start_y3 = re[0]+380, re[1]+290
                                        path3.remove((start_x3, start_y3))

                                        path4.append((start_x4, start_y4))
                                        start_x4, start_y4 = re[0]+760, re[1]
                                        path4.remove((start_x4, start_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 2
                                    if re in path1:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x, start_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x1, start_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x2, start_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x3, start_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x4, start_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        path.append((start_x, start_y))
                                        start_x, start_y = re[0]-380, re[1]
                                        path.remove((start_x, start_y))

                                        path1.append((start_x1, start_y1))
                                        start_x1, start_y1 = re[0], re[1]
                                        path1.remove((start_x1, start_y1))

                                        path2.append((start_x2, start_y2))
                                        start_x2, start_y2 = re[0]-380, re[1]+290
                                        path2.remove((start_x2, start_y2))

                                        path3.append((start_x3, start_y3))
                                        start_x3, start_y3 = re[0], re[1]+290
                                        path3.remove((start_x3, start_y3))

                                        path4.append((start_x4, start_y4))
                                        start_x4, start_y4 = re[0]+380, re[1]
                                        path4.remove((start_x4, start_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 3
                                    if re in path2:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x, start_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x1, start_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x2, start_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x3, start_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x4, start_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1]-290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1]-290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+760, re[1]-290, m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        path.append((start_x, start_y))
                                        start_x, start_y = re[0], re[1]-290
                                        path.remove((start_x, start_y))

                                        path1.append((start_x1, start_y1))
                                        start_x1, start_y1 = re[0]+380, re[1]-290
                                        path1.remove((start_x1, start_y1))

                                        path2.append((start_x2, start_y2))
                                        start_x2, start_y2 = re[0], re[1]
                                        path2.remove((start_x2, start_y2))

                                        path3.append((start_x3, start_y3))
                                        start_x3, start_y3 = re[0]+380, re[1]
                                        path3.remove((start_x3, start_y3))

                                        path4.append((start_x4, start_y4))
                                        start_x4, start_y4 = re[0]+760, re[1]-290
                                        path4.remove((start_x4, start_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 4
                                    if re in path3:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x, start_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x1, start_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x2, start_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x3, start_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x4, start_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1]-290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1]-290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]+380, re[1]-290, m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        path.append((start_x, start_y))
                                        start_x, start_y = re[0]-380, re[1]-290
                                        path.remove((start_x, start_y))

                                        path1.append((start_x1, start_y1))
                                        start_x1, start_y1 = re[0], re[1]-290
                                        path1.remove((start_x1, start_y1))

                                        path2.append((start_x2, start_y2))
                                        start_x2, start_y2 = re[0]-380, re[1]
                                        path2.remove((start_x2, start_y2))

                                        path3.append((start_x3, start_y3))
                                        start_x3, start_y3 = re[0], re[1]
                                        path3.remove((start_x3, start_y3))

                                        path4.append((start_x4, start_y4))
                                        start_x4, start_y4 = re[0]+380, re[1]-290
                                        path4.remove((start_x4, start_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 5
                                    if re in path4:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x, start_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x1, start_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x2, start_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x3, start_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(start_x4, start_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-760, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-760, re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0]-380, re[1]+290, m, m))
                                        gameSurface.blit(Imgstart, pygame.Rect(re[0], re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        path.append((start_x, start_y))
                                        start_x, start_y = re[0]-760, re[1]
                                        path.remove((start_x, start_y))

                                        path1.append((start_x1, start_y1))
                                        start_x1, start_y1 = re[0]-380, re[1]
                                        path1.remove((start_x1, start_y1))

                                        path2.append((start_x2, start_y2))
                                        start_x2, start_y2 = re[0]-760, re[1]+290
                                        path2.remove((start_x2, start_y2))

                                        path3.append((start_x3, start_y3))
                                        start_x3, start_y3 = re[0]-380, re[1]+290
                                        path3.remove((start_x3, start_y3))

                                        path4.append((start_x4, start_y4))
                                        start_x4, start_y4 = re[0], re[1]
                                        path4.remove((start_x4, start_y4))

                                        pygame.display.flip()
                                        lc = False
                                if spot[0] > start.left and spot[0] < start.right and spot[1] > start.top and spot[1] < start.bottom: #Hủy thay đổi vị trí khi nhấp chuột thêm 1 lần nữa vào hình điểm nguồn
                                    lc = False
                #tự chọn điểm end
                if spot[0] > end.left and spot[0] < end.right and spot[1] > end.top and spot[1] < end.bottom:     #Nhấp vào hình ảnh đích đề thay đổi vị trí đích
                    lc = true
                    res = []
                    while lc:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONUP:
                                spot = event.pos
                                
                                for q in range(1, 4):
                                    for p in range(1, 4):
                                        res.append((spot[0] - q, spot[1] - p))
                                for re in res:
                                    # Khi nhấn chuột trên map 1
                                    if re in path:                        #Kiểm tra vị trí nhấp chuột có hợp lí để đặt điểm nguồn không?
                                        tmpx, tmpy = re[0], re[1]
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x, end_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x1, end_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x2, end_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x3, end_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x4, end_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+760, re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        #path.append((end_x, end_y))
                                        end_x, end_y = re[0], re[1]
                                        #path.remove((end_x, end_y))

                                        #path1.append((end_x1, end_y1))
                                        end_x1, end_y1 = re[0]+380, re[1]
                                        #path1.remove((end_x1, end_y1))

                                        #path2.append((end_x2, end_y2))
                                        end_x2, end_y2 = re[0], re[1]+290
                                        #path2.remove((end_x2, end_y2))

                                        #path3.append((end_x3, end_y3))
                                        end_x3, end_y3 = re[0]+380, re[1]+290
                                        #path3.remove((end_x3, end_y3))

                                        #path4.append((end_x4, end_y4))
                                        end_x4, end_y4 = re[0]+760, re[1]
                                        #path4.remove((end_x4, end_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 2
                                    if re in path1:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x, end_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x1, end_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x2, end_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x3, end_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x4, end_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        #path.append((end_x, end_y))
                                        end_x, end_y = re[0]-380, re[1]
                                        #path.remove((end_x, end_y))

                                        #path1.append((end_x1, end_y1))
                                        end_x1, end_y1 = re[0], re[1]
                                        #path1.remove((end_x1, end_y1))

                                        #path2.append((end_x2, end_y2))
                                        end_x2, end_y2 = re[0]-380, re[1]+290
                                        #path2.remove((end_x2, end_y2))

                                        #path3.append((end_x3, end_y3))
                                        end_x3, end_y3 = re[0], re[1]+290
                                        #path3.remove((end_x3, end_y3))

                                        #path4.append((end_x4, end_y4))
                                        end_x4, end_y4 = re[0]+380, re[1]
                                        #path4.remove((end_x4, end_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 3
                                    if re in path2:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x, end_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x1, end_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x2, end_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x3, end_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x4, end_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1]-290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1]-290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+760, re[1]-290, m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        #path.append((end_x, end_y))
                                        end_x, end_y = re[0], re[1]-290
                                        #path.remove((end_x, end_y))

                                        #path1.append((end_x1, end_y1))
                                        end_x1, end_y1 = re[0]+380, re[1]-290
                                        #path1.remove((end_x1, end_y1))

                                        #path2.append((end_x2, end_y2))
                                        end_x2, end_y2 = re[0], re[1]
                                        #path2.remove((end_x2, end_y2))

                                        #path3.append((end_x3, end_y3))
                                        end_x3, end_y3 = re[0]+380, re[1]
                                        #path3.remove((end_x3, end_y3))

                                        #path4.append((end_x4, end_y4))
                                        end_x4, end_y4 = re[0]+760, re[1]-290
                                        #path4.remove((end_x4, end_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 4
                                    if re in path3:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x, end_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x1, end_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x2, end_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x3, end_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x4, end_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1]-290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1]-290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]+380, re[1]-290, m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        #path.append((end_x, end_y))
                                        end_x, end_y = re[0]-380, re[1]-290
                                        #path.remove((end_x, end_y))

                                        #path1.append((end_x1, end_y1))
                                        end_x1, end_y1 = re[0], re[1]-290
                                        #path1.remove((end_x1, end_y1))

                                        #path2.append((end_x2, end_y2))
                                        end_x2, end_y2 = re[0]-380, re[1]
                                        #path2.remove((end_x2, end_y2))

                                        #path3.append((end_x3, end_y3))
                                        end_x3, end_y3 = re[0], re[1]
                                        #path3.remove((end_x3, end_y3))

                                        #path4.append((end_x4, end_y4))
                                        end_x4, end_y4 = re[0]+380, re[1]-290
                                        #path4.remove((end_x4, end_y4))

                                        pygame.display.flip()
                                        lc = False
                                    #Khi nhấn chuột trên map 5
                                    if re in path4:
                                        # Xóa vị trí điểm nguồn cũ trên cả 2 map 
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x, end_y, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x1, end_y1, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x2, end_y2, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x3, end_y3, m, m))
                                        gameSurface.fill((0, 0, 0), pygame.Rect(end_x4, end_y4, m, m))

                                        # Vẽ lại vị trí mới cho điểm nguồn trên cả 2 map - khi chỉ cần nhấn 1 map
                                        Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-760, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1], m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-760, re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0]-380, re[1]+290, m, m))
                                        gameSurface.blit(Imgend, pygame.Rect(re[0], re[1], m, m))

                                        # Thay đổi vị trí các biến toàn cục
                                        #path.append((end_x, end_y))
                                        end_x, end_y = re[0]-760, re[1]
                                        #path.remove((end_x, end_y))

                                        #path1.append((end_x1, end_y1))
                                        end_x1, end_y1 = re[0]-380, re[1]
                                        #path1.remove((end_x1, end_y1))

                                        #path2.append((end_x2, end_y2))
                                        end_x2, end_y2 = re[0]-760, re[1]+290
                                        #path2.remove((end_x2, end_y2))

                                        #path3.append((end_x3, end_y3))
                                        end_x3, end_y3 = re[0]-380, re[1]+290
                                        #path3.remove((end_x3, end_y3))

                                        #path4.append((end_x4, end_y4))
                                        end_x4, end_y4 = re[0], re[1]
                                        #path4.remove((end_x4, end_y4))

                                        pygame.display.flip()
                                        lc = False
                                if spot[0] > end.left and spot[0] < end.right and spot[1] > end.top and spot[1] < end.bottom: #Hủy thay đổi vị trí khi nhấp chuột thêm 1 lần nữa vào hình điểm nguồn
                                    lc = False          
                


#vòng lặp chính
while True:
    pygame.time.delay(200)
    WordLC(1), WordLC(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:    #Sự kiện Nhấp chuột
            spot = event.pos                      #Lấy vị trí nhấp chuột
            # Chế độ so sánh 
            if spot[0] > ss.left and spot[0] < ss.right and spot[1] > ss.top and spot[1] < ss.bottom:
                gameSurface.fill((0, 0, 0))
                bk = True
                while bk: 
                    KhoiTao()
                    MENU()
                    m = 11
                    LoadImg()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit() 
                        if event.type == pygame.MOUSEBUTTONUP:    #Sự kiện Nhấp chuột
                            spot = event.pos                      #Lấy vị trí nhấp chuột
                            if spot[0] > map1[0] and spot[0] < map1[2] and spot[1] > map1[3] and spot[1] < map1[1]:     # Kiểm tra vị trí nhấp chuột có phải chọn map 1 không
                                MAIN(grid1)                                                                             # Tải map 1 lên 
                            if spot[0] > map2[0] and spot[0] < map2[2] and spot[1] > map2[3] and spot[1] < map2[1]:
                                MAIN(grid2)
                            if spot[0] > map3[0] and spot[0] < map3[2] and spot[1] > map3[3] and spot[1] < map3[1]:
                                MAIN(grid3)
                            if spot[0] > map4[0] and spot[0] < map4[2] and spot[1] > map4[3] and spot[1] < map4[1]:
                                MAIN(grid4)
                            if spot[0] > map5[0] and spot[0] < map5[2] and spot[1] > map5[3] and spot[1] < map5[1]:
                                MAIN(grid5)
                            if spot[0] > map6[0] and spot[0] < map6[2] and spot[1] > map6[3] and spot[1] < map6[1]:
                                MAIN(grid6)
                            if spot[0] > map7[0] and spot[0] < map7[2] and spot[1] > map7[3] and spot[1] < map7[1]:
                                MAIN(grid7)
                            if spot[0] > map8[0] and spot[0] < map8[2] and spot[1] > map8[3] and spot[1] < map8[1]:
                                MAIN(grid8)
                            if spot[0] > map9[0] and spot[0] < map9[2] and spot[1] > map9[3] and spot[1] < map9[1]:
                                MAIN(grid9)
                            if spot[0] > map10[0] and spot[0] < map10[2] and spot[1] > map10[3] and spot[1] < map10[1]:
                                MAIN(grid10)
                            if spot[0] > back.left and spot[0] < back.right and spot[1] > back.top and spot[1] < back.bottom:
                                gameSurface.fill((0, 0, 0))
                                bk = False
            #Chế độ chơi game 
            if spot[0] > play.left and spot[0] < play.right and spot[1] > play.top and spot[1] < play.bottom:
                gameSurface.fill((0, 0, 0))
                bk = True
                while bk:
                    KhoiTao()
                    MENU()
                    m = 20 
                    LoadImg()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit() 
                        if event.type == pygame.MOUSEBUTTONUP:    #Sự kiện Nhấp chuột
                            spot = event.pos                      #Lấy vị trí nhấp chuột
                            if spot[0] > map1[0] and spot[0] < map1[2] and spot[1] > map1[3] and spot[1] < map1[1]:     # Kiểm tra vị trí nhấp chuột có phải chọn map 1 không
                                PLAY(grid1)                                                                             # Tải map 1 lên 
                            if spot[0] > map2[0] and spot[0] < map2[2] and spot[1] > map2[3] and spot[1] < map2[1]:
                                PLAY(grid2)
                            if spot[0] > map3[0] and spot[0] < map3[2] and spot[1] > map3[3] and spot[1] < map3[1]:
                                PLAY(grid3)
                            if spot[0] > map4[0] and spot[0] < map4[2] and spot[1] > map4[3] and spot[1] < map4[1]:
                                PLAY(grid4)
                            if spot[0] > map5[0] and spot[0] < map5[2] and spot[1] > map5[3] and spot[1] < map5[1]:
                                PLAY(grid5)
                            if spot[0] > map6[0] and spot[0] < map6[2] and spot[1] > map6[3] and spot[1] < map6[1]:
                                PLAY(grid6)
                            if spot[0] > map7[0] and spot[0] < map7[2] and spot[1] > map7[3] and spot[1] < map7[1]:
                                PLAY(grid7)
                            if spot[0] > map8[0] and spot[0] < map8[2] and spot[1] > map8[3] and spot[1] < map8[1]:
                                PLAY(grid8)
                            if spot[0] > map9[0] and spot[0] < map9[2] and spot[1] > map9[3] and spot[1] < map9[1]:
                                PLAY(grid9)
                            if spot[0] > map10[0] and spot[0] < map10[2] and spot[1] > map10[3] and spot[1] < map10[1]:
                                PLAY(grid10)
                            if spot[0] > back.left and spot[0] < back.right and spot[1] > back.top and spot[1] < back.bottom:
                                gameSurface.fill((0, 0, 0))
                                bk = False


    
                    

