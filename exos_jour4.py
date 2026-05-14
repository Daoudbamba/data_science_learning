# Exercice 4 : Afficher les nombres de 1 à 100
# n = 100
# for i in range(1, n+1):
#     print(i)


# Exercice  : Afficher les nombres pairs de 1 à 100
# n=100
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)


# Exercice  : Afficher la somme des éléments d'une liste
# n=[11, 2, 32, 5, 6, 70]
# s=0
# for i in n:
#     s=s+i
# print(s)          

# n=[11, 2, 32, 5, 6, 70]
# max = n[0]
# for i in n:
#     max = n[0]
#     if i > max:
#         max = i
# print(max)  


from pathlib import Path
import shutil

# Association extensions -> dossiers
CATEGORIES = {
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",

    ".pdf": "pdf",

    ".txt": "textes",
    ".docx": "textes",

    ".mp3": "audio",
    ".wav": "audio",

    ".mp4": "videos",
    ".mov": "videos"
}


def obtenir_categorie(extension):
   
    return CATEGORIES.get(extension.lower(), "autres")


def organiser_dossier(chemin_dossier):
    dossier = Path(chemin_dossier)

    # Vérifie que le dossier existe
    if not dossier.exists():
        print("Le dossier n'existe pas.")
        return

    # Parcours des fichiers
    for element in dossier.iterdir():

        # Ignore les dossiers
        if element.is_dir():
            continue

        # Récupère l'extension
        extension = element.suffix

        # Trouve la catégorie
        categorie = obtenir_categorie(extension)

        # Crée le dossier cible
        dossier_cible = dossier / categorie
        dossier_cible.mkdir(exist_ok=True)

        # Nouveau chemin
        destination = dossier_cible / element.name

        # Déplace le fichier
        shutil.move(str(element), str(destination))

        print(f"[OK] {element.name} déplacé vers {categorie}/")


if __name__ == "__main__":
    chemin = input("Entrez le chemin du dossier à organiser : ")
    organiser_dossier(chemin)