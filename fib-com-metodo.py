''''
 Nome do programa: fib-com-metodo.py
 Autor: Luiz Gustavo Bragança dos Santos
 Objetivo: calcular o termo fibonacci.
'''

# apresentacao() - metodo para apresentacao.
def apresentacao():
    print("\nPrograma que calcula o Fibonacci.")
    print("\nDesenvolvido por Luiz Gustavo.")
# end apresentacao()

# leia_termos_fibonacci() - le o termo desejado.
def leia_termos_fibonacci():
    termo = int(input("\nEntre com o termo Fibonacci desejado = "))

    return termo
# end leia_termos_fibonacci()

# calc_fibonacci() - calcula o termo fibonacci.
def calc_fibonacci(termo):
    f = 0
    ant = 0

    for i in range(termo):
        if i == 1:
            f = 1
            ant = 0
        else:
            f += ant
            ant = f - ant

    return f
# end calc_fibonacci()

# print_fibonacci() - mostra o termo
def print_fibonacci(termo):
    print("\nTermo Fibonacci = ", termo)
# end print_fibonacci()

# Main
if __name__ == '__main__':
    apresentacao()

    termo = leia_termos_fibonacci()

    termo = calc_fibonacci(termo)

    print_fibonacci(termo)
# end main
