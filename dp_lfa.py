letTxt = open('automato.txt', 'r')
automato = letTxt.readlines()

automato = [line.replace("\n", "") for line in automato]

def remove_duplicidade(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    lista = l
    return lista


def exist (valor , lista):
    for l in lista:
        if valor not in l[2]:
            return False
        else:
            return True

alfabeto = []
for i in range(int(automato[0])):
    alfabeto.append(i)
estados = []
for estado in automato[1]:
    estados.append(estado)
estado_inicial = []
for estado in automato[2]:
    if estado != ' ':
        estado_inicial.append(estado)
estados_finais = []
for estado in automato[3]:
    if estado != ' ':
        estados_finais.append(estado)

possibilidades= []

pega_entradas=[]
for i in range(4, len(automato)):
    aux = automato[i]

    for estado_colocado in alfabeto:
        try:
            if estado_colocado == int(aux[0]):
                possibilidades.append(aux)

        except:
            pega_entradas.append(aux)
            continue



entradas = remove_duplicidade(pega_entradas)


situacao_automato= estado_inicial
recebe_estado= ''

for i in alfabeto:
    for entrada in entradas:
        for i 
        if entrada ==


print('cabo')









