import Exercice2


#Faire un fichier avec le MDP maitre 

def Exercice3():
    """
    Cette fonction sert de menu principal pour un système de gestion de mots de passe. Elle effectue les tâches suivantes :
    1. Vérifie si le fichier 'mpwd.txt' existe. Sinon, il crée le fichier.
    2. Lit le contenu de 'mpwd.txt'. Si le fichier est vide, elle appelle la fonction `Changer_MDP` pour changer le mot de passe maître.
    3. Affiche un menu avec trois options :
        a. Changer le mot de passe maître.
        b. Générer un mot de passe.
        c. Quitter le programme.
    4. En fonction du choix de l'utilisateur, elle effectue l'action correspondante :
        a. Appelle la fonction `Changer_MDP` pour changer le mot de passe maître puis redémarre le menu.
        b. Lit le mot de passe maître en utilisant la fonction `Lire_MDP`, demande un tag et une taille, puis appelle la fonction `Exercice2.H` pour générer un mot de passe. Redémarre le menu.
        c. Affiche un message d'adieu et quitte.
        d. Si le choix est invalide, elle affiche un message d'erreur et redémarre le menu.
    """
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