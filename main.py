# -*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *


# 飞机类
class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 230
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./image/hero.gif")
        self.bullet_list = [] # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


# 子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./image/bullet.png")

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 5


# 键盘控制方法
def key_control(hero):
    # 获取事件
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            pygame.quit()
            exit()
        # 判断是否按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否为a或者←
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left()
                print('left')
            # 检测按键是否为或者→
            elif event.key == K_d or event.key == K_RIGHT:
                hero.move_right()
                print("right")
            # 检测是不是空格键
            elif event.key == K_SPACE:
                print("space")
                hero.fire()


# 主函数
def main():
    # 窗口大小
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 创建一个背景图片
    background = pygame.image.load("./image/background.jpg")
    # 创建一个自己飞机对象
    hero = HeroPlane(screen)

    while True:
        screen.blit(background,(0, 0))
        hero.display()
        key_control(hero)
        pygame.display.update()
        time.sleep(0.01)


# 主函数
if __name__ == "__main__":
    main()