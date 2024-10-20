import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#2 # colocar ciclo for

def visualizacaoGrafica(dataNP, n_linhas,n_colunas, x_posicao, y_posicao, categorias):

    plt.subplot(n_linhas, n_colunas, x_posicao + 1)
    plt.plot(dataNP[:, x_posicao], dataNP[:, y_posicao], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel(categorias[x_posicao])
    plt.ylabel(categorias[y_posicao])
    plt.title(f"{categorias[x_posicao]} VS {categorias[y_posicao]}")


# 3)

def define_alfabeto(data_uint16):

    dic = {}

    for coluna in data_uint16:

        alfabeto = np.unique(data_uint16[coluna])
        dic[coluna] = alfabeto

    return dic

#4
def contar_ocorrencias_por_simbolo(data, coluna):
    ocorrencias = {}
    for coluna in data.columns:
        ocorrencias_simbolos = {}
        for value in data[coluna]:
            if value in ocorrencias_simbolos:
                ocorrencias_simbolos[value] += 1
            else:
                ocorrencias_simbolos[value] = 1
        ocorrencias[coluna] = ocorrencias_simbolos
    return ocorrencias

#5

def grafico_barras(ocorrencias, alfabeto):


        #print("GRAFICO BARRAS INNIT")
        

        #print(alfabeto["Displacement"])


        for categoria in ocorrencias:
            plt.figure()
            contagem_de_ocorrencias = ocorrencias[categoria]
            simbolos = alfabeto[categoria]

            plt.subplot()

            plt.bar(simbolos.astype(str), contagem_de_ocorrencias, color = "red")

            plt.ylabel("Count")
            plt.xlabel(categoria)
            #plt.show()

        #print("GRAFICO BARRAS END")


def main():
    path = "C:\\Users\\João Ferreira\\Desktop\\Documentos\\Universidade\\2º Ano\\TI\\TP1\\Semana 1\\"
    data = pd.read_excel(path+'CarDataset.xlsx')

    #1)

    varNames = data.columns.values.tolist()  # Lista com o nome das variáveis
    dataNP = data.values  # Retorna os valores do dataFrame.

    #

    # varNames é um vetor que contem as categorias

    plt.figure()

    for i in range(0,6):
        visualizacaoGrafica(dataNP,3,2,i,6,varNames)

    plt.subplots_adjust(hspace = 1.5, wspace=0.5) #Espaçamento entre gráficos
    #plt.show()


    #3

    # Conversão do dataframe para uint16
    data_uint16 = data.astype('uint16')
    alfabeto = define_alfabeto(data_uint16)
    print("ALFABETO INNIT\n")
   # print(alfabeto) # Perguntar ao stor se é tudo junto (codigo do joao) ou como está agora
    print("ALFABETO END\n")
    #4

    resultado_ocorrencias = contar_ocorrencias_por_simbolo(data_uint16, alfabeto)  # Variável que armazenará o dicionario de resultados da contagem

    grafico_barras(resultado_ocorrencias, alfabeto)
    plt.show()
    #print(resultado_ocorrencias)
    #print(resultado_ocorrencias["MPG"])  # Imprime o número de ocorrências de cada valor de MPG


if __name__ == "__main__":
    main()

'''
Pergunta 2.4
MPG vs. Acceleration (Aceleração):
Segundo os dados quanto maior a aceleração melhor é o rendimento de combustivel (estranho). Apesar de haver uma grande dispersão e a correlação não seja muito forte

MPG vs. Cylinders (Número de cilindros):
Os carros com 4 cilindros têm um MPG maior, enquanto carros com 6/8 cilindros tem um pior rendimento de combustível

MPG vs. Displacement (Deslocamento):
A relação entre MPG e o deslocamento é inversamente proporcional. Isto é lógico uma vez que motores com maior deslocamento consomem mais combustível logo menos MPG.


 MPG vs. Horsepower (Cavalos de potência):
A relação entre MPG e a potência é inversamente proporcional. Ou seja, quanto mais potente o veículo maior o seu consumo de combustível

MPG vs. Model Year (Ano do modelo):
Os carros mais recentes tem um maior MPG. Isto significa que os carros mais novos tendem a ser mais eficientes no consumo de combustível (provavelmente devido a avanços tecnológicos ou leis ambientais rigorosas)

 MPG vs. Weight (Peso):
A relação entre MPG e o peso é inversamente proporcional.
Esta relação é trivial uma vez que quanto maior o peso de um carro mais combustível é necessário para o mover.

'''
# Nao posso usar a np.var para fazer a variancia ponderada