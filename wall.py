import pygame

brickImage = r".\image\brick.png"
rockImage = r".\image\rock.png"

# 派生普通砖墙类
class Brick(pygame.sprite.Sprite):
    def __init__(self): # 初始化
        super().__init__() # 调用父类初始化方法

        self.image = pygame.image.load(brickImage).convert_alpha() # 加载图片
        self.rect = self.image.get_rect() # 获取图片尺寸

# 派生石头砖墙类
class Iron(pygame.sprite.Sprite):
    def __init__(self): # 初始化
        super().__init__() # 调用父类初始化方法

        self.image = pygame.image.load(rockImage) # 加载图片
        self.rect = self.image.get_rect() # 获取图片尺寸


class Map():
    def __init__(self): # 初始化
        self.brickGroup = pygame.sprite.Group() # 定义普通砖墙精灵组
        self.ironGroup = pygame.sprite.Group() # 定义石头砖墙精灵组

        # 画砖块（数字代表地图中的位置）
        X_1 = [2, 3, 6, 7, 18, 19, 22, 23]
        Y_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]

        X_2 = [10, 11, 14, 15]
        Y_2 = [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]

        X_3 = [4, 5, 6, 7, 18, 19, 20, 21]
        Y_3 = [13, 14]

        X_4 = [12, 13]
        Y_4 = [16, 17]

        X5Y5 = [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]

        for x in X_1:
            for y in Y_1:
                self.brick = Brick() # 生成普通砖墙对象
                self.brick.rect.x, self.brick.rect.y = 3 + x * 24, 3 + y * 24 # 设定普通砖墙位置
                self.brickGroup.add(self.brick) # 添加到普通砖墙精灵组
        for x in X_2:
            for y in Y_2:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_3:
            for y in Y_3:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X_4:
            for y in Y_4:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x, y in X5Y5:
            self.brick = Brick()
            self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brickGroup.add(self.brick)

        # 画石头（数字代表地图中的位置）
        for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
            self.iron = Iron() # 生成石头砖墙对象
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24 # 设定石头砖墙位置
            self.ironGroup.add(self.iron) # 添加到石头砖墙精灵组