class Vypis:

    # hlavička - název aplikace
    def vypis_menu(self):
        return "------------------------------------------------\n              Evidence pojištěných\n------------------------------------------------\n"

    # text pro menu
    def vyber_akci(self):
        return "Vyberte si akci:\n1  -  Přidat nového pojistného\n2  -  Vypsat všechny pojištěné\n3  -  Vyhledat pojištěného\n4  -  Konec\n"

    # funkce pro vyčištění obrazovky
    def _vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    # vyčištění obrazovky a nahrání hlavičky včetně menu
    def obrazovka_hlavicka_cela(self):
        vypis._vycisti_obrazovku() 
        print(vypis.vypis_menu())
        print(vypis.vyber_akci()) 

    # vyčištění obrazovky a nahrání hlavičky bez menu
    def obrazovka_hlavicka(self):
        vypis._vycisti_obrazovku() 
        print(vypis.vypis_menu())

# vložení třídy výpis do proměnné
vypis = Vypis()