import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Users\\João Ferreira\\Desktop\\Documentos\\Universidade\\2º Ano\\TI\\TP1\\Semana 1\\' #Usar 2 barras para separar as pastas (utilizei VSCode)
data = pd.read_excel(path+'CarDataset.xlsx')

varNames=data.columns.values.tolist() #Lista com o nome das variáveis
dataNP = data.values #Retorna os valores do dataFrame.

#Conversão do dataframe para uint16
data_uint16 = data.astype('uint16')
#Gerar um array com as ocorrências de valores ao longo de todas as colunas
alfabeto = np.unique(data_uint16.values)



def visualizaçaoGrafica(dataNP):
    #MPG vs. Acceleration graphic
    plt.figure()
    plt.subplot(3, 2, 1)
    plt.plot(dataNP[:, 0], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Acceleration')
    plt.ylabel('MPG')
    plt.title('MPG vs. Acceleration')
    plt.subplots_adjust(hspace = 1.5, wspace=0.5) #Espaçamento entre gráficos

    #MPG vs. Cylinders graphic
    plt.subplot(3, 2, 2)
    plt.plot(dataNP[:, 1], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Cylinders')
    plt.ylabel('MPG')
    plt.title('MPG vs. Cylinders')

    #MPG vs. Displacement
    plt.subplot(3, 2, 3)
    plt.plot(dataNP[:, 2], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Displacement')
    plt.ylabel('MPG')
    plt.title('MPG vs. Displacement')

    #MPG vs. Horsepower
    plt.subplot(3, 2, 4)
    plt.plot(dataNP[:, 3], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Horsepower')
    plt.ylabel('MPG')
    plt.title('MPG vs. Horsepower')

    #MPG vs. Model Year
    plt.subplot(3, 2, 5)
    plt.plot(dataNP[:, 4], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Model Year')
    plt.ylabel('MPG')
    plt.title('MPG vs. Model Year')

    #MPG vs. Weight
    plt.subplot(3, 2, 6)
    plt.plot(dataNP[:, 5], dataNP[:,6], "*m", markersize=3) #Asterisco magenta de tamanho 3
    plt.xlabel('Weight')
    plt.ylabel('MPG')
    plt.title('MPG vs. Weight')
    
    plt.show()


def contar_ocorrencias_por_simbolo(data):
    resultados = {} #Dicionário onde serão armazenados os resultados da contagem
    for coluna in data.columns: #É percorrida cada coluna individualmente
        ocorrencias = data[coluna].value_counts().sort_index() 
        #Em cada coluna, será contado a ocorrência de cada valor (value_counts()) 
        #e será organizado por ordem crescente sempre que o index de contagens for números(sort_index())
        resultados[coluna] = ocorrencias #É armazenado o resultado no dicionário
    return resultados

def main():
    visualizaçaoGrafica(dataNP) #Visualização gráfica
    print(alfabeto) #Impressão do alfabeto
    resultado_ocorrencias = contar_ocorrencias_por_simbolo(data_uint16) #Variável que armazenará o dicionario de resultados da contagem
    print(resultado_ocorrencias["MPG"]) #Imprime o número de ocorrências de cada valor de MPG

if __name__ == "__main__":
    main()

