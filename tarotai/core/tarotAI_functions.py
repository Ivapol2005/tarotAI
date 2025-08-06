import random
import json
from pathlib import Path
from object.classCard import Card, tarot_deck
from object.classSpread import Spread, spreads_list
from interpreter import get_tarot_interpretation
# from interpreter import askAI


def help(spread_id=-1, pyPrint = False):
    result = ""

    if spread_id == -1:
        result += "🔮 tarotAI Help:\n"
        result += "-" * 30 + "\n"
        result += "  tell(spreadID=0, useReversed=False) - perform a card spread.\n"
        result += "  spreadID - the index of the spread from the list of spreads.\n"
        result += "  useReversed - True = allow reversed cards, False = no reversed cards.\n"
        result += "  Available spreads:\n"
        result += "   id: spread type\n"
        for s in spreads_list:
            result += f"   {s['id']}: {s['type']}\n"
        result += "  To know more about particular spread type help([spread id])\n"
    else:
        try:
            spread = next(s for s in spreads_list if s['id'] == spread_id)
            result += f"Spread ID {spread['id']}: {spread['type']}\n"
            result += "Positions:\n"
            for card_info in spread['cards']:
                position = card_info.get('position', 'Unknown position')
                card = card_info.get('card')
                card_str = str(card) if card is not None else '(no card assigned)'
                result += f" - {position}: {card_str}\n"
        except StopIteration:
            result += f"Error: Spread with id {spread_id} not found.\n"
        except Exception as e:
            result += f"Error: {e}\n"

    if pyPrint:
        print(result)

    return result


def tell(spreadID=0, useReversed=False, pyPrint = False):
    spread_cur = Spread(spreadID)
    used_cards = []

    def takeRandomCard():
        while True:
            card_data = random.choice(tarot_deck)
            card_id = card_data["id"]
            if card_id not in used_cards:
                used_cards.append(card_id)
                reversed_tag = bool(random.getrandbits(1)) if useReversed else False
                card_obj = Card(card_id, reversed_tag)
                return card_obj

    for i, position_info in enumerate(spread_cur.positions, 1):
        position = position_info.get("position", f"Position {i}")
        card = takeRandomCard()
        spread_cur.set_card(position_info, card)

    if pyPrint:
        print(spread_cur)

    ifAskAI = True #make changeable in future versions
    if ifAskAI:
        askAI(spread_cur)

    return spread_cur


def askAI(spread):
    spread_str = str(spread)
    result_AI = get_tarot_interpretation(spread_str)
    print(result_AI)


# help(pyPrint=True)
tell(useReversed=True)
