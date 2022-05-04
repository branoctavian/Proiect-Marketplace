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
    while True:
        Idcomanda = str(genereaza_id_comanda(json.dumps("ceva")))
        data_inregistrare = str(datetime.datetime.now())
        id_comanda = {
            "id_comanda" : Idcomanda,
            "data_inregristrare": data_inregistrare,
            "detalii_comanda": []
        }
        alt_produs = "DA"
        while alt_produs == "DA":
            idProdus = ""
            numele_produsului = str(input("Introduceti produsele din comanda. Pentru a termina, intrpduceti 'stop': "))
            with open("baza_de_date/marketplace.json", "r") as j:
                d = json.load(j)
                for i in d["produse"]:
                    if d["produse"][i]["nume produs"] == numele_produsului:
                        idProdus = i
                        break
            if idProdus == "":
                print(f"Produsul " + numele_produsului + "nu exista")
                continue
            cantitatea = int(input("Introduceti cantitatea produsului selectat: "))
            id_comanda["detalii_comanda"].append({idProdus: cantitatea})
            alt_produs = str(input("Doriti sa mai adaugati un produs DA/NU: "))

        with open("baza_de_date/marketplace.json", "r") as j:
            d = json.load(j)
            d["comenzi"][Idcomanda] = id_comanda
        with open("baza_de_date/marketplace.json", "w") as j:
            j.write(json.dumps(d, indent=4))
        if alt_produs == "NU":
            break
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
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """

    pass
