from Play import *
from Sosanh import *


#vòng lặp chính
while True:
    pygame.time.delay(200)
    play = WordLC(1)
    ss = WordLC(2)
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
                    map1, map2, map3, map4, map5, map6, map7, map8, map9, map10 = MENU()
                    m = 11
                    LoadImg(16)
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