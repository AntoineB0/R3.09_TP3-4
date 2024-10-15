#Fonction qui concatène deux chaine de caractères et qui le hash et traduit renvoyer une chaine de 8 caractères
import hashlib

def H(mdpmaitre:str , tag:str) -> str:
    """
    Génère une chaîne de caractères hachée basée sur la concaténation du mot de passe maître et d'un tag.
        mdpmaitre (str): Le mot de passe maître.
        
        tag (str): Le tag à concaténer avec le mot de passe maître.
        str: Une chaîne de caractères hachée dérivée de la concaténation du mot de passe maître et du tag.
    def H(mdpmaitre: str, tag: str) -> str:
        
    """
    
    #Hash de la concatenation de deux chaines de caractères
    chaineconat = mdpmaitre + tag
    chaine = hashlib.sha256()
    chaine.update(chaineconat.encode('utf-8'))
    
    #Découpé le hash en 8 parties de 8 caractères
    chaine = chaine.hexdigest()
    tab = [0]*8
    for i in range(8):
        tab[i] = chaine[i*8:(i+1)*8]
        
    #Traduction de chaque partie en caractère
    resultat = ""
    for i in range(8):
        #addition des valeurs de chaque bloc
        somme = 0
        for j in range(8):
            somme += ord(tab[i][j])
        #traduction en caractère normaux commme spéciaux
        resultat += chr(somme%94 + 33)
    print(resultat)
    
    
if __name__ == "__main__":
    H("lemotdepasse","Unilim")
    H("lemotdepasse","Facebook")
    H("lemotdepasse","X")
    H("lemotdepasse","Youtube")