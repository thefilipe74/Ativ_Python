
#============declaração das variaves!=================

m1 = float(input("informe o prieiro valor do triangulo :"))
m2 = float(input("informe o segundo valor do triangulo :"))
m3 = float(input("informe o terceiro valor do triangulo : "))

if m1 == m2 and m1 == m3 and m2 == m3 :
    print("o triangulo é equilatero !")
#=============triangulo isoiceles===================
elif m1 == m2 and m1 == m3 and m2 != m3:
    print("o triangulo é isoiceles !")
elif m2 == m3 and m2 == m1 and m1 != m3 :
    print("o triangulo é isoiceles !")
elif m3 == m1 and m1 == m3 and m2 != m1 :
    print("o triangulo é isoiceles !")
elif m1 != m2 and m1 != m3 and m2 == m3 :
    print("o triangulo é isoiceles !")
elif m3 != m2 and m3 != m1 and m2 == m1 :
    print("o triangulo é isoiceles !")
#==============triangulo isoiceles===================
# elif m1 != m2 and m1 != m3 and m2 != m3:
# print("o triangulo é !")
else:
    print("o triangulo é escaleno !")


