class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.auteur = auteur

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    def print(self):
        print(self.titre)