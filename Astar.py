from Menu import *




#========================== CT5  ===================
class NodeAS:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f


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


def searchplay(x,y):      #Hàm chạy tìm đường đi trong mê cung - A*   
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

way = {}
def backRouteplay(x, y):
    while (x, y) != (start_x4, start_y4):
        x1, y1 = x, y
        x, y = solution4[x, y]
        way[x, y] = x1, y1




class NodeASplay:
    def __init__(self, x = 0, y = 0, g = 0, h = 0, f = 0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f

def Hxplay(x, y, end_x4, end_y4):
    return abs(end_x4 - x)/(m + 2) + abs(end_y4 - y)/(m + 2)

def LayPhanTuTotNhatplay():
    min = open4[0]
    for i in open4:
        if i.f < min.f:
            min = i
    open4.remove(min)
    return min

def KtCoTrongOpenplay(NodeASCon):
    for i in open4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            return True
    return False

def Kt1_play(NodeASCon):
    k = 0
    for i in open4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            if NodeASCon.f < i.f:
                return k
        k+=1
    return False

def KtCoTrongCloseplay(NodeASCon):
    for i in close4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            return True
    return False

def Kt2_play(NodeASCon):
    k = 0
    for i in close4:
        if NodeASCon.x == i.x and NodeASCon.y == i.y:
            if NodeASCon.f < i.f:
                return k
        k+=1
    return False


def searchplay(x,y):      #Hàm chạy tìm đường đi trong mê cung - A*   
    global k
    # x: điểm nguồn    y: điểm đích
    g = 0
    h = Hx4(x, y, end_x4, end_y4)
    f = g + h
    open4.append(NodeAS(x, y, g, h, f))                              #thêm vào danh sách duyệt
    solution4[x,y] = x,y                                  #Danh các điểm đã đi để khi tìm đường thì duyệt ngược lại 

    while len(open4) > 0:                             # exit while loop when open queue equals zero
        nodeASCha = LayPhanTuTotNhatplay()        # lấy phần tử đầu trong danh sách duyệt
        close4.append(nodeASCha)
        # print(nodeASCha.f)

        if nodeASCha.x == end_x4 and nodeASCha.y == end_y4:    # nếu x, y trùng với vị trí đích thì tìm thấy đường đi - thoát chương trình
            backRouteplay(end_x4, end_y4)
            break

        if(nodeASCha.x - (m+2), nodeASCha.y) in path4 and (nodeASCha.x - (m+2), nodeASCha.y) not in visited4:      # Kiểm tra bên trái có đường đi không
            xcon = nodeASCha.x - (m+2)
            ycon = nodeASCha.y
            gcon = nodeASCha.g + 1
            hcon = Hxplay(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpenplay(nodeASCon):
                if Kt1_play(nodeASCon) != False:
                    open4[Kt1_play(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongCloseplay(nodeASCon):
                if Kt2_play(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x - (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpenplay(nodeASCon) and KtCoTrongCloseplay(nodeASCon)):
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
            hcon = Hxplay(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpenplay(nodeASCon):
                if Kt1_play(nodeASCon) != False:
                    open4[Kt1_play(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongCloseplay(nodeASCon):
                if Kt2_4(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y - (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpenplay(nodeASCon) and KtCoTrongCloseplay(nodeASCon)):
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
            hcon = Hxplay(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpenplay(nodeASCon):
                if Kt1_play(nodeASCon) != False:
                    open4[Kt1_play(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongCloseplay(nodeASCon):
                if Kt2_play(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x + (m+2), nodeASCha.y)
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpenplay(nodeASCon) and KtCoTrongCloseplay(nodeASCon)):
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
            hcon = Hxplay(xcon, ycon, end_x4, end_y4)
            fcon = gcon + hcon
            nodeASCon = NodeAS(xcon, ycon, gcon, hcon, fcon)

            if KtCoTrongOpenplay(nodeASCon):
                if Kt1_play(nodeASCon) != False:
                    open4[Kt1_play(nodeASCon)] = nodeASCon
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if KtCoTrongCloseplay(nodeASCon):
                if Kt2_play(nodeASCon) != False:
                    open4.append(nodeASCon)
                    close4.remove(nodeASCon)
                    cell = (nodeASCha.x, nodeASCha.y + (m+2))
                    solution4[cell] = nodeASCha.x, nodeASCha.y
            if not(KtCoTrongOpenplay(nodeASCon) and KtCoTrongCloseplay(nodeASCon)):
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


def backRouteplay(x, y):    #Hàm duyệt lại đường đi khi tìm được điểm đích - x: end_x,  y: end_y
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