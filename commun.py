import numpy as np

def grille(n, L=1.0):
    x = np.linspace(0, L, n)
    return x, x[1] - x[0]

def laplacien_1d(x):
    n, dx = len(x), x[1] - x[0]
    D2 = (np.eye(n, k=1) - 2*np.eye(n) + np.eye(n, k=-1)) / dx**2
    D2[0, :] = 0
    D2[-1, :] = 0
    return D2

print("normalement c bon ca c'es notre dossier commun, suffit de faire deux trois commandes à chaque debut et fin de session pour l'envoyer sur github (demande a claude))