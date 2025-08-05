from .loadJSON import load_JSON_data

spreads_list = load_JSON_data('spreads.json')["spreads"]

class Spread:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.positions = None
        self.__set_spread_details()

    def __repr__(self):
        result_text = ""
        result_text += f"\n🔮 Spread: {self.name}\n"
        result_text += "-" * 30 + "\n"

        for idx, pos in enumerate(self.positions, 1):
            position_name = pos.get("position", f"Position {idx}")
            card = pos.get("card")  # should be Card object

            orientation = "Reversed" if card.ifReversed else "Upright"
            meanings = ", ".join(card.meaning) if isinstance(card.meaning, list) else str(card.meaning)

            result_text += f"{idx}. {position_name}: {card.name} ({orientation})\n"
            result_text += f"   Meaning: {meanings}\n"

        result_text += "-" * 30 + "\n"
        return result_text

    def __set_spread_details(self):
        for spread in spreads_list:
            if spread["id"] == self.id:
                self.name = spread["type"]
                self.positions = spread["cards"]
                # print(self)
                return
        self.name = "error"
        self.positions = ["unknown"]
        raise PositionNotFoundError(f"Spread with such id not found {self.id}")

    def set_card(self, position, card):
        for position_self in self.positions:
            if position_self["id"] == position["id"]:
                position_self["card"] = card
                # print(self)
                return
        raise PositionNotFoundError(f"Position with such id not found {position}")
