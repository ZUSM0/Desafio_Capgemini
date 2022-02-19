def desafio_1():
    print('\033[1;33mESCADA DE ASTERISCO\n\033[m')

    while True:
        # Verificador de números inteiros
        try:
            n = int(input('Digite um número:').strip())
            if n <= 0:
                print('\033[1;31mERRO: Por favor, digite somentes números maiores que 0.\033[m')
                print()
            else:
                break
        except:
            print('\033[1;31mERRO: Você só pode digitar números inteiros...Tente novamente.\033[m')
            print()

    # Código para fazer a escada de asterisco
    dcr = n
    for value in range(1, n+1):
        size = '*' * value
        space = ' ' * dcr
        print(f'{space}{size}')
        dcr -= 1
