import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
######################################################################################################################################################################################
#2 # colocar ciclo for

def visualizacaoGrafica(dataNP, n_linhas,n_colunas, x_posicao, y_posicao, categorias):

    plt.subplot(n_linhas, n_colunas, x_posicao + 1)
    plt.plot(dataNP[:, x_posicao], dataNP[:, y_posicao], "*m", markersize=3)  # Asterisco magenta de tamanho 3
    plt.xlabel(categorias[x_posicao])
    plt.ylabel(categorias[y_posicao])
    plt.title(f"{categorias[x_posicao]} VS {categorias[y_posicao]}")

######################################################################################################################################################################################
# 3)

def define_alfabeto(data_uint16):

    dic = {}

    for coluna in data_uint16:

        alfabeto = np.unique(data_uint16[coluna])
        dic[coluna] = alfabeto

    return dic

######################################################################################################################################################################################
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

######################################################################################################################################################################################
#5

# Função para criar gráfico de barras
def grafico_barras(categoria, xlabel, ocorrencias, alfabeto):
        
        contagem_de_ocorrencias = ocorrencias[categoria]
        simbolos = alfabeto[categoria]

        simbolos_sorted = sorted(simbolos)
        contagens_sorted = [] 
        for simbolo in simbolos_sorted:
            if simbolo in contagem_de_ocorrencias:
                contagens_sorted.append(contagem_de_ocorrencias[simbolo])

        plt.figure()
        plt.title(f"{categoria} vs Count", size=9)
        plt.bar(list(map(str, simbolos_sorted)), contagens_sorted, color='#D62728')
        plt.xticks(rotation = 90, size = 6)
        plt.yticks(size = 6)
        
        plt.ylabel("Count")
        plt.xlabel(xlabel)

################################################################################################################################################################################################################
#6

def simple_binning(data, bin_size):
    min_val = data.min()
    max_val = data.max()
    bins = np.arange(min_val, max_val + bin_size, bin_size)
    bin_labels = np.digitize(data, bins) - 1  # Bin indices start from 0

    # Use the most common value in each bin without `value_counts`
    bin_means = []
    for i in range(len(bins) - 1):
        bin_vals = data[(data >= bins[i]) & (data < bins[i + 1])]
        if len(bin_vals) > 0:
            counts = {}
            for val in bin_vals:
                counts[val] = counts.get(val, 0) + 1
            most_common = max(counts, key=counts.get)
            bin_means.append(most_common)
        else:
            bin_means.append(0)  # Just in case there's an empty bin
    
    binned_data = np.array([bin_means[i] if i < len(bin_means) else max_val for i in bin_labels])
    
    return binned_data


def contar_ocorrencias(categoria, lista):
    ocorrencias = {}
    ocorrencias_simbolos = {}

    for value in lista:
        if value in ocorrencias_simbolos:
            ocorrencias_simbolos[value] += 1
        else:
            ocorrencias_simbolos[value] = 1

    ocorrencias[categoria] = ocorrencias_simbolos
    return ocorrencias

def define_alfabeto_binned(categoria, binned_data):
    dic = {}
    for elemento in binned_data:

        alfabeto = np.unique(binned_data)
        dic[categoria] = alfabeto

    return dic

################################################################################################################################################################################################################

def main():
    path = "C:\\Users\\João Ferreira\\Desktop\\Documentos\\Universidade\\2º Ano\\TI\\TP1\\"
    data = pd.read_excel(path+'CarDataset.xlsx')

    #1)

    varNames = data.columns.values.tolist()  # Lista com o nome das variáveis
    dataNP = data.values  # Retorna os valores do dataFrame.

    # varNames é um vetor que contem as categorias

    plt.figure()

    for i in range(0,6):
        visualizacaoGrafica(dataNP,3,2,i,6,varNames)

    plt.subplots_adjust(hspace = 1.5, wspace=0.5) #Espaçamento entre gráficos


    #3
    # Conversão do dataframe para uint16
    
    data_uint16 = data.astype('uint16')
    alfabeto = define_alfabeto(data_uint16)
    
    #4

    resultado_ocorrencias = contar_ocorrencias_por_simbolo(data_uint16, alfabeto)  # Variável que armazenará o dicionario de resultados da contagem
    
    grafico_barras("Weight", "Não binado - Weight", resultado_ocorrencias, alfabeto)
    grafico_barras("Displacement", "Não binado - Displacement", resultado_ocorrencias, alfabeto)

    binned_varNames = ["Weight", "Displacement", "Horsepower"]

    for varName in binned_varNames:
        bin_size = 40 if varName == "Weight" else 5
        binned_list = simple_binning(data_uint16[varName], bin_size)
        ocorrencias_binned = contar_ocorrencias(varName, binned_list)
        alfabeto_binned = define_alfabeto_binned(varName, binned_list)
        grafico_barras(varName, "Binado - " + varName, ocorrencias_binned, alfabeto_binned)

    plt.show()
    
    

    plt.show()



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

