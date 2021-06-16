import pygame
import random
import bulletClass


class EnemyTank(pygame.sprite.Sprite):
    def __init__(self, x = None, kind = None, isred = None):
        super().__init__()

        # 坦克出现前动画是否播放
        self.flash = False
        self.times = 100
        # 随机选择坦克类型
        self.kind = kind
        if not kind:
            self.kind = random.randrange(1, 5)
        # 选择敌军坦克种类
        if self.kind == 1:
            self.enemy_x_0 = pygame.image.load(r".\image\enemy_1_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r".\image\enemy_1_3.png").convert_alpha()
        if self.kind == 2:
            self.enemy_x_0 = pygame.image.load(r".\image\enemy_2_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r".\image\enemy_2_3.png").convert_alpha()
        if self.kind == 3:
            self.enemy_x_0 = pygame.image.load(r".\image\enemy_3_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r".\image\enemy_3_3.png").convert_alpha()
        if self.kind == 4:
            self.enemy_x_0 = pygame.image.load(r".\image\enemy_4_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r".\image\enemy_4_3.png").convert_alpha()
        self.enemy_3_0 = pygame.image.load(r".\image\enemy_3_0.png").convert_alpha()
        self.enemy_3_2 = pygame.image.load(r".\image\enemy_3_2.png").convert_alpha()

        # 判断是否为红色坦克
        self.isred = isred
        if not None:
            self.isred = random.choice((True, False, False, False, False))
        if self.isred:
            self.tank = self.enemy_x_3
        else:
            self.tank = self.enemy_x_0
        # 随机选取坦克出生位置
        self.x = x
        if not self.x:
            self.x = random.choice([1, 2, 3])
        self.x -= 1

        # 获取运动中的两种图片（创建一个新的子Surface对象）
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.rect = self.tank_R0.get_rect()
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3 + 0 * 24

        self.speed = 1 # 初始化坦克速度
        self.dir_x, self.dir_y = 0, 1 # 初始化坦克方向
        self.life = 1 #初始化坦克生命
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet() # 创建子弹对象
        # 碰撞检测（发生则改变方向）
        self.dirChange = False
        # 设置每种坦克不同的属性
        if self.kind == 2:
            self.speed = 3
        if self.kind == 3:
            self.life = 3

    def shoot(self):
        self.bullet.life = True # 设置子弹生命
        self.bullet.changeImage(self.dir_x, self.dir_y) # 将子弹方向设为与坦克方向一致
        # 将子弹射出位置设定为坦克中心
        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
    # 敌方移动并进行碰撞检测
    def move(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y) # 移动
        # 更改坦克方向图片
        if self.dir_x == 0 and self.dir_y == -1:
            self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        elif self.dir_x == 0 and self.dir_y == 1:
            self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        elif self.dir_x == -1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        elif self.dir_x == 1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        # 边界检测（发生碰撞则后退一次并随机选择下一个方向）
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        # 砖墙检测+坦克检测
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None) \
                or pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))