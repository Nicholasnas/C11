


def exercicio_1():
    classificacao = ['palmeiras', 'flamengo', 'cruzeiro', 'fluminense', 'barcelona']

    print(f'Três primeiros colocados: {classificacao[:3]}')
    print(f"Os ultimos dois colocados: {classificacao[3:]}")
    print(f'Lista em ordem alfabetica: {sorted(classificacao)}')
    print(f'posição do time barcelona: {classificacao.index('barcelona')}')


def exercicio_2():
    loja1 = {'iphone 15','poco x7' , 'sansung a10', 'moto g32'}
    loja2 = {'iphone 12', 'poco x7', 'poco x7 pro'}
    
    print('Loja 1: ', loja1)
    print('Loja 2: ', loja2)
    print(f'Modelos na loja 1: {len(loja1)}')
    print(f'Modelos na loja 2: {len(loja2)}')
    
    print(f"modelos nas duas lojas: {loja1 | loja2} ")
    
def exercicio3():
    nome = input("Entre com o seu nome: ")
    media = float(input("Entre com a sua média: "))
    
    dados= dict()
    dados['nome'] = nome
    dados['media'] = media
    dados['situacao'] = 'AP' if media >= 50 else "RP"
    
    print(f'Dados do aluno: {dados}', )


def exercicio4():
    pessoas = list()
    
    for i in range(3):
        pessoa = dict()
        nome = input(f"Entre com o nome da pessoa {i + 1}: ")
        peso = float(input(f"Entre com o peso da pessoa {i + 1}: "))
        
        pessoa['nome'] = nome
        pessoa['peso'] = peso
        pessoas.append(pessoa)
    
    pessoas.sort(key=lambda pessoa: pessoa['peso'])
    print(f"Pessoa mais pesada: {pessoas[-1]} ")
    print(f"Pessoa mais leve: {pessoas[0]} ")
    


def exercicio5():
    pessoas = []
    media_idade = 0 
    quantidade_de_pessoas = int(input("Quantas pessoas no grupo? "))
    mulheres_com_idade_menor_que_20 = 0
    
    i = 0
    while i < quantidade_de_pessoas:
        pessoa = {}
        
        nome = input("Entre com o seu nome: ")
        idade = int(input("Entre com a sua idade: "))
        sexo = input("Entre com o sexo(M ou F): ")
        
        media_idade += idade
        pessoa['nome'] = nome
        pessoa['idade'] = idade
        pessoa['sexo'] = sexo
        pessoas.append(pessoa)
        i += 1
    
    for pessoa in pessoas:
        if pessoa['sexo'] == 'F' and pessoa['idade'] < 20:
            mulheres_com_idade_menor_que_20 += 1
        
    print("A idade média do grupo: ", media_idade/quantidade_de_pessoas )
    print("Quantidade de mulheres com menos de 20 anos: ", mulheres_com_idade_menor_que_20)
          
        

if __name__ == "__main__":
    # exercicio_1()
    # print('-'*100)
    # exercicio_2()
    # print('-'*100)
    # exercicio3()
    # print('-'*100)
    # exercicio4()
    # print('-'*100)
    exercicio5()
    