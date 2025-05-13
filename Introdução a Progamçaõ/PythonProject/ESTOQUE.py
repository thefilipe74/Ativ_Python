Qmax = 10.000
Qmin = 2.000
Qreal = 4.300

Qmedia = (Qmax + Qmin /2)

compra = int(input("Quanto voce quer comprar ? "))

if compra < Qreal:
    print("Realize compra para o estoque")
elif compra > Qreal:
    print("Não relaize a commpra para o estoque")
else:
    print('FIM DO PROGAMA')