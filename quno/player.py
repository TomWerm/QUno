class Player (object) :
    def __init__(self, endconfig, name, cards) :
        self.endconfig = endconfig
        self.name = name
        self.cards = cards          
    def getInfo(self) :
        return self.name + " aiming for: " + str(self.endconfig.data)
    def getCards(self) :
        firstLine = ""
        secondLine = ""
        thirdLine = ""
        for card in self.cards:
            firstLine += "_" * (len(card.gate.get()) + 2) + " "
            secondLine += "|" + card.gate.get() + "| "
            thirdLine += "‾" * (len(card.gate.get()) + 2) + " "
        return firstLine + "\n" + secondLine + "\n" + thirdLine
    def getCard(self, index) :
        return self.cards[index]
    def addCard(self, card) :
        self.cards + card
    def removeCard(self, index) :
        self.cards.remove(self.cards[index])
    def hasCards(self):
        return len(self.cards)>0
