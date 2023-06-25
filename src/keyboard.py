from src.item import Item


class MixinLang:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        Item.__init__(self, name, price, quantity)
        MixinLang.__init__(self)
