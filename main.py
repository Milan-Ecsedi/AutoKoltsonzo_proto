from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
import datetime

autoKolcsonzo1 = Autokolcsonzo("Pozsgás és társa kölcsönző DABAS")

auto1 = Szemelyauto("123-DTR", "Volvo", 20000, 5)
auto2 = Teherauto("518-KGB", "Renault", 20000, 100)
auto3 = Szemelyauto("411-DDR", "Ford", 40000, 4)
auto4 = Teherauto("114-UDP", "Volvo", 35000, 150)
auto5 = Szemelyauto("837-DLX", "Shevrolette", 10000, 2)
auto6 = Teherauto("912-VIE", "Mazda", 40000, 70)
auto7 = Szemelyauto("800-LKS", "Kia", 5000, 2)
autoKolcsonzo1.auto_hozzaad(auto1)
autoKolcsonzo1.auto_hozzaad(auto2)
autoKolcsonzo1.auto_hozzaad(auto3)

autoKolcsonzo1.berel_auto(auto1, datetime.date(2025, 12,11))
autoKolcsonzo1.berel_auto(auto2, datetime.date(2025, 11, 14))
autoKolcsonzo1.berel_auto(auto3, datetime.date(2025, 9, 10))
autoKolcsonzo1.berel_auto(auto3, datetime.date(2026, 1, 9))

while True:

    parancs = input("Adja meg hogy mit szeretne csinálni:\n /lista : ki listázza az összes autót  \n /listab : kiadja a bérléseket\n /berles : egy autó lefoglalása egy adott napra \n /lemond : egy autó bérlés lemondása az adott napon \n /kilepes : ki lép a programból\n")
    
    if parancs == "/lista" :
        autoKolcsonzo1.get_auto()

    elif parancs =="/listab":
        print(autoKolcsonzo1.get_berlesek())

    elif parancs == "/berles":
        i = int(input("Az elérhető bérelhető járművekből adja meg a sorszámát amit ki szeretne választani: "))
        kivalasztottAuto= autoKolcsonzo1.get_auto_as_object()[i-1]
        print("A kiválasztott gépjármű: "+ str(kivalasztottAuto))
        datum_str= input("Adja meg a bérlés dátumát (pl: 2025-12-07 ): ")
        datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
        #print(type(datum))
        autoKolcsonzo1.berel_auto(kivalasztottAuto, datum)

    elif parancs == "/lemond":
        i = int(input("Az elérhető bérelhető járművekből adja meg a sorszámát amit le szeretne mondani: "))
        kivalasztottAuto= autoKolcsonzo1.get_auto_as_object()[i-1]
        print("A kiválasztott gépjármű: "+ str(kivalasztottAuto))
        datum_str= input("Adja meg azt a napot mikor lefoglalta (pl: 2025-12-07 ) : ")
        datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
        #print(type(datum))
        autoKolcsonzo1.lemond_berlest(kivalasztottAuto, datum)

    elif parancs == "/kilepes":
        break
        





