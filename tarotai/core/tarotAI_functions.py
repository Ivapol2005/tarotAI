import random
import json
from pathlib import Path
from .classCard import Card, tarot_deck

filename_json_spreads = 'spreads.json'

folder_core = Path(__file__).parent
folder_data = folder_core.parent / "data"
target_file = folder_data / filename_json_spreads

with open(target_file, 'r') as file:
    json_spreads = json.load(file)
spreads_list = json_spreads["spreads"]


def help(spread_id=-1, pyPrint = False):
    result = ""

    if spread_id == -1:
        result += "🔮 tarotAI Help:\n"
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
    result = []

    try:
        spread = next(s for s in spreads_list if s['id'] == spreadID)
    except StopIteration:
        result += f"Error: Spread with id {spreadID} not found.\n"
        return result

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

    result = []

    for i, card_info in enumerate(spread["cards"], 1):
        position = card_info.get("position", f"Position {i}")
        card = takeRandomCard()

        entry = {
            "question": position,
            "card": card.name,
            "ifReversed": card.ifReversed,
            "meaning": card.meaning
        }

        result.append(entry)

    if pyPrint:
        result_text = ""
        result_text += f"\n🔮 Spread: {spread['type']}\n"

        for fortune in result:
            result_text += f"{idx}. {fortune['question']}: {fortune['card']} ({orientation})\n"
            result_text += f"   Meaning: {', '.join(card.meaning)}\n"

        result_text += "-" * 30 + "\n"
        print(result_text)

    return result


# help(pyPrint=True)
# tell(pyPrint=True)
