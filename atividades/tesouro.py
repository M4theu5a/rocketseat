tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

jogador = "x"


def exibir_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)


def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2 or
        tabuleiro[linha][coluna] != ""
    ):
        print("Jogada inválida!")
        return jogador
    tabuleiro[linha][coluna] = jogador
    return "o" if jogador == "x" else "x"
