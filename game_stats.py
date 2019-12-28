1  #!/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : game_stats.py
4  # @Author: JO_KAAN
5  # @Date  : 2019/6/16
6  # @Desc  :
class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化游戏的统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏一开始设置为非活动状态
        self.game_active = False

        # 在任何情况下都不重置最高分数
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1