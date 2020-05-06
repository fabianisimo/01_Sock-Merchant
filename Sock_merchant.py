import random


def entrada_variables():
    n = random.randint(1, 10)
    ar = []
    for a in range(n):
        i = random.randint(1, 10)
        ar.append(i)
    return [n, ar]

def printea_datos(entrada):
    n = entrada[0]
    ar = entrada[1]
    print (n)
    print (ar)
    #print (len(ar))

entrada = entrada_variables()
n = entrada[0]
ar = entrada[1]

entrada = printea_datos(entrada)


cant_pares = 0
posiciones_tomadas = []

for i in range(n-1):
    checando = ar[i]
    if i in posiciones_tomadas:
        pass
    else:
        print (checando)
        for o in range(i+1, n):
            if ar[i] == ar[o]:
                cant_pares = cant_pares + 1
                posiciones_tomadas.append(i)
                posiciones_tomadas.append(o)

print ("posiciones tomadas: ",posiciones_tomadas)
print ("pares encontrados: ",cant_pares)
