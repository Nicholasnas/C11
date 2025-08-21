# Exercicio 3 - Campo minado
from random import randint
import numpy as np


matriz = np.zeros((2,2))

number_linha = randint(0,1)
number_coluna = randint(0,1)

matriz[number_linha][number_coluna] = 1

print('bomba na posição: ', number_linha, number_coluna)

jogadas = 3
acertos = 0

while jogadas > 0:
    print("Selecione um posição da matriz: ")
    linha = int(input("Entre com a linha ( 0 ou 1): "))
    coluna = int(input("Entre com a coluna ( 0 ou 1): "))
    
    if matriz[linha][coluna] == 0:
        print("Correto acertou uma posição!".center(50,'-'))
        matriz[linha][coluna] = 2 # local descoberto
        
        acertos += 1
        if acertos == 3:
            print("Congratulations! You beat the game!")
            break
        
    elif matriz[linha][coluna] == 2:
        print("posição já escolhida")
        continue
    
    else:
        print("Game Over! :( Try Again! ")
        break   
        
    jogadas -= 1
            
    
    
    
    