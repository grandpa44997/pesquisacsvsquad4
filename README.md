Pesquisa de Opinião - README
TESTE
Este projeto consiste em um programa Python para coleta de respostas de uma pesquisa de opinião e gravação dessas respostas em um arquivo CSV. O programa foi desenvolvido de forma simples e sem a utilização de bibliotecas adicionais.
Instruções de Uso

    Certifique-se de ter o Python instalado em sua máquina. Você pode fazer o download em python.org.

    Faça o download ou clone este repositório para o seu ambiente local.

    Abra um terminal ou prompt de comando e navegue até o diretório do projeto.

    Execute o arquivo main.py utilizando o comando python main.py no terminal.

    O programa solicitará que você informe a idade e gênero do participante da pesquisa. Digite as informações solicitadas e pressione Enter.

    Em seguida, o programa apresentará as perguntas da pesquisa. Para cada pergunta, digite a resposta de acordo com as opções apresentadas: "1" para Sim, "2" para Não ou "3" para Não sei. Pressione Enter após digitar cada resposta.

    Continue respondendo às perguntas até que deseje finalizar a coleta de respostas. Para encerrar a coleta, digite "00" quando for solicitado a idade.

    Após encerrar a coleta de respostas, o programa gravará as respostas em um arquivo CSV chamado respostas.csv no mesmo diretório do projeto.

    As respostas da pesquisa estão agora gravadas no arquivo CSV e podem ser utilizadas para análise posterior.

Observações

    Certifique-se de que o arquivo main.py está no diretório correto e que você possui permissões para leitura e gravação de arquivos nesse diretório.

    O programa utiliza um formato simples para as perguntas e respostas. Caso deseje modificar ou adicionar novas perguntas, você pode editar o código-fonte no arquivo main.py e ajustar a lista de perguntas conforme necessário.

    Lembre-se de utilizar as aspas duplas ("") para incluir textos com espaços em branco nas perguntas. Por exemplo: "Você gosta de fazer entregas?"

    As respostas são gravadas em formato CSV, separadas por vírgulas. Se as respostas contiverem vírgulas, elas serão tratadas como parte do texto da resposta.

    Caso queira realizar uma nova pesquisa, basta executar novamente o programa. As novas respostas serão adicionadas ao arquivo CSV existente.

    Se desejar reiniciar a pesquisa e começar com um arquivo CSV vazio, basta excluir o arquivo respostas.csv antes de executar o programa.

Conclusão

O projeto de pesquisa de opinião em Python oferece uma forma simples de coletar e gravar respostas em um arquivo CSV. Sinta-se à vontade para explorar e adaptar o código para suas necessidades. Esperamos que esse projeto seja útil para você!

Em caso de dúvidas ou sugestões, sinta-se à vontade para entrar em contato.

Aproveite e aproveite o processo de pesquisa!

Equipe de Desenvolvimento




# pesquisacsvsquad4
trabalho em grupo do modulo 2 do curso vamoai

MODO DE USAR:



O PROJETO
EM GRUPO
Módulo 2 – Quero os dados na minha mesa

CONTEXTO
Sua equipe recebeu uma nova solicitação de projeto! Dessa vez
para desenvolver uma pesquisa digital com a população de
várias cidades do Brasil.
Para isso, será necessário armazenar os dados dessa pesquisa em
um arquivo .csv para utilização em análises futuras.
A pesquisa será feita a partir de um levantamento ativo, realizado
pelos funcionários da empresa que irão sair com o projeto nas ruas
para coletar as respostas.

Detalhes do projeto:
⇨ A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as
questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3).
⇨ Para iniciar o questionário será solicitado ao usuário que informe a sua idade e gênero. Cada
linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3,
resposta_4, data e hora da resposta
⇨ O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as
respostas informadas nas linhas do .csv até que a idade de 00 seja informada, então podemos
ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada
o projeto para de executar).
⇨ Com os dados preenchidos no .csv o grupo deve realizar uma exibição simples dos resultados
utilizando o Excel (simulem 10 respostas no questionário para gerar os dados). Na apresentação
será demonstrado o funcionamento do questionário e o exemplo dos dados coletados.

REQUISITOS
■ A entrada dos dados deverá ser realizada pelo teclado utilizando estruturas de repetição;
■ Estruturas condicionais e de repetição devem ser utilizadas;
■ Estruturas de dados devem ser utilizadas (listas, pilhas, filas ou dicionários), quando for
possível o uso;
■ Deverá ser utilizada a estrutura de funções, quando for possível o uso;
■ Deve ser utilizado o paradigma de orientação a objetos;
■ O projeto desenvolvido deverá ser disponibilizado em repositório no GitHub;
■ O projeto desenvolvido deverá estar funcional, ou seja, caso seja necessário algum teste
durante a apresentação ou correção do trabalho ele deve estar funcionando normalmente.
