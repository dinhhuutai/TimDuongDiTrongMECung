from Menu import *

#====================== CT1 =====================

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