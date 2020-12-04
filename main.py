"""Arquivo principal que será interpretado pelo interpretador."""
# COLOQUE SEU CÓDIGO AQUI
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    raio = float(input('Digite o valor do raio:'))
    area = math.pi*(raio*raio)
    print (f'A área do círculo é {area:.2f}')
    


if __name__ == '__main__':
    main()
