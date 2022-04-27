class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.__nom = nom
        self.__catalogue = catalogue

    def acheter_livre(self, auteur, titre, quantite):
        for livre in auteur.lister_oeuvre():
            if livre.titre == titre and self.__catalogue.get(livre):
                self.__catalogue[livre] += quantite
                break
            elif  livre.titre == titre:
                self.__catalogue[livre] = quantite
                break

    def inventaire(self):
        print('\n'.join([f'{livre.titre}: {quantite}' for livre, quantite in self.__catalogue.items()]))

    def louer(self, client, titre):
        for livre, quantite in self.__catalogue.items():
            if livre.titre == titre and quantite > 0:
                if client.collection.get(livre):
                    client.collection[livre] += 1
                else:
                    client.collection[livre] = 1
                self.__catalogue[livre] -= 1
                break
    
    def rendre_livres(self, client):
        for livre, quantite in client.collection.items():
            if quantite > 0:
                self.__catalogue[livre] += quantite
                client.collection[livre] = 0