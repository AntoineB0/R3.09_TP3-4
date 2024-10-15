import hashlib

def H(mdpmaitre:str , tag:str , taille:int) -> str:
    """
        Génère une chaîne de caractères basée sur le hash SHA-512 de la concaténation
        de `mdpmaitre` et `tag`, découpée en `taille` parties.
        Args:
            mdpmaitre (str): La chaîne de caractères principale.
            tag (str): La chaîne de caractères à concaténer avec `mdpmaitre`.
            taille (int): Le nombre de parties dans lesquelles découper le hash.
                          Doit être compris entre 1 et 128.
        Returns:
            str: Une chaîne de caractères résultante de la traduction des parties du hash.
                 Retourne `None` si `taille` est invalide.
        Raises:
            ValueError: Si `taille` est inférieur à 1 ou supérieur à 128.
    """
    if taille < 1 or taille > 128:
        print("Taille invalide")
        return
    #Hash de la concatenation de deux chaines de caractères
    chaineconat = mdpmaitre + tag
    chaine = hashlib.sha512()
    chaine.update(chaineconat.encode('utf-8'))
    
    #Découpé le hash en taille parties 
    chaine = chaine.hexdigest()
    tab = [0]*taille
    decoupe = len(chaine)//taille
    for i in range(taille):
        tab[i] = chaine[i*decoupe:(i+1)*decoupe]
        
    #Traduction de chaque partie en caractère
    resultat = ""
    for i in range(taille):
        #addition des valeurs de chaque bloc
        somme = 0
        for j in range(decoupe):
            somme += ord(tab[i][j])**taille+decoupe
        #traduction en caractère normaux commme spéciaux
        resultat += chr(somme%94 + 33)
    return(resultat)



"""Test
if __name__ == "__main__":
    print("-----------------")
    print(H("lemotdepasse","Unilim",64))
    print(H("lemotdepasse","FaceBook",64))
    print(H("lemotdepasse","Youtube",64))
    print("-----------------")
    print(H("lemotdepasse","Unilim",1))
    print(H("lemotdepasse","Unilim",2))
    print(H("lemotdepasse","Unilim",3))
"""
