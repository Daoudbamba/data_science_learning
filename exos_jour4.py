# Exercice 4 : Afficher les nombres de 1 à 100
# n = 100
# for i in range(1, n+1):
#     print(i)


# Exercice  : Afficher les nombres pairs de 1 à 100
# n=100
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)


# Exercice  : Afficher la somme des éléments d'une liste
# n=[11, 2, 32, 5, 6, 70]
# s=0
# for i in n:
#     s=s+i
# print(s)          

n=[11, 2, 32, 5, 6, 70]
max = n[0]
for i in n:
    max = n[0]
    if i > max:
        max = i
print(max)  