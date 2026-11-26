CARD_NAMES = {
    "gear": "齒輪",
    "wire": "電線",
    "battery": "電池",
    "chip": "晶片"
}

CARD_POINTS = {
    "gear": 10,
    "wire": 15,
    "battery": 20,
    "chip": 25
}

CARD_COUNTS = {
    "gear": 10,
    "wire": 10,
    "battery": 10,
    "chip": 10
}

def get_card_name(card):
    return CARD_NAMES[card]

def get_card_points(card, bonuses=None):
    points = CARD_POINTS[card]

    if bonuses is not None:
        points += bonuses.get(card, 0)

    return points

def get_card_types():
    return list(CARD_NAMES.keys())

def get_card_count(card):
    return CARD_COUNTS[card]

def is_valid_card(card):
    return card in CARD_NAMES

def get_card_info(card, bonuses=None):
    return {
        "type": card,
        "name": get_card_name(card),
        "points": get_card_points(card, bonuses),
        "count": get_card_count(card)
    }