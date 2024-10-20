#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:35:44 2024

@author: louis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    #EXERCICIO 1
    
    #Exercicio 1 - a
    data = pd.read_excel('C:\\Users\\João Ferreira\\Desktop\\Documentos\\Universidade\\2º Ano\\TI\\TP1\\CarDataSet.xlsx')
    
    #Exercicio 1 - b
    array1 = data.values
    
    #Exercicio 1 - c
    varNames = data.columns.values.tolist()
    
    
    #EXERCICIO 2 
    grafico_scatter(array1,varNames)   
        
        
    #EXERCICIO 3
    new_data = data.astype('uint16')                                # Muda tipo de int para uint16 (unsigned int 16 bits)
    dicionario = {}                                                 # Iniciliazar o dicionário para guardar o alfabeto
    
    for variavel in new_data:                                       # Percorrer todos os valores das variáveis 
            alfabeto = np.unique(new_data[variavel])                # Evitar valores repetidos
            dicionario[variavel] = alfabeto                         # Adicionar o alfabeto ao dicionário               
                                                                    
    #EXERCICIO 4
    nomes = {}
    
    for col in data:                                                # A variavel coluna vai ser o nome das seis variaveis
        nomes = num_ocorrencia(data[col],col,nomes)
   
    #EXERCICIO 5
    grafico_barras(nomes)
    
    #EXERCICIO 6
    
    i = 0                               # Variável para saber que coluna está a ser percorrida
    for coluna in data:                 # coluna = "nome da variáveis" (Ex: Weight)
        nomes = {}
        if coluna == 'Weight':
            steps = 40                      
            data_binned = binning (array1[:,i],steps,coluna)
            nomes = num_ocorrencia(data_binned,coluna,nomes)
            grafico_barras(nomes)
        elif (coluna == 'Horsepower' or coluna == 'Displacement'):
            steps = 5
            data_binned = binning (array1[:,i],steps,coluna)
            nomes = num_ocorrencia(data_binned,coluna,nomes)
            grafico_barras(nomes)
        i += 1                          # Incrementa
        
    #Exercicio 7
    #np.average(var(x),Weight=p) variancia ponderada valor medio var(x) = E((x-u)^2) 🔥
        
    
#EXERCICIO 2

def grafico_scatter(array1,varNames):
    mpg = array1[:,6]
    for i in range (6):
        plt.subplot(3,2,i+1)                                        # Mostra os seis graficos juntos (colunas 3, linhas 2, i +1 posição das matrizes)
        variaveis = array1[:,i]                                     # Variaveis 
        plt.ylabel(varNames[6], size = 9)                           # Titulo em y
        plt.xlabel(varNames[i], size = 9)                           # Titulo em x
        plt.title(varNames[6]+ " vs " + varNames[i], size = 9)      # Titulo
        plt.scatter(variaveis,mpg,color = '#BF00BF',s = 2)          # Scatter faz grafico discreto, e muda cor
        plt.tight_layout()       
    
    
#EXERCICIO 4

def num_ocorrencia(data,col,nomes):
    ocorrencias_data = {}
    for value in data:                                              # Este for percorre para cada uma das 6 e concede a value o valor de todos os numeros
        if value in ocorrencias_data:                               # Verifica se a chave esxiste
            ocorrencias_data[value] += 1                            # Se existir aumenta um valor
        else:
            ocorrencias_data[value] = 1                             # Se nao existir inicializa
    nomes[col] = ocorrencias_data

    return nomes                                                    # Retorna o dicionario

#EXERCICIO 5

def grafico_barras(nomes):
    
    for variavel, count in nomes.items():
        # Convertendo o dicionário para um DataFrame do pandas
        df = pd.DataFrame(list(count.items()), columns=['xlabel', 'ylabel'])    
        df = df.sort_values(by='xlabel')
    
        # Convertendo as colunas para string usando astype
        df['xlabel'] = df['xlabel'].astype(str)
        df['ylabel'] = df['ylabel'].astype(str)

        # Criando o gráfico de barras
        plt.figure()
        plt.title(f"{variavel} vs Count", size=9)
        plt.bar(df['xlabel'], df['ylabel'].astype(int), color='#D62728')        # ylabel deve ser int para o gráfico
        plt.xticks(rotation = 90, size = 7)
        plt.yticks(size = 7)
    # Exibindo o gráfico
    plt.show()
    
#EXERCICIO 6

def binning(data,intervalo,coluna):
    # Encontra o valor mínimo e o valor máximo do array de dados
    min_valor = np.min(data)
    min_valor -= (min_valor % intervalo)                                                    # Valor mínimo do array
    max_valor = np.max(data)   
                                                 # Valor máximo do array
    intervalo_bin = (max_valor - min_valor) / intervalo                         # Comprimento do intervalo
    intervalo_bin = intervalo_bin.astype(int)
    
    for i in range (intervalo_bin):                                                                  
        values_final = 0                                                        # Armazena a chave do valor com maior ocorrências
        
        if i == intervalo_bin - 1:                                                  # Para o último bin, incluímos o valor máximo
            dataRedux = data[data >= i*intervalo + min_valor]
            dataRedux = dataRedux[dataRedux <= max_valor]                       # Inclui o valor máximo
        else:
            dataRedux = data[data >= i*intervalo + min_valor]
            dataRedux = dataRedux[dataRedux < (1+i)*intervalo + min_valor]  # Não inclui o valor máximo aqui
        
        if len(dataRedux) > 0:
            nomes = {}                                                              # Inicializa dicionário
            nomes = num_ocorrencia(dataRedux.astype('uint16'),coluna,nomes)         
        
            valores = np.array(list(nomes[coluna].values()))
            chaves = np.array(list(nomes[coluna].keys()))

            # Índice do valor máximo
            indice_max = np.argmax(valores)

            # Valor com maior ocorrência no intervalo
            values_final = chaves[indice_max]                                           # Atualiza a chave do valor com maior ocorrências
              
            # Transforma os valores que pertencem ao intervalo no valor com maior ocorrência desse intervalo        
            if i == intervalo_bin - 1:                                                                                                                                                        
                data = np.where((data >= i*intervalo + min_valor) & (data <= max_valor), values_final, data)    
            else:
                data = np.where((data >= i*intervalo + min_valor) & (data < (1+i)*intervalo + min_valor), values_final, data)
    print(data)
    return data
        

if __name__ == "__main__":
    main()
    
    
""" 
--- Comentários exercicio 2:
Nota: *Acceleration = aceleração do carro; *Cylinder = nº de cilindros do motor; 
      *Displacement = deslocamento ou volume de ar descarregado por curso do pistão; 
      *Horsepower= cavalos de potência ; *ModelYear = ano de fabrico;
      *Weight = peso do carro; *MPG = rendimento do combustíve;
  
    
MPG vs Acceleration: O gráfico mostra que não há uma correlação clara entre a 
aceleração e o rendimento do combustivél, visto que para os mesmo valores de 
acelaração o MPG pode apresentar valores muito diferentes. 
    
MPG vs Cylinders: O gráfico mostra que quanto maior é o nº de cilindros do 
motor pior será o rendimento do combustivél, ou seja, mais combustivél será
consumido.
      
MPG vs Displacement: O gráfico mostra que quanto maior o displacement for, pior
será o rendimento do combustivél, o MPG e o Displacement apresentão ser 
inversamente proporcinais.  

MPG vs Horsepower: O gráfico mostra que quanto maior for a potência, pior será 
o redimento do combustivél. Logo MPG e Horsepower também são inversamente
proporcionais  
    
MPG vs ModelYear: O gráfico mostra que carros com o ano de fabrico mais recente
têm valores mais altos de MPG, ou seja, segundo o gráfico modelos mais novos
consomem menos combustivél.
    
MPG vs Weight: O gráfico mostra que quanto maior o peso do carro for, pior
será o rendimento do combustivél, o MPG e o Weight mostram ser 
inversamente proporcinais.
    
"""