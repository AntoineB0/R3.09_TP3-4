import Exercice2 as E2
import Exercice3 as E3

import itertools

def BruteForce(MdpMaitre: str, Tag: str, taille: int) -> str:
    """
    Trouve le mot de passe maître en utilisant la force brute.
    
    Args:
        MdpMaitre (str): Le mot de passe maître.
        Tag (str): Le tag.
        taille (int): La taille du mot de passe.
        
    Returns:
        str: Le mot de passe trouvé.
    """
    # Définit les caractères possibles (ASCII entre 33 et 126)
    caracteres = [chr(i) for i in range(33, 127)]
    
    # Génère toutes les combinaisons possibles pour un mot de passe de longueur "taille"
    for combinaison in itertools.product(caracteres, repeat=taille):
        mdp = ''.join(combinaison)
        
        # Vérifie si le mot de passe généré correspond
        if E2.H(mdp, Tag, taille) == MdpMaitre:
            return mdp
 
    return None


def BruteForceMultiTag(MdpMaitre1: str, MdpMaitre2: str,MdpMaitre3: str,Tag1: str , Tag2:str, Tag3:str, taille: int) -> str:
    """
    Trouve le mot de passe maître en utilisant la force brute avec plusieurs tags.
    
    Args:
        MdpMaitre1 (str): Le premier mot de passe maître.
        MdpMaitre2 (str): Le deuxième mot de passe maître.
        MdpMaitre3 (str): Le troisième mot de passe maître.
        Tag1 (str): Le premier tag.
        Tag2 (str): Le deuxième tag.
        Tag3 (str): Le troisième tag.
        taille (int): La taille du mot de passe.
        
    Returns:
        str: Le mot de passe trouvé.
    """
    # Définit les caractères possibles (ASCII entre 33 et 126)
    caracteres = [chr(i) for i in range(33, 127)]
    
    # Génère toutes les combinaisons possibles pour un mot de passe de longueur "taille"
    for combinaison in itertools.product(caracteres, repeat=10):
        mdp = ''.join(combinaison)
        
        # Vérifie si le mot de passe généré correspond aux trois tags ce qui permet de trouver la clé exacte
        if E2.H(mdp,Tag1 , taille) == MdpMaitre1 and E2.H(mdp,Tag2 , taille) == MdpMaitre2 and E2.H(mdp,Tag3 , taille) == MdpMaitre3:
            return mdp

    
    return None

def Exercice4():
    """
    Fonction principale de l'exercice 4.
    """
    # Lire le mot de passe maître
    mdp = E3.Lire_MDP()
    
    # Demander les tags et la taille
    tag1 = input("Saisir le premier tag : ")
    tag2 = input("Saisir le deuxième tag : ")
    tag3 = input("Saisir le troisième tag : ")
    taille = int(input("Saisir la taille : "))
    mdp1 = E2.H(mdp, tag1, taille)
    mdp2 = E2.H(mdp, tag2, taille)
    mdp3 = E2.H(mdp, tag3, taille)
    
    # Appeler la fonction BruteForceMultiTag
    print("Collision Trouvée !! :", BruteForceMultiTag(mdp1, mdp2, mdp3, tag1, tag2, tag3, taille))

if __name__ == "__main__":
    Exercice4()