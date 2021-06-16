import pygame
import bulletClass

tank_T1_0 = r".\image\-7094bf8ffccc2cec.jpg"
tank_T1_1 = r".\image\tank_T1_1.png"
tank_T1_2 = r".\image\tank_T1_2.png"
tank_T2_0 = r".\image\tank_T2_0.png"
tank_T2_1 = r".\image\tank_T2_1.png"
tank_T2_2 = r".\image\tank_T2_2.png"

class MyTank(pygame.sprite.Sprite):
    def __init__(self, playerNumber): # 初始化
        super().__init__() # 调用父类初始化方法

        # 初始化玩家生命
        self.life = True
        # 判断玩家并设置坦克的三个等级
        if playerNumber == 1:
            # 加载图片并修改像素格式
            self.tank_L0_image = pygame.image.load(tank_T1_0).convert_alpha()
            self.tank_L1_image = pygame.image.load(tank_T1_1).convert_alpha()
            self.tank_L2_image = pygame.image.load(tank_T1_2).convert_alpha()
        if playerNumber == 2:
            # 加载图片并修改像素格式
            self.tank_L0_image = pygame.image.load(tank_T2_0).convert_alpha()
            self.tank_L1_image = pygame.image.load(tank_T2_1).convert_alpha()
            self.tank_L2_image = pygame.image.load(tank_T2_2).convert_alpha()
        # 初始化玩家等级
        self.level = 0
        # 初始坦克为0级
        self.tank = self.tank_L0_image
        # 获取运动中的两种图片（创建一个新的子Surface对象）
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        self.rect = self.tank_R0.get_rect()
        # 初始化玩家位置
        if playerNumber == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        if playerNumber == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24

        self.speed = 3 # 初始化坦克速度
        self.dir_x, self.dir_y = 0, -1 # 初始化坦克方向
        self.life = 3 # 初始化坦克生命
        self.bulletNotCooling = True # 初始化子弹冷却
        self.bullet = bulletClass.Bullet() # 创建子弹对象

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
        # 修改子弹参数
        if self.level == 1:
            self.bullet.speed = 12
            self.bullet.strong = False
        if self.level == 2:
            self.bullet.speed = 16
            self.bullet.strong = True
        if self.level == 3:
            self.bullet.speed = 20
            self.bullet.strong = True
    # 玩家升级
    def levelUp(self):
        if self.level < 2:
            self.level += 1
        if self.level == 1:
            self.tank = self.tank_L1_image
            self.bullet.speed = 12
            self.bullet.strong = False
        elif self.level == 2:
            self.tank = self.tank_L2_image
            self.bullet.speed = 16
            self.bullet.strong = True
        elif self.level == 3:
            self.bullet.speed = 20
            self.bullet.strong = True
    # 玩家降级
    def levelDown(self):
        if self.level > 0:
            self.level -= 1
        if self.level == 0:
            self.tank = self.tank_L0_image
            self.bullet.speed = 8
            self.bullet.strong = False
        elif self.level == 1:
            self.tank = self.tank_L1_image
            self.bullet.speed = 12
            self.bullet.strong = False
        elif self.level == 2:
            self.bullet.speed = 16
            self.bullet.strong = True
    # 玩家移动并进行碰撞检测
    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1) # 移动
        # 更改坦克方向图片
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        self.dir_x, self.dir_y = 0, -1
        if self.rect.top < 3: # 边界检测
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None): # 砖墙检测
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None): # 坦克检测
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False

    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        return False

    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        return False

    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        return False