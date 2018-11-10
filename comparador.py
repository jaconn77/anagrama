#Detector de Anagramas
def anagramaRespuesta(cadena1,cadena2):
    lista1=list(cadena1)
    lista2=list(cadena2)

    lista1.sort()
    lista2.sort()

    num = 0
    cumple = True

    while num < len(cadena1) and cumple:
        if lista1[num] == lista2[num]:
            num = num + 1

        else:
            cumple = False

    return cumple

print(anagramaRespuesta("poca","apoc"))