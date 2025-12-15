import os

os.system('clear')
print('Vamos lá ao jogo das perguntas...')
input()

perguntas = ['Qual é a cor da vaca?',
             'Qual é a cor do porco?', 'Qual é a cor da galinha?']
respostas_corretas = ['Branco', 'Rosa', 'Vermelho']


def fazer_perguntas():
    pontuacao = 0

    for i in range(len(perguntas)):
        resposta = input(perguntas[i] + ' ').lower()

        if resposta == respostas_corretas[i].lower():
            pontuacao += 1
            print('Você acertou!')
        else:
            print(f'Errou! A resposta correta é: {respostas_corretas[i]}')
        print()

    return pontuacao


pontuacao = fazer_perguntas()
print(f'SUA PONTUAÇÃO NO MOMENTO É: {pontuacao}')
