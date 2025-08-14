
def viagens():
    distancia = float(input("Qual a distância percorrida pelo carro em Km: "))
    
    if distancia < 200:
        print(f"O preço da passagem é {distancia * 0.5}")
    else:
        print(f"O preço da passagem é {distancia * 0.45}")


def separar_casas():
    
    numero = int(input("Entre um número entre 1000 e 9999: "))

    if 1000 <= numero <= 9999:
        unidade = numero % 10
        dezena = numero // 10 % 10
        centena = numero // 100 % 10
        milhar = numero // 1000

        print("Unidade: ", unidade)
        print("Dezena: ", dezena)
        print("Centena: ", centena)
        print("Milhar: ", milhar)
    else:
        print("Número fora do intervalo!")



def verificar_numero():
    import math
    number =  float(input("Entre um número decimal: "))

    print(f"Raiz quadrada: {math.sqrt(number):.2f} ")
    print(f"Funcao teto: {math.ceil(number)} ")
    print(f"Funcao chao: {math.floor(number)} ")
    print(f"Parte inteira: {int(number)} ")
                
            


if __name__ == "__main__":
    # viagens()
    # separar_casas()
    verificar_numero()
    