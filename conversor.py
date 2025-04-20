import requests
    
def get_moeda(opcao):
    match opcao:
        case '1':
            moeda = 'BRL'
        case '2':
            moeda = 'USD'
        case '3':
            moeda = 'EUR'
        case '4':
            moeda = 'KRW'
        case _:
            print('Opção inválida')
            exit(0)

    return moeda

def currency_choice():
    opcao = input('Moeda: ')
    if '1' < opcao > '4':
        opcao = None
        return opcao
    else:
        return opcao

def get_rates(moeda):
    url = f'https://v6.exchangerate-api.com/v6/07101c470968b274701bf063/latest/{moeda}'
    response = requests.get(url).json()
    if response['result'] == 'success':
        return response
    
def get_value():
    valor = float(input('Valor: ').replace(',', '.'))
    return valor

def get_fluctuation():
    point = int(input('Valor: '))
    if point < 2:
        print('-'*60)
        print('Infelizmente não é possível que o resultado tenha menos de duas casas decimais.\nDefinindo exibição do resultado como 2 (duas) casas decimais.')
        point = 2
    return point
    
def convertion(moeda_from, moeda_to, valor):
    rates = get_rates(moeda_from)
    rates = rates['conversion_rates']
    rate = rates.get(moeda_to)
    result = valor * rate
    return result
