"""cards.py ─ 卡牌與玩家數值（共用資料結構，三個人都會 import）

【負責】A（核心邏輯）
【改動規則】欄位名稱一旦被別人用了就不要改；要改先在群組講。
"""
from dataclasses import dataclass, field

# 卡牌種類代號（程式內部統一用英文代號，顯示時再轉中文）
GEAR, WIRE, BATTERY, CHIP = "gear", "wire", "battery", "chip"

# 代號 -> (中文名稱, 基礎分數)
CARD_INFO = {
    GEAR:    ("齒輪", 10),
    WIRE:    ("電線", 15),
    BATTERY: ("電池", 20),
    CHIP:    ("晶片", 25),
}
CARDS_PER_KIND = 10          # 每種 10 張，共 40 張


@dataclass(frozen=True)
class Card:
    """一張卡牌。只記種類；實際基礎分數要看 PlayerStats（因為有升級）。"""
    kind: str

    @property
    def zh_name(self) -> str:
        return CARD_INFO[self.kind][0]


def _default_base_scores() -> dict:
    return {kind: info[1] for kind, info in CARD_INFO.items()}


@dataclass
class PlayerStats:
    """玩家目前的數值。升級就是修改這個物件。

    注意：升級「從下一關開始生效」，所以 Game 在每關開始時才套用／讀取。
    """
    play_limit: int = 4                 # 每關出牌次數（延長工時 +1）
    swap_limit: int = 2                 # 每關換牌次數（額外工具箱 +1）
    hand_size: int = 8                  # 手牌上限（擴充背包 +1）
    multiplier: float = 1.0             # 分數倍率（熟練技師 +0.2）
    combo_rate: float = 1.0             # 組合額外分數倍率（精密加工 → 1.5）
    base_scores: dict = field(default_factory=_default_base_scores)  # 各卡基礎分數
    upgrades: list = field(default_factory=list)                     # 已取得升級的 key


def build_deck() -> list:
    """回傳一副完整的 40 張牌（未洗牌）。"""
    return [Card(kind) for kind in CARD_INFO for _ in range(CARDS_PER_KIND)]
