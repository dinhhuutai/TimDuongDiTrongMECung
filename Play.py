from Menu import *
from KhoiTao import *
from Astar import *


#Hàm play - cho người chơi
def PLAY(grid):
    #ATNhacNen.play()
    gameSurface.fill((0, 0, 0))
    WordMENU(2)
    setup_maze4(grid, 325, 100)
    x, y = start_x4, start_y4
    path.append((x, y))
    Imgstart = pygame.transform.scale(pygame.image.load('cao.png'),(m, m))
    pygame.display.flip()
    Imglight = pygame.transform.scale(pygame.image.load('bongden.png'),(100, 100))
    light = gameSurface.blit(Imglight, pygame.Rect(900, 150, 100, 100))
    search4(start_x4, start_y4)

    sbd = 0
    true = True
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:   # Lên
                    if(x, y - (m+2)) in path:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x, y - (m+2), m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x, y - (m+2)
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_DOWN: # Xuống
                    if(x, y + (m+2)) in path:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x, y + (m+2), m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x, y + (m+2)
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_LEFT: # Trái
                    if(x - (m+2), y) in path:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x - (m+2), y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x - (m+2), y
                        sbd += 1
                    else:
                        ATChamTuong.play()
                elif event.key == pygame.K_RIGHT: # Phải
                    if(x + (m+2), y) in path:
                        ATDiChuyen.play()
                        gameSurface.fill((0, 0, 0), pygame.Rect(x, y, m, m))
                        gameSurface.blit(Imgstart, pygame.Rect(x + (m+2), y, m, m))    #vẽ hình ảnh chuẩn bị duyệt lên màn hình
                        pygame.display.flip()
                        x, y = x + (m+2), y
                        sbd += 1
                    else:
                        ATChamTuong.play()
        gameSurface.fill((0, 0, 0), pygame.Rect(Diem.left, Diem.top, Diem.right - Diem.left, Diem.bottom - Diem.top))
        if x == end_x and y == end_y:
            ATAnDiem.play()
            #ATNhacNen.stop()
            gameSurface.fill((0, 0, 0))
            true = False