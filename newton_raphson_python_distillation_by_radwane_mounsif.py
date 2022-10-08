import math
Z1=0.1
Z2=0.2
Z3=0.3
Z4=0.4
k1=4.2
k2=1.75
k3=0.74
k4=0.34
F=100
Tf=200
Pf=100
F=100
k=0.121
Eps=0
def RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    Results = (((Z1*(1-k1))/(1+k*(k1-1)))+((Z2*(1-k2))/(1+k*(k2-1)))+((Z3*(1-k3))/(1+k*(k3-1)))+((Z4*(1-k4))/(1+k*(k4-1))))
    return Results
def RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    Results_dri=(Z1*(1-k1)**2)/((1+k*(k1-1)**2))+((Z2*(1-k2)**2)/((1+k*(k2-1))**2))+((Z3*(1-k3)**2)/((1+k*(k3-1))**2))+((Z4*(1-k4)**2)/((1+k*(k4-1))**2))
    return Results_dri
fonction_obj=RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4)
while abs(fonction_obj) >= Eps:
    ksi=k-(fonction_obj/RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4))
    print("la valeur de notre fonction qu’est plus proche de zéro est de ",abs(fonction_obj), "si ψ", ksi)
    k=ksi
    Eps=Eps+0.001

# calcul des parametres
V=F*k
print("V est de ", V)
L = F - V
print("L est de ", L)
x1 = Z1 / (1 + k * (k1 - 1))
print("la composition de la phase liquide  de 1 est de ", x1)
x2 = Z2 / (1 + k * (k2 - 1))
print("la composition de la phase liquide  de 2 est de ", x2)
x3 = Z3 / (1 + k * (k3 - 1))
print("la composition de la phase liquide  de 3 est de ", x3)
x4 = Z4 / (1 + k * (k4 - 1))
print("la composition de la phase liquide  de 4 est de ", x4)
y1 = x1 * k1
print("la composition de la phase gazeuse  de 1 est de ", y1)
y2 = x2 * k2
print("la composition de la phase gazeuse  de 2 est de ", y2)
y3 = x3 * k3
print("la composition de la phase gazeuse  de 3 est de ", y3)
y4 = x4 * k4
print("la composition de la phase gazeuse  de 4 est de ", y4)

    


