from auto import Auto
from datetime import date
from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaad(self, auto: Auto):
        self.autok.append(auto)

    #Segéd methodus-om a berel_auto()-nak
    def auto_elerheto(self, auto: Auto, datum: date):
        for berles in self.berlesek:
            if berles.auto == auto and berles.datum == datum:
                return False
        return True

    def berel_auto(self, auto: Auto, datum: date):
         
        if datum < date.today():
            raise ValueError("Nem lehet múltbeli dátumra bérlést rögzíteni.")
        if not self.auto_elerheto(auto, datum):
            raise ValueError("Ez az autó ezen a napon már foglalt.")
        berles = Berles(auto, datum)
        self.berlesek.append(berles)
        print("A bérlés sikeres volt. Átveheti a gépjárművét "+ str(datum) +" napon \n")
        return berles.ar()

    def lemond_berlest(self, auto: Auto, datum: date):
        for berles in self.berlesek:
            if berles.auto == auto and berles.datum == datum:
                self.berlesek.remove(berles)
                return True
        raise ValueError("A megadott bérlés nem található.")
        


    def get_berlesek(self):
        for berles in self.berlesek:
            print(str(berles))

        #return [str(berles) for berles in self.berlesek]
    
    def get_auto(self):
        for auto in self.autok:
            print(str(auto))
    
    def get_auto_as_object(self):
        return [auto for auto in self.autok]

        
