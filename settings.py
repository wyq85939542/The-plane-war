class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        # 飞船都设置

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 10
        self.bullet_height = 40
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=10
        #外星人设置
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #飞船设置
        self.ship_speed_factor=30
        self.ship_limit=10
