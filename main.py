# main.py
# Gravação das respostas em um arquivo CSV (sem usar bibliotecas)

perguntas = [
    "Você gosta de programar?",
    "Você está estudando Python?",
    "Você já trabalhou com análise de dados?",
    "Você se sente confortável com estatísticas?"
]

respostas = [input(f"{pergunta} (1-Sim / 2-Não / 3-Não sei): ") for pergunta in perguntas]

# Formatação das respostas como uma linha CSV
linha_csv = ','.join(respostas) + '\n'

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
    with open(nome_arquivo, "w") as arquivo_csv:
        cabecalho = ','.join(perguntas) + '\n'
        arquivo_csv.write(cabecalho)

# Adicionar as respostas
with open(nome_arquivo, "a") as arquivo_csv:
    arquivo_csv.write(linha_csv)

print("Respostas gravadas com sucesso no arquivo CSV.")

# Documentação
"""
Esse programa realiza uma pesquisa com 4 perguntas e grava as respostas em um arquivo CSV.
As perguntas são exibidas sequencialmente, e o usuário deve responder com 1 para Sim, 2 para Não, ou 3 para Não sei.
As respostas são gravadas em um arquivo CSV chamado 'respostas.csv'.
