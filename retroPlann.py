import requests
from datetime import datetime
from bs4 import BeautifulSoup
import sys

# Regroupe le nom de tous les mois
Mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin',
        'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

# Récupère la page de discographie de rap genius pour l'année en cours
url = 'https://genius.com/Genius-france-discographie-2019-annotated'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
liens = soup.findAll('a')

# Récupère tous les albums
albums = []
for lien in liens:
    sortie = lien.get_text()
    if (sortie[0] == '*' or sortie[0] == '-') and len(sortie) > 5:
        try:
            int(sortie[5])
            int(sortie[6])
            jour = sortie[2:4]
            mois = sortie[5:7]
            reste = sortie[10:]

            artiste = reste.split(" - ")[0]
            if len(reste.split(" - ")) > 1:
                album = reste.split(" - ")[1]

            albums.append((jour, int(mois), artiste, album))
        except ValueError:
            0


# Affiche les prochaines sorties
def prochainesSorties(today, nbre, albums, bestBoo=False, best=[]):
    print("\nProchaines sorties:")
    for song in albums:
        try:
            int(song[0])
            date = datetime(2019, song[1], int(song[0]))
            if (bestBoo and song[2] in best) or not(bestBoo):
                if nbre != 0:
                    if (date - today).days == -1:
                        print("Sortie ajd: " + song[2] + " - " + song[3])
                        nbre -= 1
                    elif (date - today).days >= 0:
                        print("Dans " + str((date - today).days + 1) +
                              " jours: " + song[2] + " - " + song[3])
                        nbre -= 1
        except:
            if (bestBoo and song[2] in best) or not(bestBoo):
                if nbre != 0 and song[1] >= today.month:
                    print("Au mois de " +
                          Mois[song[1] - 1] + " : " + song[2] + " - " + song[3])
                    nbre -= 1


def main(args):
    if (len(args) == 1):
        print("Ce programme affiche les prochaines sorties d'album de rap fr, il faut indiquer d'abord le nombre d'albums à afficher puis restreindre aux best si besoin")
    elif (len(args) == 2):
        try:
            int(args[1])
            prochainesSorties(today, int(args[1]), albums)
        except ValueError:
            print("Le premier argument doit être entier !")
    else:
        try:
            int(args[1])
            prochainesSorties(today, int(args[1]), albums, True, best)
        except ValueError:
            print("Le premier argument doit être entier !")

    print("")


# Initialise les variables nécessaire pour le main
today = datetime.now()
best = ['Lomepal', 'Dinos', 'Soolking', 'Tsew The Kid', 'Alkpote', 'Caballero', 'JeanJass', 'JuL', 'Di-meh', 'Krisy', 'L\'Ordre Du Périph',
        'Népal', 'Ateyaba', 'Fixpen Sill', '2Fingz', 'Kaaris', 'ICO', 'Tengo John', 'Isha', 'Sch', 'Lefa', '47Ter', 'Kikesa', 'Vald']
main(sys.argv)
