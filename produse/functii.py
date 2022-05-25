"""
Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})
"""

import hashlib
import json
import datetime


def genereaza_id_produs(nume_produs, cantitate, pret):
    hash_object = hashlib.md5(bytes(nume_produs + str(cantitate) + str(pret), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    with open("baza_de_date/marketplace.json", "r") as j:
        d = json.load(j)
        while True:
            nume_produs = input("Introduceti numele produsului de adaugat: ")
            if len(nume_produs) in range(0, 51):
                pret = float(input("Introduceti pretul produsului de adaugat: "))
                cantitate = int(input("Introduceti cantitatea produsului de adaugat: "))
                id_produs = str(genereaza_id_produs(nume_produs, cantitate, pret))
                data_inregistrare = str(datetime.datetime.now())
                d["produse"][id_produs] = {
                    "nume produs": nume_produs,
                    "pret": pret,
                    "cantitate": cantitate,
                    "data inregistrare": data_inregistrare
                }
            else:
                print(f"Numele {nume_produs} nu este valid - Lungimea numelui trebuie sa aiba intre 1 si 50 de caractere!")
            alt_produs = input("Doriti sa adaugati alt produs? (DA/NU): ")
            if alt_produs == "NU":
                break
    with open("baza_de_date/marketplace.json", "w") as j:
        j.write(json.dumps(d, indent=4))
    '''
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    '''


def listeaza_toate_produsele():
    with open("baza_de_date/marketplace.json", "r") as f:
        d = json.load(f)
        print(json.dumps(d["produse"], indent=4))
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """


def modifica_date_produs():
    with open("baza_de_date/marketplace.json", "r") as j:
        d = json.load(j)
        while True:
            data_modificare = str(datetime.datetime.now())
            alege_actiunea = input("Alegeti una din actiuni: \n"
                             " 'n' - modificare nume produs; \n"
                             " 'p' - modificare pret; \n" 
                             " 'c' - modificare cantitate; \n"
                                   " 'e'-exit:")
            if alege_actiunea in ('n', 'p', 'c', 'e'):
                if alege_actiunea == 'e':
                    break
                elif alege_actiunea == 'n':
                    while True:
                        print(json.dumps(d["produse"], indent=4))
                        produs_de_modificat = input("Introduceti numele produsului de modificat: ")
                        for i in d["produse"]:
                            if d["produse"][i]["nume produs"] == produs_de_modificat:
                                modificare_nume_produs = input("Introduceti modificarea numelui produsului ales: ")
                                d["produse"][i].update({"nume produs": modificare_nume_produs})
                                d["produse"][i].update({"data ultimei modificari": data_modificare})
                                break
                        else:
                            print(f"Produsul {produs_de_modificat} nu exista!")
                        alt_produs = input("Doriti sa modificati numele altui produs? (DA/NU): ")
                        if alt_produs == "NU":
                            break
                elif alege_actiunea == 'p':
                    while True:
                        print(json.dumps(d["produse"], indent=4))
                        produs_de_modificat = input("Introduceti produsul de modificat: ")
                        for i in d["produse"]:
                            if d["produse"][i]["nume produs"] == produs_de_modificat:
                                modificare_pret_produs = float(input("Introduceti noul pret al produsului ales: "))
                                d["produse"][i].update({"pret": modificare_pret_produs})
                                d["produse"][i].update({"data ultimei modificari": data_modificare})
                                break
                        else:
                            print(f"Produsul {produs_de_modificat} nu exista!")
                        alt_produs = input("Doriti sa modificati pretul altui produs? (DA/NU): ")
                        if alt_produs == "NU":
                            break
                elif alege_actiunea == 'c':
                    while True:
                        print(json.dumps(d["produse"], indent=4))
                        produs_de_modificat = input("Introduceti produsul de modificat: ")
                        for i in d["produse"]:
                            if d["produse"][i]["nume produs"] == produs_de_modificat:
                                modificare_cantitate_produs = int(input("Introduceti noua cantitate a produsului ales: "))
                                d["produse"][i].update({"cantitate": modificare_cantitate_produs})
                                d["produse"][i].update({"data ultimei modificari": data_modificare})
                                break
                        else:
                            print(f"Produsul {produs_de_modificat} nu exista!")
                        alt_produs = input("Doriti sa modificati cantitatea altui produs? (DA/NU): ")
                        if alt_produs == "NU":
                            break
            else:
                print(f"Actiunea {alege_actiunea} nu exista! Va rugam introduceti o operatiune valida!")
                continue
            alta_actiune = input("Doriti sa modificati alt produs? (DA/NU): ")
            if alta_actiune == "NU":
                break
    with open("baza_de_date/marketplace.json", "w") as j:
        j.write(json.dumps(d, indent=4))


def sterge_produs():
    while True:
        produs_de_sters = input("Introduceti produsul pe care doriti sa il stergeti din lista: ")
        with open("baza_de_date/marketplace.json", "r") as j:
            d = json.load(j)
            for i in d["produse"]:
                if d["produse"][i]["nume produs"] == produs_de_sters:
                    del d["produse"][i]
                    break
            else:
                print(f"Produsul {produs_de_sters} nu exista!")
        with open("baza_de_date/marketplace.json", "w") as j:
            j.write(json.dumps(d, indent=4))
        alt_produs = input("Doriti sa stergeti alt produs? (DA/NU): ")
        if alt_produs == "NU":
            break