from Menu import *


#=====================================  CT2   ================================

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