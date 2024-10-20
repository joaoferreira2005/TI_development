# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:53:25 2024

@author: joaot
"""

from scipy.io import wavfile
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

filename = "drumloop.wav"

[fs, data] = wavfile.read(filename) 
#fs -> frequencia de amostragem
#data -> valores do sinal
sd.play(data, fs) #reproduçao do som em frequencia normal
status = sd.wait()
sd.play(data, fs*2) #reproduçao do som com frequencia dupla
status = sd.wait()
sd.play(data, fs/2) #reproduçao do som com frequencia pela metade
status = sd.wait()

def apresentarInfo(nomeFicheiro, fs, nrBitsQuant):
    print(f"Nome: {nomeFicheiro}")
    print(f"Taxa de amostragem: {fs} kHz")
    print(f"Quantização: {nrBitsQuant}")

nrBitsQuant = data.itemsize * 8 #data.itemsize retorna bytes e é suposto ser convertido para bits
fskHz = fs/1000 #fs armazena a frequencia em Hz, sendo necessaria a conversão para kHz.
apresentarInfo(filename, fskHz, nrBitsQuant)

def visualizacaoGrafica(data, fs):
    NumAmostras = data.shape[0]  # Número de amostras
    Ts = 1 / fs  # Período de amostragem
    t = np.linspace(0, (NumAmostras - 1) * Ts, NumAmostras)  # Eixo do tempo

    # Normalizar o sinal para estar no intervalo [-1, +1]
    data_norm = data / np.max(np.abs(data))

    if len(data.shape) == 1:
        # Caso mono (um único canal)
        plt.figure(figsize=(10, 6))
        plt.plot(t, data_norm)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Amplitude Normalizada')
        plt.title('Sinal de Áudio Monoaural')
        plt.grid(True)
        plt.show()
    
    elif len(data.shape) == 2:
        # Caso estéreo (dois canais)
        canal_esquerdo = data_norm[:, 0]
        canal_direito = data_norm[:, 1]
        
        fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        # Canal esquerdo
        axs[0].plot(t, canal_esquerdo)
        axs[0].set_ylabel('Amplitude Normalizada')
        axs[0].set_title('Canal Esquerdo')
        axs[0].grid(True)

        # Canal direito
        axs[1].plot(t, canal_direito)
        axs[1].set_xlabel('Tempo (s)')
        axs[1].set_ylabel('Amplitude Normalizada')
        axs[1].set_title('Canal Direito')
        axs[1].grid(True)

        plt.tight_layout()
        plt.show()
        
visualizacaoGrafica(data, fs)