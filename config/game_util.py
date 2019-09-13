from pygame.surface import Surface

from config.game_config import GameConfig


class GameUtil:

    # 获取屏正中心的位置,可根据image大小自动适应
    @staticmethod
    def get_center_position(surface_image: Surface):
        width = surface_image.get_width()
        height = surface_image.get_height()
        x = (GameConfig.screen.width - width) / 2
        y = (GameConfig.screen.height - height) / 2
        return x, y
