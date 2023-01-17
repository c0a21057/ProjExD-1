
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
    fonto = pg.font.Font(None,80)
    fonto2 = pg.font.Font(None,30)
    appnum = 3 #りんごゲットのノルマ(坂本)
    app = fonto2.render((f"APPLE:{appnum}"),True,(0,0,0)) #残りのりんごの獲得ノルマ表示(坂本)
    clear = fonto.render("Game Clear",True,(0,0,255))#ゲームクリアの表示(坂本)
    gover = fonto.render("Game Over",True,(255,0,0))#ゲームオーバーの表示(坂本)
    game = True #ゲームが続いているかのフラグ(坂本)

    tekix = random.randint(1, 60)  # 敵のx座標
    tekiy = random.randint(1, 40)  # 敵のy座標
    arr[tekix][tekiy] = -2

    teki_sfc = pg.Surface((10, 10)) # 正方形の空のSurface
    pg.draw.rect(teki_sfc, color_yello, (0, 0, 10, 10))
    teki_rct = teki_sfc.get_rect()
    teki_rct.centerx = tekix*10
    teki_rct.centery = tekiy*10

    xy = [+3,-3, 0]        #敵の移動と方向    
    vx = random.choice(xy)
    vy = random.choice(xy)

    font = pg.font.Font(None, 30) #スコアの文字列
    scor = 0 #スコアの初期値

    st = time.time()


    while True:
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

