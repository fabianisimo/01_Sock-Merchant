import random

def entrada_variables():
    n = random.randint(1, 20)
    ar = []
    for a in range(n):
        i = random.randint(1, 20)
        ar.append(i)
    return [n, ar]

entrada = entrada_variables()
n = entrada[0]
ar = entrada[1]

def sockMerchant(n,ar):
    cant_pares = 0
    posiciones_tomadas = []
    for i in range(n-1):
        for o in range(i+1, n):
            if i in posiciones_tomadas or o in posiciones_tomadas:
                pass
            else:
                if ar[i] == ar[o]:
                    cant_pares = cant_pares + 1
                    posiciones_tomadas.append(i)
                    posiciones_tomadas.append(o)
    return cant_pares


print (n)
print (ar)
pares_encontrados = sockMerchant(n,ar)
print (pares_encontrados)
