#Job8

def my_sort(L):
    coups = 0  # Compteur pour le nombre de "coups" (ou échanges) nécessaires pour trier

    # Boucle principale qui va "buller" les éléments à leur place
    n = len(L)
    for i in range(n):
        # On parcourt la liste du début jusqu'à la fin - i (car la fin est déjà triée)
        for j in range(0, n - 1 - i):  # On ignore les derniers éléments déjà triés
            if L[j] > L[j + 1]:  # Si l'élément actuel est plus grand que l'élément suivant
                L[j], L[j + 1] = L[j + 1], L[j]  # On échange les éléments
                coups += 1  # On compte un échange nécessaire (ou "coup")
    
    print("Nombre total de coups nécessaires pour trier la liste :", coups)
    return L


# Exemple d'utilisation
L = [22, 12, 11, 25, 34, 90, 64]
list_triee = my_sort(L)

print("Liste triée :", list_triee)

