"""Arquivo principal que será interpretado pelo interpretador."""
# COLOQUE SEU CÓDIGO AQUI
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    raio = float (input("Digite o valor do raio:"))
    print('A área do círculo é: %.2f' % float(math.pi*(raio*raio)))
  
    


if __name__ == '__main__':
    main()
