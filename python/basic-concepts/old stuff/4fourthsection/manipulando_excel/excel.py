import openpyxl

servicos = openpyxl.load_workbook('Relatorio de tempo de servico 01-2021 a 03-2022.xlsx')
print(servicos.sheetnames) # vendo as abas e quantas são dentro do excel
planilha1 = servicos['Relatório de tempo gasto por so']

print(planilha1['b4']) # retorna uma celula objeto
print(planilha1['b4'].value) # retornando o valor da celula

for linha in planilha1['c1:e2']:
    for coluna in linha:
        print(coluna.value)
