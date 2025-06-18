from auto import Auto

class Teherauto(Auto):
    
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó: {self.tipus} ({self.rendszam}), Teherbírás: {self.teherbiras} kg, Díj: {self.berleti_dij} Ft"
