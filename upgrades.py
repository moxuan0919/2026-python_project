"""upgrades.py ─ 升級系統

【負責】B（遊戲流程）
升級效果就是修改 PlayerStats。9 種升級的名稱與說明已填好。
"""
from dataclasses import dataclass
from cards import PlayerStats


@dataclass(frozen=True)
class Upgrade:
    key: str
    name: str
    description: str


ALL_UPGRADES = [
    Upgrade("gear_up",    "強化齒輪",   "齒輪基礎分數 +10"),
    Upgrade("wire_up",    "高級電線",   "電線基礎分數 +10"),
    Upgrade("battery_up", "高效電池",   "電池基礎分數 +15"),
    Upgrade("chip_up",    "先進晶片",   "晶片基礎分數 +20"),
    Upgrade("extra_swap", "額外工具箱", "每關增加一次換牌機會"),
    Upgrade("extra_play", "延長工時",   "每關增加一次出牌機會"),
    Upgrade("precision",  "精密加工",   "組合額外分數提升 50%"),
    Upgrade("technician", "熟練技師",   "所有得分倍率增加 0.2"),
    Upgrade("backpack",   "擴充背包",   "手牌上限增加一張"),
]


def offer_upgrades(owned_keys: list, n: int = 3) -> list:
    """從「尚未取得」的升級中隨機挑 n 種不同的，回傳 list[Upgrade]。"""
    raise NotImplementedError("B：請實作")


def apply_upgrade(stats: PlayerStats, key: str) -> None:
    """把升級效果套用到 stats，並把 key 記進 stats.upgrades。"""
    raise NotImplementedError("B：請實作")
