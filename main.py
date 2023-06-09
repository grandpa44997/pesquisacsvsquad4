# main.py
# Gravação das respostas em um arquivo CSV usando classes

import csv
from datetime import datetime

class Pesquisa:
    def __init__(self, perguntas):
        # Inicialização da classe Pesquisa com as perguntas e uma lista vazia de respostas
        self.perguntas = perguntas
        self.respostas = []
        self.cabecalho = ["Idade", "Gênero"] + perguntas + ["Data", "Hora"]

    def coletar_respostas(self):
        while True:
            print('_'*50)
            # Solicitação da idade e verificação para sair do loop
            idade = input("Informe a idade (ou 00 para sair): ")
            if idade == "00":
                break
            
            # Solicitação do nome
            nome = input('Informe seu nome: ')

            # Solicitação do gênero
            genero = input("Informe o gênero (1 - masculino, 2 - feminino, 3 - outro): ")

            respostas_perguntas = []
            # Loop para solicitar as respostas para cada pergunta
            for pergunta in self.perguntas:
                resposta = input(f"{pergunta}: ")
                respostas_perguntas.append(resposta)

            # Obtenção da data e hora atual
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # Construção da resposta como uma lista contendo idade, gênero, respostas às perguntas e data/hora
            resposta = [idade, genero] + respostas_perguntas + [data_hora]
            self.respostas.append(resposta)

    def gravar_respostas_csv(self):
        nome_arquivo = "respostas.csv"

        with open(nome_arquivo, "a", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            
            # Verificação se o arquivo está vazio
            arquivo_vazio = arquivo_csv.tell() == 0
            
            # Escrita do cabeçalho caso o arquivo esteja vazio
            if arquivo_vazio:
                writer.writerow(self.cabecalho)

            # Escrita das respostas no arquivo CSV
            writer.writerows(self.respostas)

        print("Respostas gravadas com sucesso no arquivo CSV.")

# Definição das perguntas da pesquisa
perguntas = [
    "Qual é o seu modal de entrega? \n(1 - Carro, 2 - Moto ou 3 - Bicicleta)",
    "Você enfrenta dificuldades para encontrar endereços de entrega com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",
    "Você acredita que o valor pago pelas entregas é justo considerando seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",
    "Você considera o trabalho de entregador uma opção viável de renda com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)",
    "Você recomendaria o trabalho de entregador para outras pessoas com seu modal de entrega? \n(1 - Sim, 2 - Não, 3 - Não sei)"
]

# Criação do objeto de pesquisa
pesquisa = Pesquisa(perguntas)

# Coleta das respostas
pesquisa.coletar_respostas()

# Gravação das respostas em um arquivo CSV
pesquisa.gravar_respostas_csv()

# Documentação
"""
Esse programa realiza uma pesquisa com 5 perguntas e grava as respostas em um arquivo CSV.
As perguntas são exibidas sequencialmente, e o usuário deve responder com 1 para Sim, 2 para Não ou 3 para Não sei.
As respostas são gravadas em um arquivo CSV chamado 'respostas.csv'.
"""
