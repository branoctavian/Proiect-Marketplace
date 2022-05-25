"""
Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})
"""

import hashlib
import datetime
import json


def genereaza_id_utilizator(nume, email):
    hash_object = hashlib.md5(bytes(nume + email, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_utilizator():
    while True:
        nume = input("Introduceti username-ul ales de dvs.: ")
        if len(nume) in range(0, 51):
            email = input("Introduceti adresa dvs. de e-mail: ")
            id_utilizator = str(genereaza_id_utilizator(nume, email))
            data_inregistrare = str(datetime.datetime.now())
            with open("baza_de_date/marketplace.json", "r") as j:
                d = json.load(j)
                d["utilizatori"][id_utilizator] = {
                    "nume": nume,
                    "email": email,
                    "data inregistrare": data_inregistrare
                }
            with open("baza_de_date/marketplace.json", "w") as j:
                j.write(json.dumps(d, indent=4))
            alt_utilizator = input("Doriti sa adaugati alt utilizator? (DA/NU): ")
            if alt_utilizator == "NU":
                break
        else:
            print(f"Numele {nume} nu este valid - Lungimea numelui trebuie sa aiba intre 1 si 50 de caractere!")
    """
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """


def listeaza_toti_utilizatorii():
    with open("baza_de_date/marketplace.json", "r") as f:
        d = json.load(f)
        print(json.dumps(d["utilizatori"], indent=4))
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    """


def modifica_date_utilizator():
    with open("baza_de_date/marketplace.json", "r") as j:
        d = json.load(j)
        while True:
            data_modificare = str(datetime.datetime.now())
            alege_actiunea = input("Alegeti una din actiuni: \n"
                             " 'u' - modificare username; \n"
                             " 'm' - modificare e-mail; \n" 
                             " 'e' - exit:")
            if alege_actiunea in ('u', 'm', 'e'):
                if alege_actiunea == 'e':
                    break
                elif alege_actiunea == 'u':
                    while True:
                        print(json.dumps(d["utilizatori"], indent=4))
                        utilizator_de_modificat = input("Introduceti utilizatorul de modificat: ")
                        for i in d["utilizatori"]:
                            if d["utilizatori"][i]["nume"] == utilizator_de_modificat:
                                modificare_nume_utilizator = input("Introduceti modificarea usernname-ului dvs.: ")
                                d["utilizatori"][i].update({"nume": modificare_nume_utilizator})
                                d["utilizatori"][i].update({"data ultimei modificari": data_modificare})
                                break
                        else:
                            print(f"Utilizatorul {utilizator_de_modificat} nu exista!")
                        alt_utilizator = input("Sunteti multumit de modificarea efectuata? (DA/NU): ")
                        if alt_utilizator == "DA":
                            break
                elif alege_actiunea == 'm':
                    while True:
                        print(json.dumps(d["utilizatori"], indent=4))
                        utilizator_de_modificat = input("Introduceti utilizatorul de modificat: ")
                        for i in d["utilizatori"]:
                            if d["utilizatori"][i]["nume"] == utilizator_de_modificat:
                                modificare_email = input("Introduceti modificare email-ului dvs.: ")
                                d["utilizatori"][i].update({"email": modificare_email})
                                d["utilizatori"][i].update({"data ultimei modificari": data_modificare})
                                break
                        else:
                            print(f"Utilizatorul {utilizator_de_modificat} nu exista!")
                        alt_email = input("Sunteti multumit de modificarea efectuata? (DA/NU): ")
                        if alt_email == "DA":
                            break
            else:
                print(f"Actiunea {alege_actiunea} nu exista! Va rugam introduceti o operatiune valida!")
                continue
            alta_actiune = input("Doriti sa mai modificati date ale contuli dvs.? (DA/NU): ")
            if alta_actiune == "NU":
                break
    with open("baza_de_date/marketplace.json", "w") as j:
        j.write(json.dumps(d, indent=4))

def sterge_un_utilizator():
    while True:
        utilizator_de_sters = input("Introduceti utilizatorul pe care doriti sa il stergeti din lista: ")
        with open("baza_de_date/marketplace.json", "r") as j:
            d = json.load(j)
            for i in d["utilizatori"]:
                if d["utilizatori"][i]["nume"] == utilizator_de_sters:
                    del d["utilizatori"][i]
                    break
            else:
                print(f"Utilizatorul {utilizator_de_sters} nu exista!")
        with open("baza_de_date/marketplace.json", "w") as j:
            j.write(json.dumps(d, indent=4))
        alt_utilizator = input("Doriti sa stergeti alt utilizator? (DA/NU): ")
        if alt_utilizator == "NU":
            break