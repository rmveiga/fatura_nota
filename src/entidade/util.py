def formata_numero_telefone(numero, cod_pais=None, ddd=None):
    resultado = ''

    if cod_pais:
        resultado += f'+{cod_pais} '
    if ddd:
        resultado += f'({ddd}) '
    if len(numero) == 8:
        resultado += f'{numero[:4]}-{numero[5:]}'
    elif len(numero) == 9:
        resultado += f'{numero[:5]}-{numero[6:]}'
    else:
        resultado += numero

    return resultado
