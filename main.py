# main.py
# Gravação das respostas em um arquivo CSV usando classes

import csv
from datetime import datetime

class Pesquisa:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.respostas = []
        self.cabecalho = ["Idade", "Gênero"] + perguntas + ["Data", "Hora"]

    def coletar_respostas(self):
        while True:
            print('_'*50)
            idade = input("Informe a idade (ou 00 para sair): ")
            if idade == "00":
                break
            
            nome = input('Informe seu nome: ')

            genero = input("Informe o gênero (1 - masculino, 2 - feminino, 3 - outro): ")

            respostas_perguntas = []
            for pergunta in self.perguntas:
                resposta = input(f"{pergunta}: ")
                respostas_perguntas.append(resposta)

            feedback = str(input('Gostaria de deixar alguma sugestão de melhoria na plataforma? '))
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # resposta = [nome, idade, genero] + respostas_perguntas + [data_hora]
            resposta = [nome, idade, genero] + respostas_perguntas + [feedback] + [data_hora]
            self.respostas.append(resposta)

    def gravar_respostas_csv(self):
        nome_arquivo = "respostas.csv"

        with open(nome_arquivo, "a", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            
            # Verificar se o arquivo está vazio
            arquivo_vazio = arquivo_csv.tell() == 0
            
            # Escrever o cabeçalho se o arquivo estiver vazio
            if arquivo_vazio:
                writer.writerow(self.cabecalho)

            # Adicionar as respostas
            writer.writerows(self.respostas)

        print("Respostas gravadas com sucesso no arquivo CSV.")

# Criação do objeto de pesquisa
perguntas = [
    "Qual é o seu modal de entrega? \n(1 - Carro, 2 - Moto ou 3 - Bicicleta)",
    
    "Você enfrenta dificuldades para encontrar endereços de entrega com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",

    "Você acredita que o valor pago pelas entregas é justo considerando seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",
    
    "Você considera o trabalho de entregador uma opção viável de renda com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",

    "Você recomendaria o trabalho de entregador para outras pessoas com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)"
]
pesquisa = Pesquisa(perguntas)

# Coleta das respostas
pesquisa.coletar_respostas()

# Gravação das respostas em um arquivo CSV
pesquisa.gravar_respostas_csv()

# Documentação
"""
Esse programa realiza uma pesquisa com 4 perguntas e grava as respostas em um arquivo CSV.
As perguntas são exibidas sequencialmente, e o usuário deve responder com 1 para Sim, 2 para Não, ou 3 para Não sei.
As respostas são gravadas em um arquivo CSV chamado 'respostas.csv'.
"""
