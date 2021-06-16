import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self): # 初始化
        super().__init__()
        # 加载图片
        self.bullet_up = pygame.image.load(r".\image\bullet_up.png")
        self.bullet_down = pygame.image.load(r".\image\bullet_down.png")
        self.bullet_left = pygame.image.load(r".\image\bullet_left.png")
        self.bullet_right = pygame.image.load(r".\image\bullet_right.png")

        self.dir_x, self.dir_y = 0, 0 # 初始化子弹方向
        self.speed = 8 # 初始化子弹速度
        self.life = False # 初始化子弹生命
        self.strong = False
        self.bullet = self.bullet_up
        self.rect = self.bullet.get_rect() # 获取图片尺寸
    # 根据形参修改子弹方向
    def changeImage(self, dir_x, dir_y):
        self.dir_x, self.dir_y = dir_x, dir_y
        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet = self.bullet_up
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet = self.bullet_down
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet = self.bullet_left
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet = self.bullet_right
    # 移动子弹
    def move(self):
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y)
        # 碰撞地图边界
        if self.rect.top < 3: # 上边界
            self.life = False
        if self.rect.bottom > 630 - 3: # 下边界
            self.life = False
        if self.rect.left < 3: # 左边界
            self.life = False
        if self.rect.right > 630 - 3: # 右边界
            self.life = False

        # 碰撞 brickGroup
        # if pygame.sprite.spritecollide(self, brickGroup, True, None):
        #    self.life = False
        #    moving = 0
        # 碰撞 ironGroup
        # if self.strong:
        #    if pygame.sprite.spritecollide(self, ironGroup, True, None):
        #        self.life = False
        # else:
        #    if pygame.sprite.spritecollide(self, ironGroup, False, None):
        #        self.life = False
        #    moving = 0
        # return moving