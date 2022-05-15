from Menu import *



#==========================  CT4   =============================
class NodeGR:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f


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