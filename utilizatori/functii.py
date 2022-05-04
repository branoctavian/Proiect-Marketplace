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
from pprint import pprint

from pytz import country_timezones, timezone


def genereaza_id_utilizator(nume, email):
    hash_object = hashlib.md5(bytes(nume + email, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_utilizator():
    while True:
        nume = str(input("Introduceti numele dvs.: "))
        email = str(input("Introduceti adresa dvs. de e-mail: "))
        id_produs = str(genereaza_id_utilizator(nume, email))
        data_inregistrare = str(datetime.datetime.now())
        if len(nume) in range(0, 51):
            with open("baza_de_date/marketplace.json", "r") as j:
                d = json.load(j)
                d["utilizatori"][id_produs] = {
                    "nume": nume,
                    "email": email,
                    "data inregistrare": data_inregistrare
                }
            with open("baza_de_date/marketplace.json", "w") as j:
                j.write(json.dumps(d, indent=4))
            alt_utilizator = str(input("Doriti sa mai adaugati un alt utilizator DA/NU: "))
            if alt_utilizator == "NU":
                break
        else:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere!\n"
                f"{nume}")
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
    pass


def listeaza_toti_utilizatorii():
    with open("baza_de_date/marketplace.json", "r") as f:
        d = json.load(f)
        print(json.dumps(d["utilizatori"], indent=4))
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    """
    pass

def sterge_un_utilizator():
    while True:
        utilizator_de_sters = str(input("Introduceti utilizatorul pe care doriti sa il stergeti din lista: "))
        with open("baza_de_date/marketplace.json", "r") as j:
            d = json.load(j)
            flag = False
            for i in d["utilizatori"]:
                if d["utilizatori"][i]["nume"] == utilizator_de_sters:
                    flag = True
                    del d["utilizatori"][i]
                    break
            if not flag:
                print(f"Utilizator inexistent!")
        with open("baza_de_date/marketplace.json", "w") as j:
            j.write(json.dumps(d, indent=4))
        alt_utilizator = str(input("Doriti sa mai stergeti un alt utilizator?DA/NU: "))
        if alt_utilizator == "NU":
            break
    pass