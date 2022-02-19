from desafio_1 import desafio_1
from desafio_2 import desafio_2
from desafio_3 import desafio_3


while True:
    print('\033[1;33mDESAFIO:\033[m \033[1;94mACADEMIA\033[m \033[1;34mCAPGEMINI\033[m')
    print()

    desafios = ['\033[1;33mDesafio 1\033[m', '\033[1;94mDesafio 2\033[m', '\033[1;34mDesafio 3\033[m',
                '\033[1;31mSair\033[m']

    for i, c in enumerate(desafios):
        print(f'{i+1} - {c}')

    while True:
        try:
            print()
            user = int(input('Sua opção:').strip())
            if user <= 0 or user > 4:
                print('\033[1;31mERRO: Valor digitado inválido. Verifique as opções..\033[m')
                continue
            else:
                break
        except:
            print('\033[1;31mERRO: Digite somente números inteiros\033[m')

    print()
    if user == 1:
        desafio_1()
    elif user == 2:
        desafio_2()
    elif user == 3:
        desafio_3()
    else:
        print('Obrigador ver meu desafio!')
        quit()

    print()
    input('\033[1;32mAperte enter para voltar para o menu dos desafios!\033[m')
    print()
