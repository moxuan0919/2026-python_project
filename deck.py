import random
from cards import CARD_COUNTS

def create_deck():
    deck = []

    for card, count in CARD_COUNTS.items():
        deck.extend([card] * count)

    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def draw_cards(deck, count):
    drawn_cards = []

    for _ in range(count):
        if not deck:
            break

        drawn_cards.append(deck.pop())

    return drawn_cards

def discard_cards(hand, discard_pile, indices):
    if len(indices) != len(set(indices)):
        raise ValueError("不可重複選擇同一張卡牌")

    if any(i < 0 or i >= len(hand) for i in indices):
        raise ValueError("卡牌索引超出範圍")

    removed_cards = [hand[i] for i in indices]

    for i in sorted(indices, reverse=True):
        hand.pop(i)

    discard_pile.extend(removed_cards)

    return removed_cards

def refill_hand(deck, hand, hand_limit=8):
    count = max(0, hand_limit - len(hand))

    hand.extend(draw_cards(deck, count))

    return hand

def initialize_deck(hand_limit=8):
    deck = create_deck()
    shuffle_deck(deck)

    hand = draw_cards(deck, hand_limit)
    discard_pile = []

    return deck, hand, discard_pile

def get_deck_count(deck):
    return len(deck)

def get_discard_count(discard_pile):
    return len(discard_pile)