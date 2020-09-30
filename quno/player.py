class Player (object) :
    def __init__(self, endconfig, name, cards) :
        self.endconfig = endconfig
        self.name = name
        self.cards = cards          
    def getInfo(self) :
        return "Name:" + self.name + ", endconfiguration:" + str(self.endconfig)
    def getCards(self) :
        cardsStr = ""
        for card in self.cards:
            cardsStr += card.gate.get() + "; "
        return cardsStr
    def getCard(self, index) :
        return self.cards[index]
    def addCard(self, card) :
        self.cards + card
    def removeCard(self, index) :
        self.cards.remove(self.cards[index])
    def hasCards(self):
        return len(self.cards)>0
