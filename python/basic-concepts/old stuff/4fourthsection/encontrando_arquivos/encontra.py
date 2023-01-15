import os

#sempre que tem barras invertidas, coloque um 'r' para não ter problemas com elas
caminho_procura = r'C:\Users\Gabriel\Desktop'
termo_procura = 'minha'

# raiz = a pasta que estamos verificando
# diretorio = a lista de diretorios até o arquivo
# arquivos = a lista de arquivos

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho/= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho/= giga
        texto = 'G'

    tamanho = round(tamanho,2)
    return f'{tamanho} {texto}'



contagem = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contagem += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print(f'Arquivo encontrado: {nome_arquivo}')
                print(f'Extensao do arquivo: {ext_arquivo}')
                print(f'tamanho do arquivo: {tamanho}')
                print(f'tamanho formatado: {formata_tamanho(tamanho)}')
                print(f'diretorio do arquivo: {raiz}')

            except PermissionError as e:
                 print('Sem permissão na pasta.')
            except FileNotFoundError as e:
                 print('Arquivo não encontrado')
            except Exception as e:
                 print('Erro desconhecido:', e)

print(f' {contagem} arquivo(s) encontrados(s).')
