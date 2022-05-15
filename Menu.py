import imp
from KhoiTao import *


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

#load hình ảnh
m = 20 #kích thước các hình khi chạy chính 
def LoadImg(m):
    global Imgwall, Imgstart, Imgend, Imgdauchan, Imgmui
    Imgwall = pygame.transform.scale(pygame.image.load('wall.jpg'),(m, m))         #hình gạch để xây tường
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))         #hình con cáo làm điểm nguồn 
    Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))           #hình chùm nho làm điểm đích
    Imgdauchan = pygame.transform.scale(pygame.image.load('dauchan.png'),(m, m))   #hình dấu chân những điểm đã duyệt
    Imgmui = pygame.transform.scale(pygame.image.load('mui.png'),(m, m))           #hình khói vào danh sách open chuẩn bị duyệt


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


#=====================================  CT3   ================================
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


#=====================================  CT4   ================================
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



#=====================================  CT5   ================================
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




#Hàm vẽ 2 map so sánh
def VeMAP(grid):
    setup_maze(grid, 60, 90)
    setup_maze1(grid, 440, 90)
    setup_maze2(grid, 60, 380)
    setup_maze3(grid, 440, 380)
    setup_maze4(grid, 820, 90)
    pygame.display.flip()

def MENU():    # Hàm Menu
    global m, map1, map2, map3, map4, map5, map6, map7, map8, map9, map10
    WordMENU(1)
    WordBA()

    m = 5             # Kích thước các map khi ở menu 
    LoadImg(5)         
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
    return map1, map2, map3, map4, map5, map6, map7, map8, map9, map10