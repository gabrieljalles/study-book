#maneiras de trabalhar com data, tempo e delta tempo
from datetime import datetime, timedelta

                #ano #mes #dia #hora #minuto #segundo
data = datetime(2019,  4,  20,   10,    53,      20)
print (data) # 2019-04-20 10:53:20 geralmente é assim que salvamos as coisas nas bases de dados

#outra forma, ele recebe a string e o formato logo depois (str, fmt)
data = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data)

#caso eu queira formatar a data para o usuário eu uso :
print(data.strftime('%d/%m/%Y %H:%M:%S')) #aqui dentro, eu coloco como eu quero veja nesse site as possibilidades:
                            #https://docs.python.org/2/library/datetime.html #veja nas ultimas linha

#eu posso usar o timestamp contagem de segundos até o momento da data usada,
print(data.timestamp()) #1555729200.0

#para converter de simtestamp para o formato padrão
data = datetime.fromtimestamp(1555729200.0)
print(data)

#-----------------------------------------------------------------------------------
#timedelta

#diferenca de dias
d1 = datetime.strptime('20/04/1980 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('20/04/1980 22:00:00', '%d/%m/%Y %H:%M:%S')
dif = d2-d1
print(dif)
print(dif.seconds) #vendo apenas os segundos das horas
print(dif.total_seconds()) #vendo os segundos totais
print(dif.days) #vendo diferenças em dias



#acrecentando tempo
data1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data1 = data1 + timedelta(days=5, minutes=52, seconds=38)
print(data1.strftime('%d/%m/%Y %H:%M:%S'))


#datas em extenso (ingles)
dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

#datas em extenso (pt)
from locale import setlocale, LC_ALL
setlocale(LC_ALL, '') # se eu deixar o segundo parametro vazio, ele pega o do computador atual
setlocale(LC_ALL, 'pt_BR.utf-8') #forçando ficar sempre em pt
formatacao1 = dt.strftime('%A, %d de %B de %Y')
print(formatacao1)

#------------------------------------------------------------------------------------------------
#pegando o último dia do mês
from calendar import mdays #retorna quantos dias tem um mês

#pegando o número do mês atual
mes_atual = int(dt.strftime('%m'))

#se você imprimir mdays você consegue quantos dias tem cada mês na forma de LISTA
print(mdays)
print(mdays[mes_atual]) #tirando apenas o valor do mês atual

 #para anos bissexto não funciona da mesma forma
#você pode usar:
from calendar import monthrange #retorna o dia da semana e o último dia do mês
print(monthrange(2020,2)) # r: (5, 29)

#você pode optar por desencapsular
dia_semana, ultimo_dia_mes = monthrange(2020,2)
print(dia_semana, type(dia_semana))
print(ultimo_dia_mes, type(ultimo_dia_mes))

#imprimindo de vários meses
ultimo_dia_meses_ano_atual = [monthrange(datetime.now().year,mes)[1] for mes in range (1,13)]
"""
explicando o código acima:
    list comprehension em que chamamos a func monthrange é colocado como parametro uma func que traz o ano atual e uma
    variavel que retorna no indice [1](indice do ultimo dia do mes) para cada mes no range de 1 a 13 = 13 é exclusivo
"""
print(ultimo_dia_meses_ano_atual)
#para concluir, o metodo anterior não é possível conseguir o bissexto, nesse último metodo sim.





