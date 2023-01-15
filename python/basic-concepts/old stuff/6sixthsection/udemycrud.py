import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():  # metodo usado para evitar esquecer de fechar conexao
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('conexão fechada com sucesso !')
        conexao.close()


# -------------------------- ADICIONANDO UMA PESSOA UNICA ---------------------
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#             '(%s,%s,%s,%s)'
#         cursor.execute(sql,('cleiton','borges',122,200))
#         conexao.commit()

# -------------------------- ADICIONANDO VARIAS PESSSOAS ---------------------
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#             '(%s,%s,%s,%s)'
#         dados = [
#             ('Muriel','feijao','19','80'),
#             ('fernandinho','azeitona','50','85'),
#             ('fagundes','carniça','4','20'),
#         ]
#         cursor.executemany(sql, dados) #execute many manda vários para o banco de dados
#         conexao.commit()

# -------------------------- DELETANDO UMA PESSOA DA LISTA ---------------------
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,)) #é necessario a virgula depois do numero para mostrar que é uma tupla
#         conexao.commit()

#-------------------------- DELETANDO VARIAS PESSOAS DA LISTA--------------------
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

#-------------------------- DELETANDO REGISTROS ENTRE RANGES  --------------------
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql,(2,5))
#         conexao.commit()

#-------------------------MODIFANDO UM VALOR DA LISTA --------------------------------------------
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE FROM clientes SET nome= %s WHERE id=%s' #modificando o nome onde o id é ....
        cursor.execute(sql,('JOANA',5))
        conexao.commit()



# ------------------------CRIANDO REGRA PRA SEMPRE FECHAR DEPOIS DE USAR--------------------------
with conecta() as conexao:  # esse gerenciador de contexto fecha a conexao quando caba de usar
    with conexao.cursor() as cursor:  # esse gerenciador de contexto fecha o cursor quando caba de usar
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')  # sempre de limite as consultas
        resultado = cursor.fetchall()  # pegando todos os dados da coluna!
        for x in resultado:
            print(x)
        for y in resultado:
            print(y['nome'], y['sobrenome'])
