import csv

# main.py
# Gravação das respostas em um arquivo CSV

pergunta1 = "Você gosta de programar?"
pergunta2 = "Você está estudando Python?"
pergunta3 = "Você já trabalhou com análise de dados?"
pergunta4 = "Você se sente confortável com estatísticas?"

respostas = []
for pergunta in [pergunta1, pergunta2, pergunta3, pergunta4]:
    resposta = input(f"{pergunta} (1-Sim / 2-Não / 3-Não sei): ")
    respostas.append(resposta)

# Gravação das respostas em um arquivo CSV
nome_arquivo = "respostas.csv"
with open(nome_arquivo, "a", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(respostas)

print("Respostas gravadas com sucesso no arquivo CSV.")
