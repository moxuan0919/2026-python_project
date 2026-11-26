"""game.py ─ 遊戲主流程（UI 只透過這個類別操作遊戲）

【負責】B（遊戲流程）
C 只呼叫 Game 的公開方法與屬性，不要直接碰 Deck / combos。
"""
from dataclasses import dataclass, field
from enum import Enum

from cards import Card, PlayerStats
from deck import Deck

# (訂單名稱, 目標分數)
LEVELS = [
    ("修復發電機", 300),
    ("修復廢土機器人", 600),
    ("修復能源核心", 1000),
]


class Phase(Enum):
    PLAYING = "playing"            # 關卡進行中，等玩家出牌／換牌
    CHOOSE_UPGRADE = "upgrade"     # 剛過關，等玩家選升級
    WON = "won"                    # 三關全過
    LOST = "lost"                  # 出牌次數用完且未達標


@dataclass
class PlayResult:
    """play() 的回傳值，給 UI 顯示用。"""
    cards: list                    # 這次出的牌
    combo_name: str                # 組合名稱（"無" 代表沒組合）
    score: int                     # 這次得分
    level_score: int               # 本關累積分數
    cleared: bool                  # 是否過關
    phase: Phase                   # 出牌後的遊戲階段


class Game:
    def __init__(self):
        self.stats = PlayerStats()
        self.deck = Deck()
        self.hand: list = []
        self.level_index = 0            # 0~2
        self.level_score = 0
        self.plays_left = 0
        self.swaps_left = 0
        self.total_score = 0            # 全局累積總得分（結算畫面用）
        self.phase = Phase.PLAYING
        self.upgrade_options: list = [] # phase == CHOOSE_UPGRADE 時有值
        self.start_level()

    # ── 給 UI 讀的資訊 ───────────────────────────
    @property
    def level_name(self) -> str:
        return LEVELS[self.level_index][0]

    @property
    def level_target(self) -> int:
        return LEVELS[self.level_index][1]

    # ── 給 UI 呼叫的操作 ─────────────────────────
    def start_level(self) -> None:
        """開始當前關卡：分數歸零、恢復次數（讀 stats）、重新洗牌、抽滿手牌。"""
        raise NotImplementedError("B：請實作")

    def play(self, indices: list) -> PlayResult:
        """出牌。indices 是手牌的位置（1~4 張，不可重複、不可越界，否則 raise ValueError）。
        流程：算分 → 累加 → 扣出牌次數 → 棄牌補牌 → 判定過關／失敗／下一步。"""
        raise NotImplementedError("B：請實作")

    def swap(self, indices: list) -> None:
        """換牌（1~4 張）。不得分、不扣出牌次數，扣一次換牌機會。
        沒有換牌機會時 raise ValueError。"""
        raise NotImplementedError("B：請實作")

    def choose_upgrade(self, key: str) -> None:
        """選擇升級（key 必須在 upgrade_options 內），然後進入下一關。"""
        raise NotImplementedError("B：請實作")

    def restart(self) -> None:
        """重新開始整局。"""
        raise NotImplementedError("B：請實作")

    def summary(self) -> dict:
        """結算資料：{"result": "勝利"/"失敗", "levels_cleared": int,
        "total_score": int, "upgrades": [升級名稱, ...]}"""
        raise NotImplementedError("B：請實作")
