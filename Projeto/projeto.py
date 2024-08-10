nome_do_usuario = str(input('Digite seu nome'))
idade_do_usuario = int(input('Digite sua idade'))

if idade_do_usuario < 18:
    print(f'{nome_do_usuario} você não tem idade suficiente.')
elif idade_do_usuario >= 18:
    print(f'{nome_do_usuario} parabens, voçê tem idade suficiente!')
