"""
Estados : 0,1,2,3,4,5,6,7,8,9,10,11,12 numeros de carros no stand
Estagio(?) : 1 dia

>Recebe 30€ por cada carro alugado

>Stock não é partilhado

>Carros q são entregues so podem ser usados no dia a seguir

>Carros podem ser transferidos, 3 por dia, a 7€ o carro

>Filiais tem estacionamento para 8 carros, mais do q isso e é preciso alugar um espaço a 10€ por noite
              0       1       2       3       4       5       6       7       8       9       10      11      12          """
f1Pedido =  [0.0528, 0.0904, 0.1216, 0.1396, 0.1184, 0.1112, 0.0988, 0.0852, 0.0596, 0.0568, 0.0368, 0.0220, 0.0068]
f1Entrega = [0.0348, 0.0820, 0.1180, 0.1396, 0.1264, 0.1188, 0.0932, 0.0888, 0.0640, 0.0556, 0.0436, 0.0256, 0.0096]

f2Pedido =  [0.0352, 0.0724, 0.1024, 0.1336, 0.1388, 0.1236, 0.1048, 0.0900, 0.0704, 0.0608, 0.0380, 0.0220, 0.0080]
f2Entrega = [0.0384, 0.1312, 0.2312, 0.2296, 0.1516, 0.1156, 0.0584, 0.0288, 0.0080, 0.0056, 0.0012, 0.0004, 0.0000]

import xlsxwriter

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD NAO EXISTE TRANSFERENCIA DE CARROS
matrixF1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 1 CARRO DA FILIAL 1 PARA A 2
matrixF1_C1_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C1_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C1_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 2 CARRO DA FILIAL 1 PARA A 2
matrixF1_C2_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C2_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C2_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 3 CARRO DA FILIAL 1 PARA A 2
matrixF1_C3_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C3_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF1_C3_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 1 CARRO DA FILIAL 2 PARA A 1
matrixF2_C1_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C1_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C1_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 2 CARRO DA FILIAL 2 PARA A 1
matrixF2_C2_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C2_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C2_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A PROBABILIDADES QD EXISTE TRANSFERENCIA DE 3 CARRO DA FILIAL 2 PARA A 1
matrixF2_C3_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C3_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixF2_C3_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM AO CUSTO QD NAO EXISTE TRANSFERENCIA DE CARROS
matrixC_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 1 CARRO DA FILIAL 1 PARA A 2
matrixC_F1_C1_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C1_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C1_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 2 CARRO DA FILIAL 1 PARA A 2
matrixC_F1_C2_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C2_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C2_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 3 CARRO DA FILIAL 1 PARA A 2
matrixC_F1_C3_F2_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C3_F2_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F1_C3_F2_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 1 CARRO DA FILIAL 2 PARA A 1
matrixC_F2_C1_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C1_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C1_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 2 CARRO DA FILIAL 2 PARA A 1
matrixC_F2_C2_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C2_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C2_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q CORRESPONDEM A CUSTO QD EXISTE TRANSFERENCIA DE 3 CARRO DA FILIAL 2 PARA A 1
matrixC_F2_C3_F1_F1 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C3_F1_F2 = [[0.0 for h in range(13)] for o in range(13)]
matrixC_F2_C3_F1_F1xF2 =[[0.0 for h in range(169)] for o in range(169)]

# MATRIZES Q VÃO REPRESENTAR O Q, A MISTURA ENTRE AS PROBABILIDADES E O CUSTO
q0 = [[0.0 for h in range(1)] for o in range(169)]
qF1_1_F2 = [[0.0 for h in range(1)] for o in range(169)]
qF1_2_F2 = [[0.0 for h in range(1)] for o in range(169)]
qF1_3_F2 = [[0.0 for h in range(1)] for o in range(169)]
qF2_1_F1 = [[0.0 for h in range(1)] for o in range(169)]
qF2_2_F1 = [[0.0 for h in range(1)] for o in range(169)]
qF2_3_F1 = [[0.0 for h in range(1)] for o in range(169)]

dn = [[0.0 for h in range(1)] for o in range(169)]
politica = [[-1 for h in range(7)] for o in range(169)]

#VARIAVEL COM O NUMERO DE ITERAÇÕES A FAZER NO ALGORITMO, PODEMOS METER QUANTAS QUISERMOS
itsAFazer = 200

def matrixCalculator(filial):
    if(filial == 1):
        pEntrega = f1Entrega
        pPedido = f1Pedido
    else:
        pEntrega = f2Entrega
        pPedido = f2Pedido

    for i in range(13):
        lineTotal = 0

        for x in range(12):
            pedido = i
            entrega = x
            probability = 0

            probabilidadeAcumulada = 0
            for l in range(pedido,13):
                probabilidadeAcumulada += pPedido[l]

            probability += probabilidadeAcumulada * pEntrega[entrega]
            pedido -= 1
            entrega -= 1

            while entrega >= 0 and pedido >= 0:
                probability += pPedido[pedido] * pEntrega[entrega]
                pedido -= 1
                entrega -= 1

            if(filial == 1):
                matrixF1[i][x] += probability
            else:
                matrixF2[i][x] += probability

            lineTotal += probability

        pedido = i
        entrega = 12
        probability = 0
        probabilidadeEntregasAc = 0

        probabilidadeEntregasAc += pEntrega[entrega]
        probabilidadeAcumulada = 0

        for k in range(pedido,13):
            probabilidadeAcumulada += pPedido[k]

        probability += probabilidadeAcumulada * probabilidadeEntregasAc
        pedido-=1
        entrega-=1

        while pedido >= 0 :
            probabilidadeEntregasAc += pEntrega[entrega]
            probability += pPedido[pedido] * probabilidadeEntregasAc
            pedido-=1
            entrega-=1

        lineTotal += probability

        if(filial == 1):
            matrixF1[i][12] += probability
        else:
            matrixF2[i][12] += probability

def bigMatrixCalculator():
    coluna = 0
    linha = 0
    for f1Linha in range(13):
        for f1Coluna in range(13):
            coluna = 0
            for f2Linha in range(13):
                for f2Coluna in range(13):
                    matrixF1xF2[linha][coluna] = matrixF1[f1Linha][f2Linha] * matrixF2[f1Coluna][f2Coluna]
                    matrixF1_C1_F2_F1xF2[linha][coluna] = matrixF1_C1_F2_F1[f1Linha][f2Linha] * matrixF1_C1_F2_F2[f1Coluna][f2Coluna]
                    matrixF1_C2_F2_F1xF2[linha][coluna] = matrixF1_C2_F2_F1[f1Linha][f2Linha] * matrixF1_C2_F2_F2[f1Coluna][f2Coluna]
                    matrixF1_C3_F2_F1xF2[linha][coluna] = matrixF1_C3_F2_F1[f1Linha][f2Linha] * matrixF1_C3_F2_F2[f1Coluna][f2Coluna]
                    matrixF2_C1_F1_F1xF2[linha][coluna] = matrixF2_C1_F1_F1[f1Linha][f2Linha] * matrixF2_C1_F1_F2[f1Coluna][f2Coluna]
                    matrixF2_C2_F1_F1xF2[linha][coluna] = matrixF2_C2_F1_F1[f1Linha][f2Linha] * matrixF2_C2_F1_F2[f1Coluna][f2Coluna]
                    matrixF2_C3_F1_F1xF2[linha][coluna] = matrixF2_C3_F1_F1[f1Linha][f2Linha] * matrixF2_C3_F1_F2[f1Coluna][f2Coluna]

                    matrixC_F1xF2[linha][coluna] = matrixC_F1[f1Linha][f2Linha] + matrixC_F2[f1Coluna][f2Coluna]
                    matrixC_F1_C1_F2_F1xF2[linha][coluna] = matrixC_F1_C1_F2_F1[f1Linha][f2Linha] + matrixC_F1_C1_F2_F2[f1Coluna][f2Coluna]
                    matrixC_F1_C2_F2_F1xF2[linha][coluna] = matrixC_F1_C2_F2_F1[f1Linha][f2Linha] + matrixC_F1_C2_F2_F2[f1Coluna][f2Coluna]
                    matrixC_F1_C3_F2_F1xF2[linha][coluna] = matrixC_F1_C3_F2_F1[f1Linha][f2Linha] + matrixC_F1_C3_F2_F2[f1Coluna][f2Coluna]
                    matrixC_F2_C1_F1_F1xF2[linha][coluna] = matrixC_F2_C1_F1_F1[f1Linha][f2Linha] + matrixC_F2_C1_F1_F2[f1Coluna][f2Coluna]
                    matrixC_F2_C2_F1_F1xF2[linha][coluna] = matrixC_F2_C2_F1_F1[f1Linha][f2Linha] + matrixC_F2_C2_F1_F2[f1Coluna][f2Coluna]
                    matrixC_F2_C3_F1_F1xF2[linha][coluna] = matrixC_F2_C3_F1_F1[f1Linha][f2Linha] + matrixC_F2_C3_F1_F2[f1Coluna][f2Coluna]

                    coluna += 1
            linha += 1

def bigMatrixLineSum(matrix):
    lineTotal = 0
    for linha in range(169):
        for coluna in range(169):
            lineTotal += matrix[linha][coluna]

    print("Soma das probabilidades da Linha",linha,":",lineTotal)

def matrixBuilder_TrfXCarros():
    for linha in range(0,13):
        for coluna in range(0,12):
            matrixF1_C1_F2_F1[linha][coluna] = matrixF1[linha][(coluna+1)]
            matrixF2_C1_F1_F2[linha][coluna] = matrixF2[linha][(coluna+1)]

    for linha in range(0,13):
        for coluna in range(0,11):
            matrixF1_C2_F2_F1[linha][coluna] = matrixF1[linha][(coluna+2)]
            matrixF2_C2_F1_F2[linha][coluna] = matrixF2[linha][(coluna+2)]

    for linha in range(0,13):
        for coluna in range(0,10):
            matrixF1_C3_F2_F1[linha][coluna] = matrixF1[linha][(coluna+3)]
            matrixF2_C3_F1_F2[linha][coluna] = matrixF2[linha][(coluna+3)]

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C1_F2_F1[linha][coluna]
            sum2 += matrixF2_C1_F1_F2[linha][coluna]
        for coluna in range(0,12):
            matrixF1_C1_F2_F1[linha][coluna] += ((1-sum1) * (matrixF1_C1_F2_F1[linha][coluna] / sum1))
            matrixF2_C1_F1_F2[linha][coluna] += ((1-sum2) * (matrixF2_C1_F1_F2[linha][coluna] / sum2))

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C2_F2_F1[linha][coluna]
            sum2 += matrixF2_C2_F1_F2[linha][coluna]
        for coluna in range(0,11):
            matrixF1_C2_F2_F1[linha][coluna] += ((1-sum1) * (matrixF1_C2_F2_F1[linha][coluna] / sum1))
            matrixF2_C2_F1_F2[linha][coluna] += ((1-sum2) * (matrixF2_C2_F1_F2[linha][coluna] / sum2))

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C3_F2_F1[linha][coluna]
            sum2 += matrixF2_C3_F1_F2[linha][coluna]
        for coluna in range(0,11):
            matrixF1_C3_F2_F1[linha][coluna] += ((1-sum1) * (matrixF1_C3_F2_F1[linha][coluna] / sum1))
            matrixF2_C3_F1_F2[linha][coluna] += ((1-sum2) * (matrixF2_C3_F1_F2[linha][coluna] / sum2))

def matrixBuilder_RcbXCarros():
    for linha in range(0,13):
        for coluna in range(1,13):
                matrixF1_C1_F2_F2[linha][coluna] = matrixF2[linha][(coluna-1)]
                matrixF2_C1_F1_F1[linha][coluna] = matrixF1[linha][(coluna-1)]

    for linha in range(0,13):
        for coluna in range(2,13):
                matrixF1_C2_F2_F2[linha][coluna] = matrixF2[linha][(coluna-2)]
                matrixF2_C2_F1_F1[linha][coluna] = matrixF1[linha][(coluna-2)]

    for linha in range(0,13):
        for coluna in range(3,13):
                matrixF1_C3_F2_F2[linha][coluna] = matrixF2[linha][(coluna-3)]
                matrixF2_C3_F1_F1[linha][coluna] = matrixF1[linha][(coluna-3)]

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C1_F2_F2[linha][coluna]
            sum2 += matrixF2_C1_F1_F1[linha][coluna]
        for coluna in range(1,13):
            matrixF1_C1_F2_F2[linha][coluna] += ((1-sum1) * (matrixF1_C1_F2_F2[linha][coluna] / sum1))
            matrixF2_C1_F1_F1[linha][coluna] += ((1-sum2) * (matrixF2_C1_F1_F1[linha][coluna] / sum2))

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C2_F2_F2[linha][coluna]
            sum2 += matrixF2_C2_F1_F1[linha][coluna]
        for coluna in range(2,13):
            matrixF1_C2_F2_F2[linha][coluna] += ((1-sum1) * (matrixF1_C2_F2_F2[linha][coluna] / sum1))
            matrixF2_C2_F1_F1[linha][coluna] += ((1-sum2) * (matrixF2_C2_F1_F1[linha][coluna] / sum2))

    for linha in range(0,13):
        sum1,sum2 = 0,0
        for coluna in range(0,13):
            sum1 += matrixF1_C3_F2_F2[linha][coluna]
            sum2 += matrixF2_C3_F1_F1[linha][coluna]
        for coluna in range(3,13):
            matrixF1_C3_F2_F2[linha][coluna] += ((1-sum1) * (matrixF1_C3_F2_F2[linha][coluna] / sum1))
            matrixF2_C3_F1_F1[linha][coluna] += ((1-sum2) * (matrixF2_C3_F1_F1[linha][coluna] / sum2))

def costMatrixCalculator(filial):
    if(filial == 1):
        pEntrega = f1Entrega
        pPedido = f1Pedido
        matrizP = matrixF1
    else:
        pEntrega = f2Entrega
        pPedido = f2Pedido
        matrizP = matrixF2

    for i in range(13):
        lineTotal = 0

        for x in range(12):
            pedido = i
            entrega = x
            custo = 0

            probabilidadeAcumulada = 0
            for l in range(pedido,13):
                probabilidadeAcumulada += pPedido[l]

            custo += ( (probabilidadeAcumulada * pEntrega[entrega]) / matrizP[i][x] ) * (pedido * 30)
            #custo += (probabilidadeAcumulada * (pedido * 30)) * pEntrega[entrega]
            pedido -= 1
            entrega -= 1

            while entrega >= 0 and pedido >= 0:
                custo += ( (pPedido[pedido] * pEntrega[entrega]) / matrizP[i][x] ) * (pedido * 30)
                #custo += (pPedido[pedido] * (pedido * 30)) * pEntrega[entrega]
                pedido -= 1
                entrega -= 1

            if( x >= 9):
                custo -= 10

            #print("Custo de ir do estado ",i," para o estado ",x," :",custo)

            if(filial == 1):
                matrixC_F1[i][x] += custo
            else:
                matrixC_F2[i][x] += custo

            lineTotal += custo

        pedido = i
        entrega = 12
        custo = 0
        probabilidadeEntregasAc = 0

        probabilidadeEntregasAc += pEntrega[entrega]
        probabilidadeAcumulada = 0

        for k in range(pedido,13):
            probabilidadeAcumulada += pPedido[k]

        if(matrizP[i][12] != 0):
            custo += ( (probabilidadeAcumulada * probabilidadeEntregasAc) / matrizP[i][12] ) * (pedido * 30)

        #custo += (probabilidadeAcumulada * (pedido * 30)) * probabilidadeEntregasAc
        pedido-=1
        entrega-=1

        while pedido >= 0 :
            probabilidadeEntregasAc += pEntrega[entrega]
            if(matrizP[i][12] != 0):
                custo += ( (pPedido[pedido] * probabilidadeEntregasAc) / matrizP[i][12] ) * (pedido * 30)
            #custo += (pPedido[pedido]*(pedido * 30)) * probabilidadeEntregasAc
            pedido-=1
            entrega-=1

        custo -= 10

        lineTotal += custo

        #print("Custo de ir do estado ",i," para o estado 12 :",custo)
        if(filial == 1):
            matrixC_F1[i][12] += custo
        else:
            matrixC_F2[i][12] += custo

def costMatrixBuilder_TrfXCarros():
    for linha in range(0,13):
        for coluna in range(0,12):
            if( (coluna <= 8) and ((coluna + 1) >= 9) ):
                matrixC_F1_C1_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+1)] - 7 + 10
                matrixC_F2_C1_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+1)] - 7 + 10
            else:
                matrixC_F1_C1_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+1)] - 7
                matrixC_F2_C1_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+1)] - 7

    for linha in range(0,13):
        for coluna in range(0,11):
            if( (coluna <= 8) and ((coluna + 2) >= 9) ):
                matrixC_F1_C2_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+2)] - 14 + 10
                matrixC_F2_C2_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+2)] - 14 + 10
            else:
                matrixC_F1_C2_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+2)] - 14
                matrixC_F2_C2_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+2)] - 14

    for linha in range(0,13):
        for coluna in range(0,10):
            if( (coluna <= 8) and ((coluna + 3) >= 9) ):
                matrixC_F1_C3_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+3)] - 21 + 10
                matrixC_F2_C3_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+3)] - 21 + 10
            else:
                matrixC_F1_C3_F2_F1[linha][coluna] = matrixC_F1[linha][(coluna+3)] - 21
                matrixC_F2_C3_F1_F2[linha][coluna] = matrixC_F2[linha][(coluna+3)] - 21

    for linha in range(0,13):
        matrixC_F1_C1_F2_F1[linha][12] = -10000
        matrixC_F2_C1_F1_F2[linha][12] = -10000
        matrixC_F1_C2_F2_F1[linha][12] = -10000
        matrixC_F2_C2_F1_F2[linha][12] = -10000
        matrixC_F1_C2_F2_F1[linha][11] = -10000
        matrixC_F2_C2_F1_F2[linha][11] = -10000
        matrixC_F1_C3_F2_F1[linha][12] = -10000
        matrixC_F2_C3_F1_F2[linha][12] = -10000
        matrixC_F1_C3_F2_F1[linha][11] = -10000
        matrixC_F2_C3_F1_F2[linha][11] = -10000
        matrixC_F1_C3_F2_F1[linha][10] = -10000
        matrixC_F2_C3_F1_F2[linha][10] = -10000

def costMatrixBuilder_RcbXCarros():
    for linha in range(0,13):
        for coluna in range(1,13):
            if( coluna >= 9 and (coluna-1) <= 8):
                matrixC_F1_C1_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-1)] - 10
                matrixC_F2_C1_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-1)] - 10
            else:
                matrixC_F1_C1_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-1)]
                matrixC_F2_C1_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-1)]

    for linha in range(0,13):
        for coluna in range(2,13):
            if( coluna >= 9 and (coluna-2) <= 8):
                matrixC_F1_C2_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-2)] - 10
                matrixC_F2_C2_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-2)] - 10
            else:
                matrixC_F1_C2_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-2)]
                matrixC_F2_C2_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-2)]

    for linha in range(0,13):
        for coluna in range(3,13):
            if( coluna >= 9 and (coluna-3) <= 8):
                matrixC_F1_C3_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-3)] - 10
                matrixC_F2_C3_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-3)] - 10
            else:
                matrixC_F1_C3_F2_F2[linha][coluna] = matrixC_F2[linha][(coluna-3)]
                matrixC_F2_C3_F1_F1[linha][coluna] = matrixC_F1[linha][(coluna-3)]

    for linha in range(0,13):
        matrixC_F1_C1_F2_F2[linha][0] = -10000
        matrixC_F2_C1_F1_F1[linha][0] = -10000
        matrixC_F1_C2_F2_F2[linha][0] = -10000
        matrixC_F2_C2_F1_F1[linha][0] = -10000
        matrixC_F1_C2_F2_F2[linha][1] = -10000
        matrixC_F2_C2_F1_F1[linha][1] = -10000
        matrixC_F1_C3_F2_F2[linha][0] = -10000
        matrixC_F2_C3_F1_F1[linha][0] = -10000
        matrixC_F1_C3_F2_F2[linha][1] = -10000
        matrixC_F2_C3_F1_F1[linha][1] = -10000
        matrixC_F1_C3_F2_F2[linha][2] = -10000
        matrixC_F2_C3_F1_F1[linha][2] = -10000

def calculateQ():
    for linha in range(169):
        for coluna in range(169):
            q0[linha][0] += matrixF1xF2[linha][coluna] * matrixC_F1xF2[linha][coluna]
            qF1_1_F2[linha][0] += matrixF1_C1_F2_F1xF2[linha][coluna] * matrixC_F1_C1_F2_F1xF2[linha][coluna]
            qF1_2_F2[linha][0] += matrixF1_C2_F2_F1xF2[linha][coluna] * matrixC_F1_C2_F2_F1xF2[linha][coluna]
            qF1_3_F2[linha][0] += matrixF1_C3_F2_F1xF2[linha][coluna] * matrixC_F1_C3_F2_F1xF2[linha][coluna]
            qF2_1_F1[linha][0] += matrixF2_C1_F1_F1xF2[linha][coluna] * matrixC_F2_C1_F1_F1xF2[linha][coluna]
            qF2_2_F1[linha][0] += matrixF2_C2_F1_F1xF2[linha][coluna] * matrixC_F2_C2_F1_F1xF2[linha][coluna]
            qF2_3_F1[linha][0] += matrixF2_C3_F1_F1xF2[linha][coluna] * matrixC_F2_C3_F1_F1xF2[linha][coluna]

def beginAlgoritmo(iteracoes,fnAnterior):

    if(iteracoes < itsAFazer):
        pnXfn = [[0.0 for h in range(1)] for o in range(169)]
        f1c1f2 = [[0.0 for h in range(1)] for o in range(169)]
        f1c2f2 = [[0.0 for h in range(1)] for o in range(169)]
        f1c3f2 = [[0.0 for h in range(1)] for o in range(169)]
        f2c1f1 = [[0.0 for h in range(1)] for o in range(169)]
        f2c2f1 = [[0.0 for h in range(1)] for o in range(169)]
        f2c3f1 = [[0.0 for h in range(1)] for o in range(169)]

        # VN = (Pn * FnAnterior) + Q
        vn = [[0.0 for h in range(1)] for o in range(169)]
        vnf1c1f2 = [[0.0 for h in range(1)] for o in range(169)]
        vnf1c2f2 = [[0.0 for h in range(1)] for o in range(169)]
        vnf1c3f2 = [[0.0 for h in range(1)] for o in range(169)]
        vnf2c1f1 = [[0.0 for h in range(1)] for o in range(169)]
        vnf2c2f1 = [[0.0 for h in range(1)] for o in range(169)]
        vnf2c3f1 = [[0.0 for h in range(1)] for o in range(169)]

        fn = [[0.0 for h in range(1)] for o in range(169)]

        for linha in range(169):
            somaLinha1, somaLinha2, somaLinha3, somaLinha4, somaLinha5, somaLinha6, somaLinha7 = 0,0,0,0,0,0,0

            for coluna in range(169):
                somaLinha1 += matrixF1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha2 += matrixF1_C1_F2_F1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha3 += matrixF1_C2_F2_F1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha4 += matrixF1_C3_F2_F1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha5 += matrixF2_C1_F1_F1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha6 += matrixF2_C2_F1_F1xF2[linha][coluna] * fnAnterior[coluna][0]
                somaLinha7 += matrixF2_C3_F1_F1xF2[linha][coluna] * fnAnterior[coluna][0]

            pnXfn[linha][0] = somaLinha1
            f1c1f2[linha][0] = somaLinha2
            f1c2f2[linha][0] = somaLinha3
            f1c3f2[linha][0] = somaLinha4
            f2c1f1[linha][0] = somaLinha5
            f2c2f1[linha][0] = somaLinha6
            f2c3f1[linha][0] = somaLinha7

        for linha in range(169):
            vn[linha][0] = pnXfn[linha][0] + q0[linha][0]
            vnf1c1f2[linha][0] = f1c1f2[linha][0] + qF1_1_F2[linha][0]
            vnf1c2f2[linha][0] = f1c2f2[linha][0] + qF1_2_F2[linha][0]
            vnf1c3f2[linha][0] = f1c3f2[linha][0] + qF1_3_F2[linha][0]
            vnf2c1f1[linha][0] = f2c1f1[linha][0] + qF2_1_F1[linha][0]
            vnf2c2f1[linha][0] = f2c2f1[linha][0] + qF2_2_F1[linha][0]
            vnf2c3f1[linha][0] = f2c3f1[linha][0] + qF2_3_F1[linha][0]

        for linha in range(169):
            fn[linha][0] = max(vn[linha][0],vnf1c1f2[linha][0],vnf1c2f2[linha][0],vnf1c3f2[linha][0],vnf2c1f1[linha][0],vnf2c2f1[linha][0],vnf2c3f1[linha][0])
            dn[linha][0] = fn[linha][0] - fnAnterior[linha][0]

            if(iteracoes == itsAFazer - 1):
                vns = [vn[linha][0],vnf1c1f2[linha][0],vnf1c2f2[linha][0],vnf1c3f2[linha][0],vnf2c1f1[linha][0],vnf2c2f1[linha][0],vnf2c3f1[linha][0]]
                vns.sort(reverse=True)
                for insert in range(7):
                    if(vns[insert] == vn[linha][0]):
                        politica[linha][insert] = 0
                    if(vns[insert] == vnf1c1f2[linha][0]):
                        politica[linha][insert] = 1
                    if(vns[insert] == vnf1c2f2[linha][0]):
                        politica[linha][insert] = 2
                    if(vns[insert] == vnf1c3f2[linha][0]):
                        politica[linha][insert] = 3
                    if(vns[insert] == vnf2c1f1[linha][0]):
                        politica[linha][insert] = 4
                    if(vns[insert] == vnf2c2f1[linha][0]):
                        politica[linha][insert] = 5
                    if(vns[insert] == vnf2c3f1[linha][0]):
                        politica[linha][insert] = 6

        iteracoes += 1
        beginAlgoritmo(iteracoes,fn)

def writeToExcell():
    workbook = xlsxwriter.Workbook('Matrizes.xlsx')
    resultado = workbook.add_worksheet("DN e Politca Optima")
    ws102 = workbook.add_worksheet("Matriz 0 transferencias")
    wsC102 = workbook.add_worksheet("Matriz de Contribuições")
    ws112 = workbook.add_worksheet("Matriz 1 transf de F1 para F2")
    wsC112 = workbook.add_worksheet("Matriz Contrib 1 Tr F1->F2")
    ws122 = workbook.add_worksheet("Matriz 2 transf de F1 para F2")
    wsC122 = workbook.add_worksheet("Matriz Contrib 2 Tr F1->F2")
    ws132 = workbook.add_worksheet("Matriz 3 transf de F1 para F2")
    wsC132 = workbook.add_worksheet("Matriz Contrib 3 Tr F1->F2")
    ws211 = workbook.add_worksheet("Matriz 1 transf de F2 para F1")
    wsC211 = workbook.add_worksheet("Matriz Contrib 1 Tr F2->F1")
    ws221 = workbook.add_worksheet("Matriz 2 transf de F2 para F1")
    wsC221 = workbook.add_worksheet("Matriz Contrib 2 Tr F2->F1")
    ws231 = workbook.add_worksheet("Matriz 3 transf de F2 para F1")
    wsC231 = workbook.add_worksheet("Matriz Contrib 3 Tr F2->F1")

    cell_format = workbook.add_format({'bold': True, 'bg_color': 'gray'})
    cell_format.set_align('center')
    cell_format2 = workbook.add_format({'bold': True, 'bg_color': 'gray'})
    cell_format2.set_align('right')
    cell_format3 = workbook.add_format({'bold': True, 'bg_color': 'gray'})
    cell_format3.set_align('left')

    f = 1
    for linha in range(13):
        for coluna in range(13):
            ws102.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws102.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws112.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws112.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws122.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws122.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws132.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws132.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws211.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws211.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws221.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws221.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws231.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            ws231.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)

            wsC102.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC102.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC112.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC112.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC122.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC122.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC132.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC132.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC211.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC211.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC221.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC221.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC231.write(f,0,'('+str(linha)+','+str(coluna)+')',cell_format)
            wsC231.write(0,f,'('+str(linha)+','+str(coluna)+')',cell_format)
            f+=1

    for linha in range(1,170):
        for coluna in range(1,170):
            ws102.write(linha,coluna,matrixF1xF2[linha-1][coluna-1])
            ws112.write(linha,coluna,matrixF1_C1_F2_F1xF2[linha-1][coluna-1])
            ws122.write(linha,coluna,matrixF1_C2_F2_F1xF2[linha-1][coluna-1])
            ws132.write(linha,coluna,matrixF1_C3_F2_F1xF2[linha-1][coluna-1])
            ws211.write(linha,coluna,matrixF2_C1_F1_F1xF2[linha-1][coluna-1])
            ws221.write(linha,coluna,matrixF2_C2_F1_F1xF2[linha-1][coluna-1])
            ws231.write(linha,coluna,matrixF2_C3_F1_F1xF2[linha-1][coluna-1])

            wsC102.write(linha,coluna,matrixC_F1xF2[linha-1][coluna-1])
            wsC112.write(linha,coluna,matrixC_F1_C1_F2_F1xF2[linha-1][coluna-1])
            wsC122.write(linha,coluna,matrixC_F1_C2_F2_F1xF2[linha-1][coluna-1])
            wsC132.write(linha,coluna,matrixC_F1_C3_F2_F1xF2[linha-1][coluna-1])
            wsC211.write(linha,coluna,matrixC_F2_C1_F1_F1xF2[linha-1][coluna-1])
            wsC221.write(linha,coluna,matrixC_F2_C2_F1_F1xF2[linha-1][coluna-1])
            wsC231.write(linha,coluna,matrixC_F2_C3_F1_F1xF2[linha-1][coluna-1])

    resultado.set_column('A:U',15)
    resultado.write(1,0,"DN = [",cell_format2)
    out = 0
    for divs in range(1,7):
        for linhas in range(1,28):
            resultado.write(linhas,divs,dn[out][0])
            out+=1
    resultado.write(1,7,dn[162][0])
    resultado.write(2,7,dn[163][0])
    resultado.write(3,7,dn[164][0])
    resultado.write(4,7,dn[165][0])
    resultado.write(5,7,dn[166][0])
    resultado.write(6,7,dn[167][0])
    resultado.write(7,7,dn[168][0])
    resultado.write(7,8,"].",cell_format3)

    resultado.write(1,9,"PO = [",cell_format2)
    out = 0
    for divs in range(1,7):
        for linhas in range(1,28):
            resultado.write(linhas,9+divs,str(politica[out]))
            out+=1
    resultado.write(1,16,str(politica[162]))
    resultado.write(2,16,str(politica[163]))
    resultado.write(3,16,str(politica[164]))
    resultado.write(4,16,str(politica[165]))
    resultado.write(5,16,str(politica[166]))
    resultado.write(6,16,str(politica[167]))
    resultado.write(7,16,str(politica[168]))
    resultado.write(7,17,"].",cell_format3)

# BEGIN PARSE #
matrixCalculator(1)
matrixCalculator(2)
#################################
costMatrixCalculator(1)
costMatrixCalculator(2)
#################################
matrixBuilder_TrfXCarros()
matrixBuilder_RcbXCarros()
#################################
costMatrixBuilder_TrfXCarros()
costMatrixBuilder_RcbXCarros()
#################################
bigMatrixCalculator()
#################################
fn0 = [[0.0 for h in range(1)] for o in range(169)]
calculateQ()
beginAlgoritmo(0,fn0)
#################################
writeToExcell()
# END PARSE #

print("---------------------------------------------------------------------------------------------------------------")
print(str(dn))
print("<------------------------------------------------------------------------------------------------------------->")
print(str(politica))
print("---------------------------------------------------------------------------------------------------------------")
