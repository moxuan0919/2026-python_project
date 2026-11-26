from collections import Counter
from cards import get_card_points, is_valid_card

COMBOS = [
    ("傳動裝置", {"gear": 2}, 30),
    ("線路系統", {"wire": 2}, 40),
    ("儲能裝置", {"battery": 2}, 50),
    ("運算核心", {"chip": 2}, 60),
    ("電力模組", {"battery": 1, "wire": 1}, 40),
    ("控制模組", {"battery": 1, "wire": 1, "chip": 1}, 100),
    ("重型引擎", {"gear": 2, "battery": 1}, 120),
    ("完整機械", {"gear": 1, "wire": 1,
                  "battery": 1, "chip": 1}, 200)
]

def validate_cards(cards):
    if not 1 <= len(cards) <= 4:
        raise ValueError("每次必須打出1至4張卡牌")

    for card in cards:
        if not is_valid_card(card):
            raise ValueError("無效的卡牌")

def detect_combo(cards):
    validate_cards(cards)

    card_counts = Counter(cards)

    best_name = "無組合"
    best_bonus = 0

    for name, requirements, bonus in COMBOS:

        if all(card_counts[card] >= count
               for card, count in requirements.items()):

            if bonus > best_bonus:
                best_name = name
                best_bonus = bonus

    return best_name, best_bonus

def calculate_base_score(cards, card_bonuses=None):
    validate_cards(cards)

    return sum(
        get_card_points(card, card_bonuses)
        for card in cards
    )

def calculate_score(cards, card_bonuses=None,
                    combo_multiplier=1.0,
                    score_multiplier=1.0):

    base_score = calculate_base_score(cards, card_bonuses)

    combo_name, combo_bonus = detect_combo(cards)

    combo_bonus *= combo_multiplier

    total_score = round(
        (base_score + combo_bonus) * score_multiplier
    )

    return {
        "combo_name": combo_name,
        "base_score": base_score,
        "combo_bonus": combo_bonus,
        "score_multiplier": score_multiplier,
        "total_score": total_score
    }