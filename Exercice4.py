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

def BruteForceMultiTag(MdpMaitre: str, Tag1: str , Tag2:str, Tag3:str, taille: int) -> str:
    """
    Trouve le mot de passe maître en utilisant la force brute.
    
    Args:
        MdpMaitre (str): Le mot de passe maître.
        Tag (list): Liste de tag.
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
        if E2.H(mdp,Tag1 , taille) == MdpMaitre and E2.H(mdp,Tag2 , taille) == MdpMaitre and E2.H(mdp,Tag3 , taille) == MdpMaitre:
            return mdp

    
    return None

def Exercice4():
    """
        Fonction principale de l'exercice 4.
    """
    # Lire le mot de passe maître
    mdp = E3.Lire_MDP()
    
    # Demander le tag et la taille
    tag = input("Saisir le tag : ")
    taille = int(input("Saisir la taille : "))
    mdp = E2.H(mdp, "Unilim",taille )
    # Appeler la fonction BruteForce
    print("Collision Trouver !! :",BruteForce(mdp, tag, taille))


if __name__ == "__main__":
    Exercice4()