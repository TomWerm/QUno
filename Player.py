class Player (object) :
    def __init__(self, endconfig, name, cards) :
        self.endconfig = endconfig
        self.name = name
        self.cards = cards          
    def getInfo(self) :
        return "Name:" + self.name + ", endconfiguration:" + self.endconfig
    def getCard(self, index) :
        return cards[index]
    
