import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图像并获得外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rec = screen.get_rect()

        # 把每艘新飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rec.centerx
        self.rect.bottom = self.screen_rec.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # 根据移动标志调整飞船位置
        if self.moving_right and self.rect.right <= self.screen_rec.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >= 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top >= 0:
            self.rect.centery -= 1

        if self.moving_down and self.rect.bottom <= self.screen_rec.bottom:
            self.rect.centery += 1

        self.rect.centerx = self.center
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.x = self.screen_rec.centerx
        self.rect.bottom = self.screen_rec.bottom
