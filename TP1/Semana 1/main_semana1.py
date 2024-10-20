import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#2
def visualizaçaoGrafica(dataNP):

    # MPG vs. Acceleration graphic
    plt.figure()
    plt.subplot(3, 2, 1)
    plt.plot(dataNP[:, 0], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Acceleration')
    plt.ylabel('MPG')
    plt.title('MPG vs. Acceleration')
    plt.subplots_adjust(hspace=1.5, wspace=0.5)  # Espaçamento entre gráficos

    # MPG vs. Cylinders graphic
    plt.subplot(3, 2, 2)
    plt.plot(dataNP[:, 1], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Cylinders')
    plt.ylabel('MPG')
    plt.title('MPG vs. Cylinders')

    # MPG vs. Displacement
    plt.subplot(3, 2, 3)
    plt.plot(dataNP[:, 2], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Displacement')
    plt.ylabel('MPG')
    plt.title('MPG vs. Displacement')

    # MPG vs. Horsepower
    plt.subplot(3, 2, 4)
    plt.plot(dataNP[:, 3], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Horsepower')
    plt.ylabel('MPG')
    plt.title('MPG vs. Horsepower')

    # MPG vs. Model Year
    plt.subplot(3, 2, 5)
    plt.plot(dataNP[:, 4], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Model Year')
    plt.ylabel('MPG')
    plt.title('MPG vs. Model Year')

    # MPG vs. Weight
    plt.subplot(3, 2, 6)
    plt.plot(dataNP[:, 5], dataNP[:, 6], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel('Weight')
    plt.ylabel('MPG')
    plt.title('MPG vs. Weight')

    plt.show()

# 3)
def define_alfabeto(data_uint16):

    dic = {}

    for coluna in data_uint16:

        alfabeto = np.unique(data_uint16[coluna])
        dic[coluna] = alfabeto

    return dic

#4
def contar_ocorrencias_por_simbolo(data):

    dic = {}  # Dicionário onde serão armazenados os resultados da contagem

    for coluna in data.columns:  # Vai aceder a cada categoria do carro

        # a linha de codigo é autoexplicativa

        ocorrencias = data[coluna].value_counts().sort_index()

        # Em cada coluna, será contado a ocorrência de cada valor (value_counts())
        # e será organizado por ordem crescente sempre que o index de contagens for números(sort_index())

        dic[coluna] = ocorrencias  # É armazenado o resultado no dicionário

    return dic

def main():

    data = pd.read_excel('CarDataset.xlsx')

    #1)

    varNames = data.columns.values.tolist()  # Lista com o nome das variáveis
    dataNP = data.values  # Retorna os valores do dataFrame.

    # 2
    visualizaçaoGrafica(dataNP)  # Visualização gráfica

    #3

    # Gerar um array com as ocorrências de valores ao longo de todas as colunas
    #alfabeto = np.unique(data_uint16.values)
    #print(alfabeto)  # Impressão do alfabeto

    # Conversão do dataframe para uint16
    data_uint16 = data.astype('uint16')
    alfabeto = define_alfabeto(data_uint16)
    print(alfabeto) # Perguntar ao stor se é tudo junto (codigo do joao) ou como está agora

    #4
    resultado_ocorrencias = contar_ocorrencias_por_simbolo(data_uint16)  # Variável que armazenará o dicionario de resultados da contagem

    print(resultado_ocorrencias["MPG"])  # Imprime o número de ocorrências de cada valor de MPG


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