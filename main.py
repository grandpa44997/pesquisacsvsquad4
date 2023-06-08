# main.py
# Gravação das respostas em um arquivo CSV usando classes (sem usar bibliotecas)

class Pesquisa:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.respostas = []

    def coletar_respostas(self):
        for pergunta in self.perguntas:
            resposta = input(f"{pergunta} (1-Sim / 2-Não / 3-Não sei): ")
            self.respostas.append(resposta)

    def gravar_respostas_csv(self):
        # Formatação das respostas como uma linha CSV
        linha_csv = ','.join(self.respostas) + '\n'

        # Gravação das respostas em um arquivo CSV
        nome_arquivo = "respostas.csv"

        # Verificar se o arquivo já existe
        arquivo_existe = False
        try:
            with open(nome_arquivo, "r"):
                arquivo_existe = True
        except FileNotFoundError:
            arquivo_existe = False

        # Escrever o cabeçalho se o arquivo não existir
        if not arquivo_existe:
            cabecalho = ','.join(self.perguntas) + '\n'
            with open(nome_arquivo, "w") as arquivo_csv:
                arquivo_csv.write(cabecalho)

        # Adicionar as respostas
        with open(nome_arquivo, "a") as arquivo_csv:
            arquivo_csv.write(linha_csv)

        print("Respostas gravadas com sucesso no arquivo CSV.")

# Criação do objeto de pesquisa
perguntas = [
    "Você gosta de programar?",
    "Você está estudando Python?",
    "Você já trabalhou com análise de dados?",
    "Você se sente confortável com estatísticas?"
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
