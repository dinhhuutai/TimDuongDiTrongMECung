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

#load h??nh ???nh
m = 20 #k??ch th?????c c??c h??nh khi ch???y ch??nh 
def LoadImg(m):
    global Imgwall, Imgstart, Imgend, Imgdauchan, Imgmui
    Imgwall = pygame.transform.scale(pygame.image.load('wall.jpg'),(m, m))         #h??nh g???ch ????? x??y t?????ng
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))         #h??nh con c??o l??m ??i???m ngu???n 
    Imgend = pygame.transform.scale(pygame.image.load('nho.png'),(m, m))           #h??nh ch??m nho l??m ??i???m ????ch
    Imgdauchan = pygame.transform.scale(pygame.image.load('dauchan.png'),(m, m))   #h??nh d???u ch??n nh???ng ??i???m ???? duy???t
    Imgmui = pygame.transform.scale(pygame.image.load('mui.png'),(m, m))           #h??nh kh??i v??o danh s??ch open chu???n b??? duy???t


def KhoiTao():
    global walls4, path4, visited4, open4, close4, solution4
    global walls3, path3, visited3, open3, close3, solution3
    global walls2, path2, visited2, open2, close2, solution2
    global walls, walls1, path, path1, visited, visited1, frontier, frontier1, solution, solution1
    walls = []              #Danh s??ch v??? tr?? c??c b???c t?????ng
    path = []               #Danh s??ch v??? tr?? c??c ???????ng ??i
    visited = set()         #Danh s??ch c??c v??? tr?? ???? ??i v?? ??ang trong danh s??ch duy???t
    frontier = deque()      #Danh s??ch c??c v??? tr?? chu???n b??? duy???t
    solution = {}           #Danh s??ch c??c v??? tr?? ???????ng ??i duy???t ng?????c l???i - khi t??m ???????c ??i???m ????ch

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
def setup_maze(grid, v, t):                          # H??m t???o m?? cung
    global start_x, start_y, end_x, end_y      # C??c bi???n to??n c???c : start_x, start_y l?? v??? tr?? x, y c???a ??i???m b???t ?????u : end_x, end_y l?? v??? tr?? x, y c???a ??i???m k???t th??c
    for y in range(len(grid)):                 # ?????c t???ng d??ng 
        for x in range(len(grid[y])):          # ?????c t???ng ?? trong d??ng
            character = grid[y][x]             # g??n k?? t??? tr??n grid v??? tr?? x, y cho bi???n character
            screen_x = v + (x * (m+2))         # M???i ?? vu??ng c?? k??ch th?????c l?? 21, kho???ng c??ch c??c ?? = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #D???u c???ng l?? h??nh b???c t?????ng
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #V??? h??nh ???nh b???c t?????ng l??n c???a s???
                walls.append((screen_x, screen_y))                                #Th??m v??? tr?? c??c b???c t?????ng v??o bi???n walls

            if character == " " or character == "e":  #?? tr???ng ho???c e l?? v??? tr?? tr???ng ????nh d???u ??i ???????c
                path.append((screen_x, screen_y))     # th??m c??c v??? tr?? ??i ???????c v??o bi???n path

            if character == "e":                      # e l?? ??i???m ????ch 
                end_x, end_y = screen_x, screen_y     # g??n v??? tr?? ????ch cho bi???n to??n c???c
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #V??? ??i???m ????ch l??n c???a s???

            if character == "s":                       #s l?? ??i???m ngu???n
                start_x, start_y = screen_x, screen_y     # g??n v??? tr?? ngu???n cho bi???n to??n c???c
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #v??? ??i???m ngu???n l??n c???a s???

#=====================================  CT2   ================================
def setup_maze1(grid, v, t):                          # H??m t???o m?? cung
    global start_x1, start_y1, end_x1, end_y1         # C??c bi???n to??n c???c : start_x, start_y l?? v??? tr?? x, y c???a ??i???m b???t ?????u : end_x, end_y l?? v??? tr?? x, y c???a ??i???m k???t th??c
    for y in range(len(grid)):                        # ?????c t???ng d??ng 
        for x in range(len(grid[y])):                 # ?????c t???ng ?? trong d??ng
            character = grid[y][x]                    # g??n k?? t??? tr??n grid v??? tr?? x, y cho bi???n character
            screen_x = v + (x * (m+2))                # M???i ?? vu??ng c?? k??ch th?????c l?? 21, kho???ng c??ch c??c ?? = 3
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
def setup_maze2(grid, v, t):                          # H??m t???o m?? cung
    global start_x2, start_y2, end_x2, end_y2      # C??c bi???n to??n c???c : start_x, start_y l?? v??? tr?? x, y c???a ??i???m b???t ?????u : end_x, end_y l?? v??? tr?? x, y c???a ??i???m k???t th??c
    for y in range(len(grid)):                 # ?????c t???ng d??ng 
        for x in range(len(grid[y])):          # ?????c t???ng ?? trong d??ng
            character = grid[y][x]             # g??n k?? t??? tr??n grid v??? tr?? x, y cho bi???n character
            screen_x = v + (x * (m+2))         # M???i ?? vu??ng c?? k??ch th?????c l?? 21, kho???ng c??ch c??c ?? = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #D???u c???ng l?? h??nh b???c t?????ng
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #V??? h??nh ???nh b???c t?????ng l??n c???a s???
                walls2.append((screen_x, screen_y))                                #Th??m v??? tr?? c??c b???c t?????ng v??o bi???n walls

            if character == " " or character == "e":  #?? tr???ng ho???c e l?? v??? tr?? tr???ng ????nh d???u ??i ???????c
                path2.append((screen_x, screen_y))     # th??m c??c v??? tr?? ??i ???????c v??o bi???n path

            if character == "e":                      # e l?? ??i???m ????ch 
                end_x2, end_y2 = screen_x, screen_y     # g??n v??? tr?? ????ch cho bi???n to??n c???c
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #V??? ??i???m ????ch l??n c???a s???

            if character == "s":                       #s l?? ??i???m ngu???n
                start_x2, start_y2 = screen_x, screen_y     # g??n v??? tr?? ngu???n cho bi???n to??n c???c
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #v??? ??i???m ngu???n l??n c???a s???


#=====================================  CT4   ================================
def setup_maze3(grid, v, t):                          # H??m t???o m?? cung
    global start_x3, start_y3, end_x3, end_y3      # C??c bi???n to??n c???c : start_x, start_y l?? v??? tr?? x, y c???a ??i???m b???t ?????u : end_x, end_y l?? v??? tr?? x, y c???a ??i???m k???t th??c
    for y in range(len(grid)):                 # ?????c t???ng d??ng 
        for x in range(len(grid[y])):          # ?????c t???ng ?? trong d??ng
            character = grid[y][x]             # g??n k?? t??? tr??n grid v??? tr?? x, y cho bi???n character
            screen_x = v + (x * (m+2))         # M???i ?? vu??ng c?? k??ch th?????c l?? 21, kho???ng c??ch c??c ?? = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #D???u c???ng l?? h??nh b???c t?????ng
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #V??? h??nh ???nh b???c t?????ng l??n c???a s???
                walls3.append((screen_x, screen_y))                                #Th??m v??? tr?? c??c b???c t?????ng v??o bi???n walls

            if character == " " or character == "e":  #?? tr???ng ho???c e l?? v??? tr?? tr???ng ????nh d???u ??i ???????c
                path3.append((screen_x, screen_y))     # th??m c??c v??? tr?? ??i ???????c v??o bi???n path

            if character == "e":                      # e l?? ??i???m ????ch 
                end_x3, end_y3 = screen_x, screen_y     # g??n v??? tr?? ????ch cho bi???n to??n c???c
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #V??? ??i???m ????ch l??n c???a s???

            if character == "s":                       #s l?? ??i???m ngu???n
                start_x3, start_y3 = screen_x, screen_y     # g??n v??? tr?? ngu???n cho bi???n to??n c???c
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #v??? ??i???m ngu???n l??n c???a s???



#=====================================  CT5   ================================
def setup_maze4(grid, v, t):                          # H??m t???o m?? cung
    global start_x4, start_y4, end_x4, end_y4      # C??c bi???n to??n c???c : start_x, start_y l?? v??? tr?? x, y c???a ??i???m b???t ?????u : end_x, end_y l?? v??? tr?? x, y c???a ??i???m k???t th??c
    for y in range(len(grid)):                 # ?????c t???ng d??ng 
        for x in range(len(grid[y])):          # ?????c t???ng ?? trong d??ng
            character = grid[y][x]             # g??n k?? t??? tr??n grid v??? tr?? x, y cho bi???n character
            screen_x = v + (x * (m+2))         # M???i ?? vu??ng c?? k??ch th?????c l?? 21, kho???ng c??ch c??c ?? = 3
            screen_y = t + (y * (m+2))          # move to the y location of the screen starting at 288

            if character == "+":                  #D???u c???ng l?? h??nh b???c t?????ng
                gameSurface.blit(Imgwall, pygame.Rect(screen_x, screen_y, m, m))  #V??? h??nh ???nh b???c t?????ng l??n c???a s???
                walls4.append((screen_x, screen_y))                                #Th??m v??? tr?? c??c b???c t?????ng v??o bi???n walls

            if character == " " or character == "e":  #?? tr???ng ho???c e l?? v??? tr?? tr???ng ????nh d???u ??i ???????c
                path4.append((screen_x, screen_y))     # th??m c??c v??? tr?? ??i ???????c v??o bi???n path

            if character == "e":                      # e l?? ??i???m ????ch 
                end_x4, end_y4 = screen_x, screen_y     # g??n v??? tr?? ????ch cho bi???n to??n c???c
                gameSurface.blit(Imgend, pygame.Rect(screen_x, screen_y, m, m))   #V??? ??i???m ????ch l??n c???a s???

            if character == "s":                       #s l?? ??i???m ngu???n
                start_x4, start_y4 = screen_x, screen_y     # g??n v??? tr?? ngu???n cho bi???n to??n c???c
                gameSurface.blit(Imgstart, pygame.Rect(screen_x, screen_y, m, m))  #v??? ??i???m ngu???n l??n c???a s???




#H??m v??? 2 map so s??nh
def VeMAP(grid):
    setup_maze(grid, 60, 90)
    setup_maze1(grid, 440, 90)
    setup_maze2(grid, 60, 380)
    setup_maze3(grid, 440, 380)
    setup_maze4(grid, 820, 90)
    pygame.display.flip()

def MENU():    # H??m Menu
    global m, map1, map2, map3, map4, map5, map6, map7, map8, map9, map10
    WordMENU(1)
    WordBA()

    m = 5             # K??ch th?????c c??c map khi ??? menu 
    LoadImg(5)         
    x, y = 45, 150    #v??? tr?? c??c map tr??n menu
    kc = 230          #Kho???ng c??ch gi???a c??c menu

    setup_maze(grid1, x, y)                        #V??? map
    map1 = [x, y + 7*20, x + 7*25, y]              #V??? tr?? map
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