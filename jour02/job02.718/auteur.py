from personne import Personne
from livre import Livre

class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.__oeuvre = []

    def lister_oeuvre(self):
        return self.__oeuvre
    
    def ecrire_un_livre(self, titre):
        livre = Livre(titre, self)
        self.__oeuvre.append(livre)