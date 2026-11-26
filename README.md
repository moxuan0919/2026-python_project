# 廢土零件行 ─ 專案骨架

## 分工
| 組員 | 檔案 | 驗收 |
|---|---|---|
| A 核心邏輯 | `cards.py`（已完成）、`combos.py`、`deck.py` | `pytest tests/test_combos.py tests/test_deck.py` 全過 |
| B 遊戲流程 | `game.py`、`upgrades.py` | `pytest tests/test_game.py` 全過（需要 A 完成；A 未完成前可先寫自己的部分） |
| C 介面與測試 | `ui.py`、`main.py`（已寫好主迴圈） | `python main.py` 能玩完整一局 |

## 依賴方向（不要反過來）
`ui.py / main.py (C)` → `game.py (B)` → `combos.py / deck.py / cards.py (A)`

## 介面規則
1. 函式簽名、類別屬性名稱是「合約」，要改先通知另外兩個人。
2. 手牌位置（indices）在程式內一律從 **0** 開始；給玩家看的編號從 1 開始，轉換只在 `ui.py` 做。
3. 卡牌種類在程式內用英文代號（`gear / wire / battery / chip`），中文只在顯示時用。
4. 還沒實作的函式會 `raise NotImplementedError`，實作完就刪掉那一行。

## 已決定的規則解釋（可討論後修改）
- 組合「包含即可」，多個組合成立取額外分數最高的一個。
- 得分 = (基礎分數總和 + 組合額外分數 × combo_rate) × multiplier，四捨五入為整數。
- 精密加工 = combo_rate 變 1.5。熟練技師 = multiplier +0.2。
- 升級從下一關開始生效；只有過第 1、2 關後會出現升級。
- 抽牌堆不夠時，把棄牌堆洗回去再抽。

## 開發流程
```
pip install pytest
pytest            # 一開始會全部失敗（NotImplementedError），這是正常的
```
