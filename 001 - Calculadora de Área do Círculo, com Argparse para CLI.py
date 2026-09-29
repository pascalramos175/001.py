import argparse
import math

def calcular_area_por_raio(raio):
    return math.pi * (raio ** 2)

def calcular_area_por_diametro(diametro):
    raio = diametro / 2
    return math.pi * (raio ** 2)

def main():
    # Configura o parser dos argumentos da linha de comando
    parser = argparse.ArgumentParser(
        description="Calculadora de Área do Círculo via CLI."
    )

    # Cria um grupo mutuamente exclusivo (ou entra o raio, ou entra o diâmetro)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument(
        '-r', '--raio', 
        type=float, 
        help='O raio do círculo (número positivo).'
    )
    grupo.add_argument(
        '-d', '--diametro', 
        type=float, 
        help='O diâmetro do círculo (número positivo).'
    )

    # Argumento opcional para formatar as casas decimais
    parser.add_argument(
        '-p', '--precisao', 
        type=int, 
        default=2, 
        help='Número de casas decimais no resultado (padrão: 2).'
    )

    # Processa os argumentos
    args = parser.parse_args()

    # Validação de valores negativos
    if args.raio is not None and args.raio <= 0:
        parser.error("O raio deve ser um número maior que zero.")
    if args.diametro is not None and args.diametro <= 0:
        parser.error("O diâmetro deve ser um número maior que zero.")
    if args.precisao < 0:
        parser.error("A precisão não pode ser um número negativo.")

    # Executa o cálculo baseado no argumento fornecido
    if args.raio is not None:
        area = calcular_area_por_raio(args.raio)
        origem = f"raio {args.raio}"
    else:
        area = calcular_area_por_diametro(args.diametro)
        origem = f"diâmetro {args.diametro}"

    # Exibe o resultado formatado
    print(f"A área do círculo com {origem} é: {area:.{args.precisao}f}")

if __name__ == '__main__':
    main()
