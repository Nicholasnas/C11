
def ler_dados():
    nome_completo = input("Entre com o seu nome: ")
    print(f"Nome Maiúscula: {nome_completo.upper()}")
    print(f"Nome Minúscula: {nome_completo.lower()}")
    nome_completo_sem_espaco = nome_completo.replace(" ", "")
    print(f"Quantidade de letras no nome: {len(nome_completo_sem_espaco)}")
    nome_completo_separado = nome_completo.split(" ")
    nome_completo_separado[-1] = "do Inatel"
    print(f"Nome completo alterado: {" ".join(nome_completo_separado)}")
    

def tabuada():
    print("TABUADA".center(50,"-"))
    number = int(input("Entre com um valor: "))
    start = int(input("Entre com o valor de inicio: "))
    end = int(input("Entre com o valor final: "))
    
    while start <= end:
        print(f"{number} X {start} = {number*start}")
        start += 1
    
    print("Fim".center(50, "-"))


def ler_pessoas():
    while True:
        sexo = input("Entre com o seu sexo(F-feminino ou M-masculino): " )
        if sexo in ['f',"F", "m", "M" ]:
            print("Entrada Correta - Fim")
            return
        print('Entrada inválida, tente novamente.')
        
if __name__ == "__main__":
    # ler_dados()
    # tabuada()
    ler_pessoas()