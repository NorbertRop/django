import random

class Kosci:
    gracze = {'jeden': None, 'dwa': None} 
    gracz = 'jeden'
    kosci = {1: None, 2: None, 3: None, 4: None, 5: None}
    kolejka = 1
    sumaPunktow = None 

    def __init__(self):
        self.reset()


    def reset(self):
        self.gracze['jeden'] = None
        self.gracze['dwa'] = None
        self.gracz = 'jeden'
        self.kosci = {1: None, 2: None, 3: None, 4: None, 5: None}
        self.kolejka = 1
        self.sumaPunktow = {1: {'jeden': None, 'dwa': None}, 2: {'jeden': None, 'dwa': None}, 3: {'jeden': None, 'dwa': None}, 4: {'jeden': None, 'dwa': None},
                            5: {'jeden': None, 'dwa': None}, 6: {'jeden': None, 'dwa': None}, 7: {'jeden': None, 'dwa': None}, 8: {'jeden': None, 'dwa': None},
                            9: {'jeden': None, 'dwa': None}, 10: {'jeden': None, 'dwa': None}, 11: {'jeden': None, 'dwa': None}, 12: {'jeden': None, 'dwa': None},
                            13: {'jeden': None, 'dwa': None}} 

    def graczDolaczyl(self, consumer):
        if self.gracze['jeden'] is None:
            self.gracze['jeden'] = consumer
            consumer.accept()
            consumer.send_json({'gracz': 'jeden'})
        elif self.gracze['dwa'] is None:
            self.gracze['dwa'] = consumer
            consumer.accept()
            consumer.send_json({'gracz': 'dwa'})
        
        if self.obajGraczePolaczeni():
            self.wyslijDoGraczy({'kolej': self.gracz})
            # self.wyslijDoGraczy({''})


    def graczRozlaczyl(self, consumer):
        if self.gracze['jeden'] == consumer:
            self.gracze['jeden'] = None
        
        if self.gracze['dwa'] == consumer:
            self.gracze['dwa'] = None


    def obajGraczePolaczeni(self):
        return self.gracze['jeden'] is not None and self.gracze['dwa'] is not None

    def wyslijDoGraczy(self, command, message):
        self.gracze['jeden'].send_json({command: message})
        self.gracze['dwa'].send_json({command: message})

    def rzutKoscmi(self):
        for i in self.kosci:
            self.kosci[i] = random.randint(1,6)
            self.sumaPunktow[self.gracz] += self.kosci[i]


    def kolejnaKolejka(self):
        self.kolejka += 1


    def ktoWygral(self):
        if self.sumaPunktow['jeden'] > self.sumaPunktow['dwa']:
            return 'Gracz jeden'
        elif self.sumaPunktow['jeden'] < self.sumaPunktow['dwa']:
            return 'Gracz dwa'
        else:
            return 'Remis'

    