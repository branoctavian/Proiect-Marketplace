"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json
import datetime


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    with open("baza_de_date/marketplace.json", "r") as j:
        d = json.load(j)
    while True:
        data_inregistrare = str(datetime.datetime.now())
        id_comanda = {
            "id_comanda": " ",
            "data_inregristrare": data_inregistrare,
            "detalii_comanda": []
        }
        while True:
            numele_produsului = input("Introduceti produsele din comanda. Pentru a termina, introduceti 'STOP': ")
            if numele_produsului == "STOP":
                break
            for i in d["produse"]:
                if d["produse"][i]["nume produs"] == numele_produsului:
                    idProdus = i
                    break
            else:
                print(f"Produsul {numele_produsului} nu exista")
                continue
            cantitatea = int(input("Introduceti cantitatea produsului selectat: "))
            id_comanda["detalii_comanda"].append({idProdus: cantitatea})
            Idcomanda = str(genereaza_id_comanda(json.dumps(id_comanda)))
            id_comanda["id_comanda"] = Idcomanda
            d["comenzi"][Idcomanda] = id_comanda
            alt_produs = input("Doriti sa mai adaugati un produs DA/STOP: ")
            if alt_produs == "STOP":
                break
        break
    with open("baza_de_date/marketplace.json", "w") as j:
        j.write(json.dumps(d, indent=4))
    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """
    pass


def modifica_comanda():
    with open("baza_de_date/marketplace.json", "r") as j:
        d = json.load(j)
        while True:
            alege_actiunea = input("Alegeti una din actiuni: \n"
                             "( 'a' - adaugare produs; \n"
                             " 'm' - modificare cantitate; \n" 
                             " 's'- sterge produs, \n"
                                   " 'e'-exit:")
            if alege_actiunea in ('a', 'm', 's', 'e'):
                if alege_actiunea == 'e':
                    break
                chei_comenzi = str(d["comenzi"].keys())
                print(f"Lista comenzilor este: {chei_comenzi}")
                comanda_de_modificat = str(input("Introduceti identificatorul comenzii de modificat: "))
                if alege_actiunea == 'a':
                    while True:
                        produs_de_adaugat = input("Introduceti produsul de adaugat: ")
                        for i in d["produse"]:
                            if d["produse"][i]["nume produs"] == produs_de_adaugat:
                                idProdus = i
                                cantitatea = int(input("Introduceti cantitatea pentru produsul selectat: "))
                                d["comenzi"][comanda_de_modificat]["detalii_comanda"].append({idProdus: cantitatea})
                                break
                        else:
                            print(f"Produsul {produs_de_adaugat} nu exista!")
                            continue
                        alt_produs = input("Doriti sa introduceti un alt produs? (DA/NU): ")
                        if alt_produs == "NU":
                            break
                if alege_actiunea == 'm':
                    while True:
                        produse_din_comanda = d["comenzi"][comanda_de_modificat]["detalii_comanda"]
                        print(f"Lista produselor din comanda: {produse_din_comanda}")
                        produs_schimba_cantitatea = str(input("Introduceti identificatorul produsului a carui cantitate o modificati: "))
                        noua_cantitate = int(input("Introduceti noua cantitatea a produsului selectat: "))
                        for i in range(len(produse_din_comanda)):
                            if produs_schimba_cantitatea in produse_din_comanda[i]:
                                produse_din_comanda[i].update({produs_schimba_cantitatea: noua_cantitate})
                                break
                        else:
                            print(f"Produsul {produs_schimba_cantitatea} nu se afla in comanda selectata!")
                            continue
                        alta_modificare = input("Doriti sa efectuati alt modificare? (DA/NU):")
                        if alta_modificare == "NU":
                            break
                if alege_actiunea == 's':
                    while True:
                        produse_din_comanda = d["comenzi"][comanda_de_modificat]["detalii_comanda"]
                        print(f"Lista produselor din comanda: {produse_din_comanda}")
                        sterge_produs = str(input("Introduceti identificatorul produsului de sters: "))
                        for i in range(len(produse_din_comanda)):
                            if sterge_produs in produse_din_comanda[i]:
                                del produse_din_comanda[i]
                                break
                        else:
                            print(f"Produsul {produs_schimba_cantitatea} nu se afla in comanda selectata!")
                            continue
                        alt_produs_de_sters = str(input("Doriti sa stergeti alt produs din comanda selectata?(DA/NU): "))
                        if alt_produs_de_sters == "NU":
                            break
            else:
                print("Operatiune invalida!")
            alta_actiune = input("Doriti sa executati alta actiune? (DA/NU): ")
            if alta_actiune == "NU":
                break
    with open("baza_de_date/marketplace.json", "w") as j:
        j.write(json.dumps(d, indent=4))

    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """

    pass


def listeaza_toate_comenzile():
    with open("baza_de_date/marketplace.json", "r") as f:
        d = json.load(f)
        print(json.dumps(d["comenzi"], indent=4))
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    pass




def sterge_o_comanda():
    while True:
        with open("baza_de_date/marketplace.json", "r") as j:
            d = json.load(j)
            chei_comenzi = str(d["comenzi"].keys())
            print(f"Lista comenzilor este: {chei_comenzi}")
            comanda_de_sters = input("Introduceti identificatorul comenzii de sters: ")
            if comanda_de_sters in d["comenzi"]:
                del d["comenzi"][comanda_de_sters]
            else:
                print("Produs inexistent!")
        with open("baza_de_date/marketplace.json", "w") as j:
            j.write(json.dumps(d, indent=4))
        alta_comanda = input("Doriti sa stergeti o alta comanda? (DA/NU): ")
        if alta_comanda == "NU":
            break
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """

    pass
