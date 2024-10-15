import Exercice2


#Faire un fichier avec le MDP maitre 

def Exercice3():
    print("-----------------")
    #Verifier si le fichier existe
    try:
        with open('mpwd.txt', 'r') as fichier:
            pass
    except FileNotFoundError:
        with open('mpwd.txt', 'w') as fichier:
            pass
    
    
    # Ouvrir et lire le fichier
    with open('mpwd.txt', 'r') as fichier:
        contenu = fichier.read()

        if not contenu:  # Si le contenu est vide
            Changer_MDP()
    
    #Menu
    print("1. Changer le mot de passe maître")
    print("2. Générer un mot de passe")
    print("3. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        Changer_MDP()
        Exercice3()
        
    elif choix == "2":
        # Lire le mot de passe maître
        mdp = Lire_MDP()
        # Demander le tag et la taille
        tag = input("Saisir le tag : ")
        taille = int(input("Saisir la taille : "))
        # Appeler la fonction H
        print(Exercice2.H(mdp, tag, taille))
        Exercice3()

    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choix invalide.")
        Exercice3()
    
    
    
def Changer_MDP():
    with open('mpwd.txt', 'w') as fichier:
        mdp = input("Saisir le mot de passe maître : ")
        # Ecrire le mot de passe dans le fichier
        fichier.write(mdp)
        print("Le mot de passe a été changé.")   

def Lire_MDP()-> str:
    with open('mpwd.txt', 'r') as fichier:
        mdp = fichier.read()
        return mdp


if __name__ == "__main__":
    Exercice3()