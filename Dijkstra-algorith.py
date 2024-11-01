import math

listetourisme_p= [[(7,50),(8,220)],[(6,50)],[(5,141),(7,100),(8,170)],[(6,295),(7,222)],[(5,220),(6,420),(8,192)],[(2,141),(4,220),(6,316),(8,122)],[(1,50),(3,295),(4,420),(5,316),(8,450)],[(0,50),(2,100),(3,222)],[(0,220),(2,170),(4,192),(5,122),(6,450)]]


MatTourisme_p = [[0, 0, 0, 0, 0, 0, 0, 50, 220],
                 [0, 0, 0, 0, 0, 0, 50, 0, 0],
                 [0, 0, 0, 0, 0, 141, 0, 100, 170],
                 [0, 0, 0, 0, 0, 0, 295, 222, 0],
                 [0, 0, 0, 0, 0, 220, 420, 0, 192],
                 [0, 0, 141, 0, 220, 0, 316, 0, 122],
                 [0, 50, 0, 295, 420, 316, 0, 0, 450],
                 [50, 0, 100, 222, 0, 0, 0, 0, 0],
                 [220, 0, 170, 0, 192, 122, 450, 0, 0]]


listecentreville = [    [(1,2),(2,5)],[(2,2),(5,4)],[(3,3),(4,6)],[(4,1),(6,2)],[(7,4)],[(3,1),(6,4),(7,7)],[(7,2)],[]     ]


MatCentreVille = [[0, 2, 5, 0, 0, 0, 0, 0],
                  [0, 0, 2, 0, 0, 4, 0, 0],
                  [0, 0, 0, 3, 6, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0, 4],
                  [0, 0, 0, 1, 0, 0, 4, 7],
                  [0, 0, 0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0, 0, 0]]


import math

def Djikstra(G, depart, arivee):
    """
    Effectue l'algorithme de Dijkstra pour trouver le plus court chemin entre un nœud de départ et un nœud d'arrivée dans un graphe pondéré.

    Arguments :
    - G : Liste d'adjacence représentant le graphe pondéré.
    - depart : Nœud de départ.
    - arivee : Nœud d'arrivée.

    Retour :
    - chemin : Liste des nœuds formant le plus court chemin de départ à arrivée.
    - distance : Distance totale du plus court chemin.
    """

    # Initialisation des structures de données
    A_traiter = []
    Distances = []
    Provenance = []

    for i in range(len(G)):
        A_traiter.append(i)
        Distances.append(math.inf)
        Provenance.append(0)

    en_cours = []
    en_cours.append(depart)
    Distances[depart] = 0

    # Boucle principale de l'algorithme
    while len(A_traiter) > 0 and en_cours[0] != arivee:
        A_traiter.remove(en_cours[0])
        p = math.inf
        listedesvoisins = []
        j = 0

        # Parcours des voisins du nœud en cours
        for i in G[en_cours[0]]:
            if i != 0:
                listedesvoisins.append(j)
                if i + Distances[en_cours[0]] < Distances[j]:
                    Distances[j] = i + Distances[en_cours[0]]
                    Provenance[j] = en_cours[0]
            j += 1

        j = 0

        # Recherche du nœud avec la distance minimale parmi les nœuds restants
        for i in Distances:
            if i != 0 and i < p and j in A_traiter:
                p = i
                sommet = j
            j += 1

        en_cours[0] = sommet

    # Construction du chemin à partir des nœuds visités
    a = arivee
    chemin = [depart, arivee]
    while Provenance[a] != depart:
        chemin.insert(1, Provenance[a])
        a = Provenance[a]

    return chemin, "avec une Distance de :", Distances[arivee]






print("le chemin le plus cours de B(0) a D(1) est : ",Djikstra([[0, 0, 0, 0, 0, 0, 0, 50, 220],
                 [0, 0, 0, 0, 0, 0, 50, 0, 0],
                 [0, 0, 0, 0, 0, 141, 0, 100, 170],
                 [0, 0, 0, 0, 0, 0, 295, 222, 0],
                 [0, 0, 0, 0, 0, 220, 420, 0, 192],
                 [0, 0, 141, 0, 220, 0, 316, 0, 122],
                 [0, 50, 0, 295, 420, 316, 0, 0, 450],
                 [50, 0, 100, 222, 0, 0, 0, 0, 0],
                 [220, 0, 170, 0, 192, 122, 450, 0, 0]],0,1))
                
            
        
        
        
print("le chemin le plus cours dans le centre ville pour allez de 2 a 7 est : ",Djikstra([[0, 2, 5, 0, 0, 0, 0, 0],
                  [0, 0, 2, 0, 0, 4, 0, 0],
                  [0, 0, 0, 3, 6, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0, 4],
                  [0, 0, 0, 1, 0, 0, 4, 7],
                  [0, 0, 0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0, 0, 0]],1,6))  



# ============================================================ Question 1 ==============================================================
# cet algorythme se fonde sur le parcours en largeur

# ============================================================ Question 2 ==============================================================

# il appartient au type des gloutons

# ============================================================ Question 3 ==============================================================

# La terminaison de l'algorithme garantit qu'il s'arrêtera après un nombre fini d'itérations et ne bouclera 
# pas indéfiniment. En prouvant la terminaison, on s'assure que l'algorithme trouvera une solution ou indiquera qu'aucun chemin n'existe 
# entre les nœuds de départ et d'arrivée. 
# La correction de l'algorithme assure qu'il fournit la solution correcte, c'est-à-dire le chemin 
# le plus court entre les nœuds de départ et d'arrivée. En prouvant la correction, on démontre que l'algorithme 
# trouve effectivement le chemin optimal en utilisant la méthode de Dijkstra.
# La preuve de terminaison implique de montrer qu'il existe une condition d'arrêt pour la boucle while, 
# garantissant que le nombre d'itérations est limité. Cela peut être réalisé en montrant que, à chaque itération, 
# le nombre de nœuds non traités diminue d'au moins un, jusqu'à ce qu'il n'en reste plus.
# La preuve de correction implique de montrer que les distances et les chemins calculés par l'algorithme sont corrects.
# En prouvant à la fois la terminaison et la correction de l'algorithme de Dijkstra, on peut être sûr que l'algorithme fonctionnera correctement pour n'importe quel graphe pondéré donné et produira le chemin le plus court entre les nœuds de départ et d'arrivée.


# ============================================================ Question 4 ==============================================================

# Soit n le nombre initial de sommets à traiter.
# Au début de l'algorithme, n est égal au nombre total de sommets du graphe. Donc, n ≥ 0.
# Hypothèse de récurrence :
# Supposons que l'algorithme se termine après k itérations lorsque le nombre de sommets à traiter est n.
# À la (k+1)-ème itération de la boucle while, un sommet est retiré de la liste "A_traiter", ce qui réduit le nombre de sommets à traiter de 1. Donc,
# le nombre de sommets à traiter à cette étape est n - 1.
# Selon l'hypothèse de récurrence, l'algorithme se termine après k itérations lorsque 
# le nombre de sommets à traiter est n. Donc, à la (k+1)-ème itération, le nombre de sommets à traiter est n - 1.
# Conclusion :
# En utilisant la récurrence, nous avons montré que si l'algorithme se termine après k itérations lorsque le nombre de 
# sommets à traiter est n, alors il se terminera également après (k+1) itérations lorsque le nombre de sommets à traiter est n - 1.
# Puisque n est initialisé au nombre total de sommets du graphe (len(G)), qui est un entier positif, et que le nombre de
#  sommets à traiter diminue strictement à chaque itération de la boucle while, nous pouvons conclure que 
#  l'algorithme se terminera après un nombre fini d'itérations. Par conséquent, la terminaison de l'algorithme est prouvée.


# ============================================================ Question 5 ==============================================================




# Pour prouver la correction de cet algorithme, nous allons utiliser comme invariant 
# de boucle la propriété suivante :

# Invariant de boucle : À chaque itération de la boucle while, la distance 
# associée à chaque sommet déjà traité est la distance minimale par rapport au sommet de départ.

# Preuve de correction :

# Initialisation : Au début de l'algorithme, toutes les distances sont 
# initialisées à l'infini, sauf la distance du sommet de départ qui est de 0 
# (Distances[depart] = 0). Par conséquent, l'invariant de boucle est vérifié initialement.

# Hypothèse d'induction : Supposons que l'invariant de boucle soit vrai à
#  une certaine itération donnée de la boucle while.

# Étape de mise à jour : À chaque itération de la boucle while, 
# le sommet en_cours[0] est retiré de la liste "A_traiter" et les distances 
# et les provenances de ses voisins sont mises à jour si nécessaire. Par conséquent, 
# à la fin de cette itération, le sommet en_cours[0] est traité.

# Maintien de l'invariant : Lorsque le sommet en_cours[0] est traité, cela 
# signifie que toutes les distances vers ses voisins ont été mises à jour correctement. 
# La distance minimale vers chaque voisin a été déterminée en comparant les distances actuelles 
# avec la distance du sommet en_cours[0] plus le poids de l'arête qui les relie. Par conséquent,
#  après cette mise à jour, la distance associée à chaque sommet déjà traité reste la distance minimale 
#  par rapport au sommet de départ.

# Terminaison : La boucle while continue tant qu'il reste des sommets à traiter dans 
# la liste "A_traiter". Lorsque tous les sommets ont été traités, c'est-à-dire lorsque 
# len(A_traiter) = 0, l'algorithme se termine.

# Conclusion :
# En utilisant l'invariant de boucle précédent, nous avons montré que 
# lors de chaque itération de la boucle while, la distance associée à chaque sommet
#  déjà traité est la distance minimale par rapport au sommet de départ. Comme 
#  l'algorithme se termine après avoir traité tous les sommets, nous pouvons conclure
#  que les distances finales attribuées à chaque sommet sont correctes et représentent 
#  les distances minimales par rapport au sommet de départ.
# Ainsi, la correction de l'algorithme de Dijkstra est prouvée.








