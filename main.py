from vypis import Vypis # importování třídy Vypis ze souboru vypis

vypis = Vypis() # vložení třídy do proměnné 

pokracovat = True # přiřazení boolenovské hodnoty k proměnné pro použitý while cyklu

# nastavení špatné odpovědi do proměnné
spatne = "Špatná odpověď, prosím znovu.\n" # vložení špatné odpovědi do proměnné pro pozdější výpis po špatném zadání uživatele
neni = "\nHledaný pojištěnec se bohužel nenachází v seznamu, prosím pokračujte libovolnou klávesou do hlavní nabídky...\n" # vložení špatné odpovědi do proměnné pro pozdější výpis, když nelze nalézt uživatele
velikost_sloupce = 15 # počet znaků (celkem) v každém sloupci při výpisu údajů uživatele

"""
- Menu je ošetřené proti vstupu jakýchkoliv jiných vstupů než integer
- Dále lze zadat pouze číslice 1 - 4  díky podmínkám if / elif 
"""

# cyklus pro užívání aplikace dokud uživatel nezadá č. 4 - konec aplikace (False hodnota u Pokračovat)
while pokracovat:
    vypis.obrazovka_hlavicka_cela() # vypsání hlavičky programu včetně výběru zadání
    spravne_zadani = False # nastavení proměné pro 
    while spravne_zadani != True: # cykl pro zadání správné odpovědi, dokud nebude zadána, bude se opakovat       
        try:    # opatření proti špatné volbě požadavku
            vyber = int(input()) # musí být v menu zadáno pouze číslo - integer            
            if vyber == 1: # podmínka - pokud zvolíme v menu č. 1
                spravne_zadani = True # již nebude splněna podmínka - provedli jsme správné zadání
                from pridat_novy import PridatUzivatele # importování třídy pro přidání nového uživatele
                pridat_uzivatele = PridatUzivatele() # náhraní třídy pro přidání uživatele do proměnné
                pridat_uzivatele.kompletni_zapis() # zavolání funkce pro zápis nového uživatele 
              
                """
                - Vstup jména a příjmení není nijak ošetřen, je možné zadat libovolný počet jakýchkoliv znaků - včetně číslic 
                - Tel. číslo je ošetřeno pro zadání (pouze) integer s libovolným počtem znaků (zahraniční pojištěnci mohou mít jiný format tel. čísla)
                - Věk je nastavený pro rozsah 0 až 110 let, jinak vypíše chybovou hlášku a vyžádá si nové zadání
                """

            elif vyber == 2: # podmínka - pokud zvolíme v menu č. 2
                pozice = -1 # nastavení proměnné, která poumůže s výpisem požadovaných indexů z listu
                vypis.obrazovka_hlavicka() # vyčištění obrazovky a vypsání hlavičky - loga
                spravne_zadani = True # již nebude splněna podmínka - provedli jsme správné zadání
                pojistenci = pridat_uzivatele.__str__() # načtení všech uložených/přidaných dat z třídy pridat_uzivatele do proměnné pojistenci
                while pozice != (len(pojistenci) - 1): # cykl, který vypíše postupně všechny pojistence pod sebe
                    print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[pozice+1]," "*(velikost_sloupce - len(pojistenci[pozice+1])),pojistenci[pozice+2]," "*(velikost_sloupce - len(pojistenci[pozice+2])),pojistenci[pozice+3]," "*(velikost_sloupce - len(str(pojistenci[pozice+3]))),pojistenci[pozice+4]))
                    # výpis dat v uspořádaném formátu, každý sloupec nastaven na 15 znaků
                    pozice += 4 # po vypsání se posuneme o 4 indexy na dalšího pojistence
                print("\nPokračujte libovolnou klávesou...\n")
                input()

                """
                - Data uživatelů se ukládají do jednoho listu za sebe, každý uživatel má 4 hodnoty, tzn. první uživatel obsadí indexy listu 0 - 3, druhý 4 - 7, ...
                - Sloupce výpisu všech uživatelů jsou zarovnány tak, aby stehné hodnoty byly seřazeny pod sebou, šířka sloupce je nastavena na 15 znaků pod proměnnou - velikost_sloupce
                """

            elif vyber == 3: # podmínka - pokud zvolíme v menu č. 3
                spravne_zadani = True # již nebude splněna podmínka - provedli jsme správné zadání
                vypis.obrazovka_hlavicka() # vyčištění obrazovky a vypsání hlavičky - loga 
                jmeno = input("Zadejte jméno pojištěného:\n") # vstup pro hledání podle jména
                prijmeni = input("\nZadejte příjmení pojištěného:\n") # vstup pro hledání podle příjmení
                vypis.obrazovka_hlavicka() # vyčištění obrazovky a vypsání hlavičky - loga 
                pojistenci = pridat_uzivatele.__str__() # načtení všech uložených/přidaných dat z třídy pridat_uzivatele do proměnné pojistenci
                if (jmeno and prijmeni) in pojistenci: # podmínka - pokud se zadané jméno a příjmení nachází v listu
                    index_jmeno = pojistenci.index(jmeno) # zjištění indexu pro zadané jméno
                    index_prijmeni = pojistenci.index(prijmeni) # zjištění indexu pro zadané příjmení
                    if (index_prijmeni - index_jmeno) == 1: # podmínka, že zadané jméno a příjmení musejí v listu být vedle sebe a tím pádem přísluší jednomu pojištěnci                        
                        print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[index_jmeno]," "*(velikost_sloupce - len(pojistenci[index_jmeno])),pojistenci[index_prijmeni]," "*(velikost_sloupce - len(pojistenci[index_prijmeni])),pojistenci[index_prijmeni+1]," "*(velikost_sloupce - len(str(pojistenci[index_prijmeni+1]))),pojistenci[index_prijmeni+2]))
                        # výpis dat v uspořádaném formátu, každý sloupec nastaven na 15 znaků
                        print("\nPokračujte libovolnou klávesou...\n")
                        input()
                    else: # pokud jméno a příjmení nejsou v listu vedle sebe, vypíše informaci, že pojistenec není v listu
                        print(neni)
                        input()
                else: # pokud nenajdeme jmeno a prijmeni v listu, vypíše informaci, že pojistenec není v listu
                    print(neni)
                    input()

                """
                - po zadání jména a přijmení si zjistíme index zadaných vstupů a ověříme, že se v listu nachází vedle sebe
                - následuje opět zarovnaný výpis pojištěnce, případně hláška, že se uživatel nenachází v listu
                """

            elif vyber == 4: # podmínka - pokud zvolíme v menu č. 4
                spravne_zadani = True # již nebude splněna podmínka - provedli jsme správné zadání        
                pokracovat = False
                pass

                """
                - zadání č. 4 zruší počáteční pomínku cyklu while, který se ukončí a tím aplikace skončí 
                """

            else:
                print(spatne) # výpis hlášky o špatně zadaném vstupu v úvodním menu
        except:
            print(spatne) # výpis hlášky o špatně zadaném vstupu v úvodním menu
        
vypis.obrazovka_hlavicka()
print("              KONEC - Nashledanou.\n------------------------------------------------\n")

"""
na Závěr se vyčistí obrazovka, nahraje hlavička aplikace a vypíše hláška o ukončení aplikace
"""


