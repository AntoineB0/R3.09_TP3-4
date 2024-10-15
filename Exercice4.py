import Exercice2 as E2
import Exercice3 as E3

def BruteForce(MdpMaitre:str , Tag:str , taille:int)->str:
    """
        Trouve le mot de passe maître en utilisant la force brute.
        Args:
            MdpMaitre (str): Le mot de passe maître.
            Tag (str): Le tag.
            taille (int): La taille du mot de passe.
        Returns:
            str: Le mot de passe trouvé.
    """
    for i in range(33, 127):
        for j in range(33, 127):
            for k in range(33, 127):
                for l in range(33, 127):
                    for m in range(33, 127):
                        for n in range(33, 127):
                            for o in range(33, 127):
                                for p in range(33, 127):
                                    for q in range(33, 127):
                                        for r in range(33, 127):
                                            mdp = chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n)+chr(o)+chr(p)+chr(q)+chr(r)
                                            if E2.H(mdp, Tag, taille) == MdpMaitre:
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