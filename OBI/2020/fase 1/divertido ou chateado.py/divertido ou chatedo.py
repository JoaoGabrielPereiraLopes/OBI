mensagem=input()
if mensagem.count(':-)')>mensagem.count(':-('):
    print('divertido')
elif mensagem.count(':-)')<mensagem.count(':-('):
    print('chateado')
else:
    print('neutro')