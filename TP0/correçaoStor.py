import scipy.io.wavfile as wav
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

def apresentarInfo(filename, fs, nrBitsQuant):
    print("Informações do ficheiro")
    print("Nome: %s" % filename)
    print("Taxa de amostragem: %.1f kHz" % (fs/1000))
    print("Quantização: %d bits" % nrBitsQuant)

def visualizaçaoGrafica(data, fs):
    [nl, nc] = data.shape

    #tempo = np.arange(0, nl/fs, 1/fs)
    tempo = np.linspace(0, nl/fs, nl)

    nb = data.itemsize * 8
    dataN = data / (2 ** (nb-1))

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(tempo[1000:1020], dataN[1000:1020, 0], tempo[1000:1020], dataN[1000:1020, 1])
    plt.xlabel('Tempo [s]')
    plt.ylabel('Amplitude [-1:1]')
    plt.title('Canal Esquerdo')
    plt.subplots_adjust(hspace=1)

    plt.subplot(2, 1, 2)
    plt.plot(tempo[1000:1020], dataN[1000:1020, 1], "og")
    plt.xlabel('Tempo [s]')
    plt.ylabel('Amplitude [-1:1]')
    plt.title('Canal Direito')
    plt.show()

def main():
    #read audio file
    path = "C:\\Users\\joaot\\Desktop\\Documentos\\Universidade\\2º Ano\\TI\\TP0\\"
    fName = "drumloop.wav"
    [fs, data] = wav.read(path+fName)
    
    # print(fs)
    # print(data.shape) #(Numero de linhas, numero de colunas)
    # print(data.dtype) #Tipo dos elementos no array
    # print(data.max()) #Valor maximo
    # print(data.min()) #Valor minimo
    
    #play file
    # sd.play(data,fs, blocking=true) #forma mais generica
    # print("aaa")

    #apresentar info do ficheiro
    nb = data.itemsize * 8
    apresentarInfo(fName, fs, nb)

    #Visualizar ondas sonoras
    visualizaçaoGrafica(data, fs)

if __name__ == "__main__":
    main()
