import csv

# main.py
# Gravação das respostas em um arquivo CSV

perguntas = [
    "Você gosta de programar?",
    "Você está estudando Python?",
    "Você já trabalhou com análise de dados?",
    "Você se sente confortável com estatísticas?"
]

respostas = []
for pergunta in perguntas:
    resposta = input(f"{pergunta} (1-Sim / 2-Não / 3-Não sei): ")
    respostas.append(resposta)

# Gravação das respostas em um arquivo CSV
nome_arquivo = "respostas.csv"
with open(nome_arquivo, "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(respostas)

print("Respostas gravadas com sucesso no arquivo CSV.")
