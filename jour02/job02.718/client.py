from personne import Personne
class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.__collection = {}  

    @property
    def collection(self):
        return self.__collection
    
    @collection.setter
    def collection(self, collection):
        self.__collection = collection

    def inventaire(self):
        print('\n'.join([f'{livre.titre}: {quantite}' for livre, quantite in self.__collection.items()]))
