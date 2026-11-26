"""combos.py ─ 組合判定與計分

【負責】A（核心邏輯）

已決定的規則解釋（要改請全組一起討論）：
  1. 組合「包含即可」：只要出的牌裡含有所需零件就算，多出來的牌只算基礎分。
     多種組合同時成立時，只取額外分數最高的一種。
  2. evaluate_combo 回傳「原始」額外分數；精密加工（combo_rate）在 calculate_score 才乘。
  3. 得分 = (基礎分數總和 + 組合額外分數 × combo_rate) × multiplier，最後四捨五入成 int。
"""
from collections import Counter
from cards import Card, PlayerStats, GEAR, WIRE, BATTERY, CHIP

# (組合名稱, 所需零件, 額外分數) ─ 資料表已填好，A 只需寫判定邏輯
COMBOS = [
    ("傳動裝置", Counter({GEAR: 2}), 30),
    ("線路系統", Counter({WIRE: 2}), 40),
    ("儲能裝置", Counter({BATTERY: 2}), 50),
    ("運算核心", Counter({CHIP: 2}), 60),
    ("電力模組", Counter({BATTERY: 1, WIRE: 1}), 40),
    ("控制模組", Counter({BATTERY: 1, WIRE: 1, CHIP: 1}), 100),
    ("重型引擎", Counter({GEAR: 2, BATTERY: 1}), 120),
    ("完整機械", Counter({GEAR: 1, WIRE: 1, BATTERY: 1, CHIP: 1}), 200),
]


def evaluate_combo(cards: list) -> tuple:
    """判定這次出的牌符合哪個組合。

    回傳 (組合名稱, 原始額外分數)；沒有任何組合回傳 ("無", 0)。
    """
    raise NotImplementedError("A：請實作")


def calculate_score(cards: list, stats: PlayerStats) -> int:
    """計算單次出牌得分。

    基礎分數用 stats.base_scores[card.kind]（不是固定值，因為有升級）。
    範例（倍率 1.0）：電池、電線、晶片 → 20+15+25 + 控制模組 100 = 160
    範例（倍率 1.2）：同上 → 192
    """
    raise NotImplementedError("A：請實作")
