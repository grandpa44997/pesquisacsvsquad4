# main.py
# Implementação do fluxo de perguntas e respostas

# Perguntas
pergunta1 = "Você gosta de programar?"
pergunta2 = "Você está estudando Python?"
pergunta3 = "Você já trabalhou com análise de dados?"
pergunta4 = "Você se sente confortável com estatísticas?"

# Respostas
respostas = []
for pergunta in [pergunta1, pergunta2, pergunta3, pergunta4]:
    resposta = input(f"{pergunta} (1-Sim / 2-Não / 3-Não sei responder): ")
    respostas.append(resposta)

print("Respostas:", respostas)