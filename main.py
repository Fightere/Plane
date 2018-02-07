# -*- coding:utf-8 -*-
import pygame
import time
import random
from pygame.locals import *


class BasePlane(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界,否则一段时间之后会从底下飘上来
                self.bullet_list.remove(bullet)

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


# 飞机类
class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        super().__init__(screen_temp, 230,700 ,"./image/hero.gif")

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5


class EnemyPlane(BasePlane):
    """敌机的类"""
    def __init__(self, screen_temp):
        super().__init__(screen_temp, 0, 0, "./image/enemy0.png")
        self.direction = "right"  # 用来存储飞机默认的显示方向

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        # 判断边界
        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(object):
    def __init__(self,screen_temp,x,y,img_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(img_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


# 子弹类
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        super().__init__(screen_temp,x+40,y-20,"./image/bullet.png")

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


# 敌机子弹类
class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        super().__init__(screen_temp, x + 25, y + 40, "./image/bullet-1.gif")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


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
    # 创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        key_control(hero)
        pygame.display.update()
        time.sleep(0.01)


# 主函数
if __name__ == "__main__":
    main()