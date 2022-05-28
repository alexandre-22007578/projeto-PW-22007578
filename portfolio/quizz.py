import matplotlib.pyplot as dadosGraficos


def informacao_sobre_utilizadores(arg):
    dados = {}
    for quizz in arg:
        dados[quizz.nome] = Pontuacao(quizz)

    return dados


def desenha_graficodados(arg):
    dados = informacao_sobre_utilizadores(arg)

    dadosOrdenados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dadosOrdenados.keys())
    pontuacao = list(dadosOrdenados.values())

    dadosGraficos.figure(figsize=(7, 4))

    dadosGraficos.barh(pessoa, pontuacao, color='#201120FF')

    dadosGraficos.title("Pontuação do Quizz!")
    dadosGraficos.ylabel("Participantes")
    dadosGraficos.xlabel("Pontuação")

    dadosGraficos.savefig('portfolio/static/portfolio/images/graficoQuizz.png')


def Pontuacao(input):
    pontuacao = 0

    if input.pergunta1 == "ola":
        pontuacao += 5

    if input.pergunta2 == "ola":
        pontuacao += 5

    if input.pergunta3 == "ola":
        pontuacao += 5

    if input.pergunta4 == "ola":
        pontuacao += 5

    return pontuacao
