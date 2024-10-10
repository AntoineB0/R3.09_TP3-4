import hashlib

def H(mdpmaitre:str , tag:str , taille:int) -> str:
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
            somme += ord(tab[i][j])**taille*decoupe
        #traduction en caractère normaux commme spéciaux
        resultat += chr(somme%94 + 33)
    print(resultat)




if __name__ == "__main__":
    print("-----------------")
    H("lemotdepasse","Unilim",64)
    H("lemotdepasse","FaceBook",64)
    H("lemotdepasse","Youtube",64)
    print("-----------------")