from client import Client
from livre import Livre
from bibliotheque import Bibliotheque
from auteur import Auteur

client1 = Client('John', 'Doe')
client2 = Client('Mika', 'Doe')

auteur1 = Auteur('Victor', 'Hugo')
auteur2 = Auteur('Emile', 'zola')

auteur1.ecrire_un_livre('Les misérables 1')
auteur1.ecrire_un_livre('Les misérables 2')
auteur1.ecrire_un_livre('Les misérables 3')
auteur2.ecrire_un_livre('Les misérables 4')
auteur2.ecrire_un_livre('Les misérables 5')
livre1,livre2,livre3 = auteur1.lister_oeuvre()
livre4, livre5 = auteur2.lister_oeuvre()
catalogue1 = {
    livre1: 3,
    livre2: 4,
    livre3: 1
}

bibliotheque = Bibliotheque('Ma bibliotheque', catalogue1)
bibliotheque.inventaire()
bibliotheque.acheter_livre(auteur1, 'Les misérables 1', 6)
bibliotheque.acheter_livre(auteur2, 'Les misérables 4', 2)
print()
bibliotheque.inventaire()
bibliotheque.louer(client1, 'Les misérables 1')
bibliotheque.louer(client1, 'Les misérables 2')
print()
client1.inventaire()
print()
bibliotheque.inventaire()
print()
bibliotheque.rendre_livres(client1)
client1.inventaire()
print()
bibliotheque.inventaire()
