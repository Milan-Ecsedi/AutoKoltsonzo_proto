from auto import Auto

class Teherauto(Auto):
    
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int, rakodo_ter : int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras
        self.rakodo_ter= rakodo_ter

    def __str__(self):
        return f"Teherautó: {self.tipus} ({self.rendszam}), Teherbírás: {self.teherbiras} kg, Rakodó tér magassága: {self.rakodo_ter} méter, Díj: {self.berleti_dij} Ft"
