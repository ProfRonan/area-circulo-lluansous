"""Arquivo principal que será interpretado pelo interpretador."""
# COLOQUE SEU CÓDIGO AQUI
import math
pi = 3.141592


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    raio = input("Digite o valor do raio:")
    print('A área do círculo é: %.2f' % float(pi*(raio**2)))
    


if __name__ == '__main__':
    main()
