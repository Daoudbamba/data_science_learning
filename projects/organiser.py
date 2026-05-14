from pathlib import Path
import shutil

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

    if not dossier.exists():
        print("Le dossier n'existe pas.")
        return

    for element in dossier.iterdir():

        # Ignorer les dossiers créés par le script
        if element.is_dir() and element.name in CATEGORIES.values():
            continue

        if element.is_dir():
            continue

        extension = element.suffix
        categorie = obtenir_categorie(extension)

        dossier_cible = dossier / categorie
        dossier_cible.mkdir(exist_ok=True)

        destination = dossier_cible / element.name

        try:
            shutil.move(str(element), str(destination))
            print(f"[OK] {element.name} déplacé vers {categorie}/")
        except Exception as e:
            print(f"[ERREUR] Impossible de déplacer {element.name} : {e}")

    print("\nOrganisation terminée.")

if __name__ == "__main__":
    chemin = input("Entrez le chemin du dossier à organiser : ")
    organiser_dossier(chemin)
cd 