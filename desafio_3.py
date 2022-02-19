def desafio_3():
    from time import sleep as slp
    print('\033[1;34mDECIFRADOR DE ANAGRAMAS\n\033[m')

    while True:
        word = input('Digite uma anagrama:').strip().lower()
        print()

        print('\033[0;33mDecifrando seu anagrama...\033[m')
        slp(1)
        # Encontra todas as sub-palavras contidas na palavra.
        ordered_words = []
        for x in range(len(word)):
            for y in range(len(word) + 1):
                if word[x:y] != '' and word[x:y] != word:
                    ordered_words.append(word[x:y])

        # Encontra os pares de anagramas contido nas palavras.
        anagrams = []
        for a in range(len(ordered_words)):
            for b in ordered_words[a + 1:]:
                analysi_a = sorted(ordered_words[a][::-1])
                analysi_b = sorted(b)
                if analysi_a == analysi_b and (ordered_words[a], b) not in anagrams:
                    anagrams.append((ordered_words[a], b))

        # Conta quantos anagramas diferentes tem na frase.
        counting = []
        for pair in anagrams:
            for c in pair:
                if c not in counting:
                    counting.append(c)

        print(
            f'\n{len(counting)} tipos diferentes de anagramas foram encontrados.\nOs pares de anagramas foram: {anagrams}.')

        user = input('\nDeseja analisar outro anagrama(S/N)?').strip().lower()
        print()
        if user == 's' or user == 'sim':
            continue
        elif user == 'n' or user == 'não' or user == 'nao':
            print('\033[1;33mEncerrando decifrador de anagramas... Obrigado por usar nossos serviços!\033[m')
            break
        else:
            print('Vamos considerar isso como um "não"...')
            break
