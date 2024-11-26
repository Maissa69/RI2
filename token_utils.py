import re
import os
import glob

def Tokeniser(lst):
    # Tokeniser par rapport aux blancs et aux caractères spéciaux
    return [re.findall(r'[a-zA-Z0-9]+', l) for l in lst]

def get_requet(path='requet.txt'):
    # Lire le contenu du fichier de requête
    data = []
    filename = glob.glob(path)
    for file in filename:
        with open(file, 'r') as f:
            data.extend(line.lower() for line in f.read().splitlines())
    return data

def get_doc(repertoire="./Doc"):
    # Lire tous les documents dans le répertoire
    try:
        if not os.path.exists(repertoire):
            raise FileNotFoundError(f"Le répertoire {repertoire} n'existe pas.")
        fichiers = os.listdir(repertoire)
        data = []
        if not fichiers:
            print(f"Aucun fichier trouvé dans le répertoire {repertoire}.")
        else:
            for nom_fichier in fichiers:
                if nom_fichier.endswith(".txt"):
                    chemin_fichier = os.path.join(repertoire, nom_fichier)
                    try:
                        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
                            data.extend(line.lower() for line in fichier.read().splitlines())
                    except Exception as e:
                        print(f"Erreur lors de la lecture du fichier {nom_fichier} : {e}")
        return data
    except Exception as e:
        print(f"Erreur : {e}")
        return []
