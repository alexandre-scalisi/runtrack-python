class Personne:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom
    @nom.setter
    def nom (self, nom):
        self.__nom = nom
    @prenom.setter
    def prenom (self, prenom):
        self.__prenom = prenom

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}")