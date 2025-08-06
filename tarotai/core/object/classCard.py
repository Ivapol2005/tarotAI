from .loadJSON import load_JSON_data

tarot_deck= load_JSON_data('cards.json')["cards"]

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
