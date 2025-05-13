#============RESPOSTA PROFESSOR===============



m1 = float(input("lado 1"))
m2 = float(input("lado 2"))
m3 = float(input("lado 3 "))

if m1 == m2 == m3:
    print("equilatero")
elif m1 != m2 and m2 != m3 and m1 != m3 :
    print("escaleno")
if not (m1 == m2 == m3) and (m1 == m2 or m2 == m3 or m1 == m3):
    print('isóceles')
