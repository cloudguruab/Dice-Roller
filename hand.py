from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError('You must provide a die class')
        super().__init__()

        for _ in range(size):
            self.append(die_class()) 
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self: 
            if int(die) == value:
                dice.append(die)
        return dice


class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    @property  
    def ones(self):
        return self._by_value(1)
    
    @property
    def twos(self):
        return self._by_value(2)

    @property    
    def threes(self):
        return self._by_value(3)
    
    @property
    def fours(self):
        return self._by_value(4)

    @property   
    def fives(self):
        return self._by_value(5)

    @property  
    def six(self):
        return self._by_value(6)

    @property  
    def _sets(self):
        return {
            1: len(self._by_value(1)),
            2: len(self._by_value(2)),
            3: len(self._by_value(3)),
            4: len(self._by_value(4)),
            5: len(self._by_value(5)),
            6: len(self._by_value(6)),
        }
