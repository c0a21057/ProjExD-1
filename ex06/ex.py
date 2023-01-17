
import sys
import random,time
import pygame as pg
import maze_maker as mm

class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

class Maze:
    def __init__(self,maze_lst,scr:Screen):
        self.sfc=pg.Surface((1200,900)) 
        self.sfc.set_colorkey((0,0,0))
        color=["white", "blue"] #迷路の色
        for y in range(len(maze_lst)): 
            for x in range(len(maze_lst[y])):
                pg.draw.rect(self.sfc,color[maze_lst[y][x]],(x*50,y*50,50,50)) #迷路の一マスの大きさと間隔
        self.rct=self.sfc.get_rect()

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

def check_bound(obj_rct, scr_rct):
    # 第1引数；敵rect
    # 第2引数：スクリーンrect
    # 範囲内：+1/範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main2():
    clock = pg.time.Clock()
    scr = Screen("食べろにょろにょろ", (1600,900), "fig/pg_bg.jpg")

    make_lst=mm.make_maze(18,18) #マスの数
    print (make_lst)
    maze=Maze(make_lst,scr)

    color_red = pg.Color(255, 0, 0)
    color_green = pg.Color(0, 255, 0)
    color_yello = pg.Color(255, 212, 0)
    screen = pg.display.set_mode((900, 1000)) #スクリーンの大きさ
    pg.display.set_caption("蛇")
    arr = [([0] * 41) for i in range(61)]  
    x = 10  # 蛇の初期x座標
    y = 10  # 蛇の初期y座標
    foodx = random.randint(1, 60)  # 食べ物のx座標
    foody = random.randint(1, 40)  # 食べ物のy座標
    arr[foodx][foody] = -1
    snake_lon = 3  # 蛇の長さ
    way = 1  # 蛇の運動方向
    spd = 1 # 蛇の移動速度(筒井)
    t = 0.1 # 蛇の移動速度変更用の変数(筒井)

    while True:
        scr.blit()
        maze.blit(scr)
        
        #screen.fill(color_white)
        time.sleep(0.1)
        for event in pg.event.get():  
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                    way = 1
                if (event.key == pg.K_LEFT) and (way != 1):  # 左
                    way = 2
                if (event.key == pg.K_UP) and (way != 4):  # 上
                    way = 3
                if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                    way = 4
        if way == 1:
            x += spd # 1をspdに変更(筒井)
        if way == 2:
            x -= spd
        if way == 3:
            y -= spd
        if way == 4:
            y += spd
        if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 死亡(壁、自分の体をぶつかったら)
            sys.exit()
        arr[x][y] = snake_lon
        for a, b in enumerate(arr, 1):
            for c, d in enumerate(b, 1):
                # 食べ物は-1，空地は0，蛇の位置は正数
                if (d > 0):
                    # print(a,c) #蛇の座標を表示
                    arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                    pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                if (d < 0):
                    pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))  
        # 蛇の移動速度(筒井)
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                    way = 1
                if (event.key == pg.K_LEFT) and (way != 1):  # 左
                    way = 2
                if (event.key == pg.K_UP) and (way != 4):  # 上
                    way = 3
                if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                    way = 4

        if (x == foodx) and (y == foody):   #蛇が食べ物を食べたら
            snake_lon += 1    #長さ+1
            t -= t/4 # 蛇が現在の速度の1/4加速(筒井)

            while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                foodx = random.randint(1, 60)
                foody = random.randint(1, 40)
            arr[foodx][foody] = -1

        pg.display.update()
        clock.tick(1000)

if __name__ == '__main__':
    pg.init()
    main2()
    pg.quit()
    sys.exit()   

