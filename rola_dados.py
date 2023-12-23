from random import randrange as rr


def joga_dados(quantia, tamanho):
    """Função responsavel por jogar os dados"""
    for dado in range(1, quantia+1):
        valor = rr(1, tamanho+1)
        print(f'Dado {dado}: {valor}')

    return 'Todos os dados foram jogados\n'


def quantia():
    """Função responsavel por pegar a quantidade de dados que serão utilizados na função joga_dados"""
    while True:
        quantidade = input('Digite a quantidade da dados que serão jogados\n')
        if quantidade <= '0':
            print('Digite um número maior que zero\n')
        else:
            try:
                quantidade = int(quantidade)
                break
            except ValueError:
                print('O valor passado deve ser um número\n')
                
    return quantidade


def valores():
    """Função responsavel por pegar a quantidade de lados do dado que serão utilizados na função joga_dados"""
    while True:
        tamanho = input('\nDigite a quantidade de lados (EX:6)\n')
        if tamanho <= '1':
            print('Digite um número maior que um\n')
        else:
            try:
                tamanho = int(tamanho)
                break
            except ValueError:
                print('O valor passado deve ser um número\n')
                
    return tamanho


if __name__ == '__main__':
    #executando as funções
    quantidade = quantia()
    tamanho = valores()


    #jogando os dados
    while True:
        resposta = input('\nDigite "1" para rolar os dados\n'
                        '"2" para mudar os dados\n'
                        '"0" para parar\n')
        if resposta == '1':
            print('\n')
            print(joga_dados(quantidade, tamanho))
        elif resposta == '0':
            print('Obrigado por ter jogado')
            break
        elif resposta == '2':
            quantidade = quantia()
            tamanho = valores()
        else:
            print('Valor incorreto')
