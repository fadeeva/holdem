import random

class CardDeck:
    cards = ['\u26602', '\u26603', '\u26604', '\u26605', '\u26606', '\u26607', '\u26608', '\u26609', '\u266010', '\u2660J', '\u2660Q', '\u2660K', '\u2660A',
             '\u26652', '\u26653', '\u26654', '\u26655', '\u26656', '\u26657', '\u26658', '\u26659', '\u266510', '\u2665J', '\u2665Q', '\u2665K', '\u2665A',
             '\u26662', '\u26663', '\u26664', '\u26665', '\u26666', '\u26667', '\u26668', '\u26669', '\u266610', '\u2666J', '\u2666Q', '\u2666K', '\u2666A',
             '\u26662', '\u26663', '\u26664', '\u26665', '\u26666', '\u26667', '\u26668', '\u26669', '\u266610', '\u2666J', '\u2666Q', '\u2666K', '\u2666A']

    deck = []
    out_cards = []

    def get_new_deck(self):
        self.deck = list(self.cards)

    def get_card(self):
        return self.cards[random.randint(0, len(self.cards))]

    def shuffle_deck(self):
        self.get_new_deck()
        random.shuffle(self.deck)



deck = CardDeck()
deck.shuffle_deck()

print(deck.deck)
print(deck.cards)