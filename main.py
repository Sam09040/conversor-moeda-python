from conversor import convertion, currency_choice, get_fluctuation, get_moeda, get_value, currency_choice

print('-'*60)
print(' '*15,'Bem vindo(a) ao conversor!')
print('-'*60)

print(' '*15, 'Escolha a moeda de origem: \n')
print(' '*8, '(1) BRL -- (2) USD -- (3) EUR -- (4) KRW')
print('-'*60)
moeda_from = currency_choice()
moeda_from = get_moeda(moeda_from)

print('-'*60)
print(' '*8, 'Escolha a moeda para qual deseja converter:\n')
print(' '*8, '(1) BRL -- (2) USD -- (3) EUR -- (4) KRW')
print('-'*60)
moeda_to = currency_choice()
moeda_to = get_moeda(moeda_to)

print('-'*60)
print(' '*10, 'Qual o valor que deseja converter?')
print('-'*60)
valor = get_value() 

print('-'*60)
print(' '*6, 'Quantas casas decimais o resultado deve ter?')
print('-'*60)
point = get_fluctuation()

result = convertion(moeda_from, moeda_to,valor)

print('-'*60)
print(f'O valor é de {result:.{point}f} {moeda_to}!')
