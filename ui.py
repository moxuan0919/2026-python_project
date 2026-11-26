"""ui.py ─ 畫面與輸入（先做文字版，之後可換成 tkinter / pygame）

【負責】C（介面與測試）
這裡的函式只負責「顯示」與「讀輸入」，不處理遊戲規則。
"""
from game import Game, PlayResult


def show_status(game: Game) -> None:
    """顯示：關卡名稱、目標分數、目前分數、剩餘出牌／換牌次數。"""
    raise NotImplementedError("C：請實作")


def show_hand(game: Game) -> None:
    """顯示手牌，每張前面標編號（建議從 1 開始，給人看的）。"""
    raise NotImplementedError("C：請實作")


def ask_action() -> str:
    """問玩家要 'play'（出牌）還是 'swap'（換牌）。"""
    raise NotImplementedError("C：請實作")


def ask_indices(hand_size: int) -> list:
    """讓玩家選牌，回傳「從 0 開始」的位置 list（注意編號轉換）。輸入錯誤要重問。"""
    raise NotImplementedError("C：請實作")


def show_play_result(result: PlayResult) -> None:
    """顯示這次出牌的組合名稱與得分。"""
    raise NotImplementedError("C：請實作")


def ask_upgrade(options: list) -> str:
    """顯示三個升級選項，回傳玩家選的 Upgrade.key。"""
    raise NotImplementedError("C：請實作")


def show_summary(summary: dict) -> None:
    """結算畫面：結果、完成關卡數、總得分、獲得的升級。"""
    raise NotImplementedError("C：請實作")


def ask_restart() -> bool:
    """問要不要重新開始。"""
    raise NotImplementedError("C：請實作")
