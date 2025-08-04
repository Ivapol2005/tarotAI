import json
from pathlib import Path

filename_json_cards = 'cards.json'

folder_core = Path(__file__).parent
folder_data = folder_core.parent / "data"
target_file = folder_data / filename_json_cards

with open(target_file, 'r') as file:
    json_cards = json.load(file)
tarot_deck= json_cards["cards"]

class Card:
    def __init__(self, id, ifReversed):
        self.id = id
        self.ifReversed = ifReversed
        self.name = None
        self.meaning = None
        self.__set_card_details()

    def __set_card_details(self):
        for card in tarot_deck:
            if card["id"] == self.id:
                self.name = card["name"]
                self.meaning = card["reversed_meaning"] if self.ifReversed else card["meaning"]
                return
        self.name = "error"
        self.meaning = ["unknown"]
