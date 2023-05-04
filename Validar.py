while True:
    cpf = input('Digite o CPF: ') \
        .replace('.', '') \
        .replace(' ', '') \
        .replace('-', '')
    nove_digitos = cpf[:9]
    contador_regressivo = 10

    resultado = 0
    for digito_1 in nove_digitos:
        resultado += int(digito_1) * contador_regressivo
        contador_regressivo -= 1
    digito_1 = (resultado * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito2 = (resultado_2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    novo_cpf = f'{nove_digitos}{digito_1}{digito2}'

    if cpf == novo_cpf:
        print(f'{novo_cpf} é valido!')
    else:
        print('CPF invalido!')

