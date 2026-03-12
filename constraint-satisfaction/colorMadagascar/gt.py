import itertools

# Données originales de l'utilisateur
prov = ["Tana", "Majunga", "Tamatave", "Fianarantsoa", "Diego", "Tulear"]
col = ["Red", "Green", "Blue"]
contrainte = [
    "Tana-Majunga",
    "Tana-Tamatave",  
    "Tana-Fianarantsoa",
    "Tana-Tulear", 
    "Diego-Majunga",
    "Diego-Tamatave",
    "Tamatave-Majunga",
    "Tamatave-Fianarantsoa",
    "Majunga-Tulear",
    "Fianarantsoa-Tulear"
]

def solve():
    # 1. GENERATE : Créer toutes les combinaisons possibles (3^6 = 729)
    # itertools.product génère toutes les attributions possibles de couleurs
    for combinaison in itertools.product(col, repeat=len(prov)):
        # prov_col : la combinaison actuelle à tester (list)
        prov_col = list(combinaison)
        
        # 2. TEST : Vérifier chaque contrainte pour cette combinaison
        est_valide = True
        for c in range(len(contrainte)):
            # On sépare les deux provinces (ex: "Tana" et "Majunga")
            spliter = contrainte[c].split("-")
            
            # On récupère l'index de chaque province dans la liste 'prov'
            idx0 = prov.index(spliter[0])
            idx1 = prov.index(spliter[1])
            
            # TEST CRITIQUE : Si les deux provinces adjacentes ont la même couleur, c'est FAUX
            if prov_col[idx0] == prov_col[idx1]:
                est_valide = False
                break
        
        # Si la combinaison a passé TOUS les tests, on a trouvé une solution
        if est_valide:
            return prov_col

    return None

if __name__ == "__main__":
    resultat = solve()
    if resultat:
        print("Solution trouvé (Generate & Test) :")
        for i in range(len(prov)):
            print(f"{prov[i]:<15} : {resultat[i]}")
    else:
        print("Pas de solution trouvé.")