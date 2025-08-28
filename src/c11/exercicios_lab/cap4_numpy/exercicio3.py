
from random import randint
import numpy as np

# Atividade 3

df = np.loadtxt('/home/nkk/Área de trabalho/projetos/C11/space.csv', delimiter=';', dtype=str, encoding='utf-8')


# 1 porcentagem de missos bem sucedidas
def atividade1():
        
    status = df[1:,7]
    total = len(status)
    sucessos = np.sum(status == 'Success')
    porcentagem = (sucessos/total) * 100
    
    print(f"Porcentagens de missoes bem sucedidas: {porcentagem:.2f}%")

def atividade2():
    # Media de gastos por missao
    custos = df[1:, 6]
    custos = custos.astype(float)

    custos_validos = custos[custos > 0]
    media = np.mean(custos_validos)

    print(f"Media de gastos por lancamento: {media:.2f}")
    
    
def atividade3():
    # Missoes lancadas pelo os EUA
    local = df[1:, 2]
    missoes_eua = np.sum(np.char.find(local, "USA") >= 0)

    print(f"Quantidade de missoes lancadas nos USA: {missoes_eua}")


def atividade4():
    lacamentos = df[1:,1]
    custos = df[1:,6]

    spacex = custos[lacamentos == "SpaceX"].astype(float)
    indice_maior_custo = np.argmax(spacex)
    
    missao = df[1:,:][lacamentos == "SpaceX"][indice_maior_custo]
    print(f"Missao mais cara da spaceX {missao}")
    
def atividade5():
    empresas = df[1:, 1]
    unicas, contagens = np.unique(empresas, return_counts=True)

    for empresa, contagens in zip(unicas, contagens):
        print(f"{empresa}: {contagens} missões")


if __name__ == "__main__":
    atividade1()
    atividade2()
    atividade3()
    atividade4()
    atividade5()
    
    


    
    