from Menu import *



#=====================   CT3    =======================
class NodeUCS:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f


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