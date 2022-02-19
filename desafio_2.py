def desafio_2():
    from time import sleep as slp

    while True:
        # Mini menu
        print('\033[1;94mANALISADOR DE SENHAS\033[m')
        print()
        opt = ['Analisar a senha', 'Ler requisítos uma senha protegida', 'sair']
        for i, o in enumerate(opt):
            print(f'{i+1}- {o}')

        while True:
            try:
                print()
                user = int(input('Sua opção:').strip())
                if user > 3:
                    print('\033[1;31mERRO: Você só pode digitar números de 1 a 3.\033[m')
                    continue
                else:
                    break
            except:
                print('\033[1;31mERRO: Digite somente números inteiros\033[m')

        if user == 1:
            while True:
                print()
                # inicio do desafio: Verificador de senhas.
                password = input('Digite sua senha: ').strip()
                print()

                if len(password) >= 6:
                    print('\033[0;33mAnalisando senha...\033[m')
                    print()
                    slp(0.5)
                    break
                else:
                    print(f'\033[1;31mERROR: Senha deve ter no mínimo 6 digitos. Por favor, acrescente mais '
                          f'{6-len(password)} caracteres.\033[m')

            # extra: um contador de pontos para a segurança da sua senha.
            analysis = set()
            for x in password:
                if x.islower():
                    analysis.update('l')
                elif x.isnumeric():
                    analysis.update('n')
                elif x.isupper():
                    analysis.update('u')
                elif x in '!@#$%^&*()-+':
                    analysis.update('s')

            score = 0

            for c in analysis:
                if c in 'lnus':
                    score += 1

            if score == 1:
                print('A senha ainda está fraca... Leia os requísitos para uma senha forte.')
            elif score == 2:
                print('A senha está razoável.')
            elif score == 3:
                print('A senha está forte.')
            elif score == 4:
                print('A senha está muito segura.')
            print()

        #extra 2: Permite o usuário ver os requisistos para uma senha segura.
        elif user == 2:
            print()
            print('''Para sua senha ser protegida precisa dos seguintes requisítos:
            1- Possuir no mínimo 6 caracteres.
            2- Conter no mínmimo 1 dígito
            3- Conter no mínimo 1 letra minúsculo
            4- Conter no mínimo 1 letre maiúscula
            5- Conter no mínimo 1 caractere especial. Exemplo: !@#$%^&*()-+.''')

        else:
            print('\033[1;33mObrigado por usar meu analisador de senhas!!!\033[m')
            break
        input('Aperte enter para continuar!')
        print()
