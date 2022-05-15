from Menu import *
from KhoiTao import *
from BFS import *
from DFS import *
from UCS import *
from GREEDY import *
from Astar import *



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
    m = 11
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