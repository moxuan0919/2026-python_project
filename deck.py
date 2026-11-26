"""deck.py ─ 牌堆（抽牌堆 + 棄牌堆）

【負責】A（核心邏輯）
"""
from cards import Card, build_deck


class Deck:
    def __init__(self):
        """建立 40 張牌並洗牌。"""
        raise NotImplementedError("A：請實作")

    def draw(self, n: int) -> list:
        """抽 n 張回傳。抽牌堆不夠時，把棄牌堆洗回去再抽；真的不夠就有幾張給幾張。"""
        raise NotImplementedError("A：請實作")

    def discard(self, cards: list) -> None:
        """把用掉或丟掉的牌放進棄牌堆。"""
        raise NotImplementedError("A：請實作")

    def reset(self) -> None:
        """每關開始：所有牌（含棄牌堆）全部收回並重新洗牌。"""
        raise NotImplementedError("A：請實作")

    @property
    def remaining(self) -> int:
        """抽牌堆剩餘張數。"""
        raise NotImplementedError("A：請實作")
