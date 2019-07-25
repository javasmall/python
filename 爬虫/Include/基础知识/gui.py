import time
import random
import pygame
from pygame.locals import *


class HeroPlane(object):

    def __init__(self,screen):

        #设置飞机默认的位置
        self.x = 230
        self.y = 600

        #设置要显示内容的窗口
        self.screen = screen

        self.imageName = "../timg.jpg"
        self.image = pygame.image.load(self.imageName).convert()

        #用来存储英雄飞机发射的所有子弹
        self.bulletList = []

    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))

        #判断一下子弹的位置是否越界，如果是，那么就要删除这颗子弹
        #
        #这种方法会漏掉很多需要删除的数据
        # for i in self.bulletList:
        #     if i.y<0:
        #         self.bulletList.remove(i)

        #存放需要删除的对象信息
        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.bulletList.remove(i)

        # del needDelItemList

        #更新及这架飞机发射出的所有子弹的位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

        #修改所有子弹的位置
        # for bullet in self.bulletList:
        #     bullet.y -= 2

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("../timg.jpg").convert()

    def move(self):
        self.y -= 2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyPlane(object):

    def __init__(self,screen):

        #设置飞机默认的位置
        self.x = 0
        self.y = 0

        #设置要显示内容的窗口
        self.screen = screen

        self.imageName = "../timg.jpg"
        self.image = pygame.image.load(self.imageName).convert()

        #用来存储敌人飞机发射的所有子弹
        self.bulletList = []

        self.direction = "right"

    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))

        #判断一下子弹的位置是否越界，如果是，那么就要删除这颗子弹
        #
        #这种方法会漏掉很多需要删除的数据
        # for i in self.bulletList:
        #     if i.y<0:
        #         self.bulletList.remove(i)

        #存放需要删除的对象信息
        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)

        # del needDelItemList

        #更新及这架飞机发射出的所有子弹的位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()


    def move(self):

        #如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2

        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"


if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("../timg.jpg").convert()

    #3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    #4. 创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    #3. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))

        heroPlane.display()

        enemyPlane.move()
        enemyPlane.display()

        #判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                    #控制飞机让其向左移动
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    print("space")
                    heroPlane.sheBullet()

        #通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)

        pygame.display.update()