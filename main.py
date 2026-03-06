"""
Gerador de Senha Segura

Programa que gera uma senha segura.
Versão: 1.0
"""
from secrets import choice
from random import shuffle

TAMANHO_LINHA = 78
TITULO = 'Gerador de Senha Segura'
LETRAS_MAIUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETRAS_MINUSCULAS = 'abcdefghijklmnopqrstuvwxyz'
NUMEROS = '0123456789'
CARACTERES_ESPECIAIS = "!@#$%&*?"


def gerar_senha_segura() -> str:
    """
    Função que gera uma senha segura.
    """
    senha = [choice(LETRAS_MAIUSCULAS), choice(LETRAS_MINUSCULAS), choice(NUMEROS), choice(CARACTERES_ESPECIAIS)]
    todos_caracteres = LETRAS_MAIUSCULAS + LETRAS_MINUSCULAS + NUMEROS + CARACTERES_ESPECIAIS

    while len(senha) < 12:
        senha.append(choice(todos_caracteres))

    shuffle(senha)
    senha = ''.join(senha)

    return senha


def main():
    """
    Função principal que executa o fluxo do programa.
    """
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")

    senha = gerar_senha_segura()
    print('Senha gerada:', senha)
    print(TAMANHO_LINHA * "=")


if __name__ == '__main__':
    main()
