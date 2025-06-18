from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ulesek_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def __str__(self):
        return f"Személyautó: {self.tipus} ({self.rendszam}), {self.ulesek_szama} ülés, Díj: {self.berleti_dij} Ft"
