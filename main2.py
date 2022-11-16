from pprint import pprint
# creating an empty list
lstz = []
lstk = []
lstfunction = []
lstfunctiond = []
lsttest = []
lstksi = []
lstx = []
lsty = []
lstname = []
ksi = 0.12
Eps = 0

# number of elements as input
try:
 n = int(input("Enter number of elements : "))
except :
 print("erruer, SVP entre une valeur exact")

# iterating till the range
try:
 for i in range(0, n):
     # about the name of element
    print("entre name of element",i+1, ':')
    nz = input()
    # about z
    print('z',i+1,'=')
    z = float(input())
    # about k
    print('k', i + 1, '=')
    k = float(input())
    #function
    function_obj = (z*(1-k))/(1+ksi*(k-1))
    function_dr = (z * (1 - k) ** 2)/ ((1 + ksi*(k + 1)**2))

    # adding the element
    lstz.append(z)
    lstk.append(k)
    lstname.append(nz)
    lstfunction.append(function_obj)
    lstfunctiond.append(function_dr)
except:
 print("erruer, SVP entre une valeur exact")

# print(lstz)
# print(lstk)
# print(lstfunction)
# print(lstfunctiond)
sum_function = sum(lstfunction)
sum_functiond = sum(lstfunctiond)
# print('function =',sum_function)
# print('functiond =',sum_functiond)


# iteration
while ksi >= 0 and ksi <= 1 and abs(sum_function) >= Eps:
    ksi1=ksi-(sum_function/sum_functiond)
    ksi=ksi1
    lsttest.append(abs(sum_function))
    lstksi.append(ksi1)
    Eps=Eps+0.00001


totals = list(zip(lsttest, lstksi))  # All elements in one list
# pprint(totals)
# print('\n')

x = list(filter(lambda item: min(totals[1]), totals[0])) # filter to find min function obj +-= 0
# pprint(x)
function_0 = x[0]
ksi_obj = x[1]
print("la valeur de notre fonction, plus proche de zéro est de ", function_0, "si ψ", ksi_obj)
print('\n')

try:
 print("donner la valeur de débit d'alimentation F") # INPUT FLOW
 F = float(input())
except:
    print('erreur')

V = F*ksi_obj
print("Débit de vapeur: V=",V)
L = F - V
print("Débit de liquide: L est de=",L)
print('\n')
for i in range(0, n):
        x = lstz[i] / (1 + ksi_obj * (lstk[i] - 1))
        lstx.append(x)
        y = lstx[i] * lstk[i]
        nx = i+1
        lsty.append(y)
        print('la fraction liquide de ',lstname[i] ,':x', nx,'=', lstx[i])
        print('la fraction vapeur de ',lstname[i] , ':y', nx, '=', lsty[i])
        print('\n')