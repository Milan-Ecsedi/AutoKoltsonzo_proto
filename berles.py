from auto import Auto
from datetime import date

class Berles:
    def __init__(self, auto: Auto, datum: date):
        self.auto = auto
        self.datum = datum

    def ar(self):
        return self.auto.berleti_dij

    def __str__(self):
        return f"{self.auto} - Bérlés dátuma: {self.datum}"