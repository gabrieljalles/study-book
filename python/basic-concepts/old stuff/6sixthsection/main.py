from creation import DDLSQLite
from crud import CrudSQLite

objeto = DDLSQLite()
objeto_crud = CrudSQLite('desafio')

objeto.criar_banco_de_dados('desafio')

# ddl_create = """
# CREATE TABLE cliente (
#     id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     nome_cliente TEXT NOT NULL,
#     cpf VARCHAR(14) NOT NULL,
#     email TEXT NOT NULL,
#     telefone VARCHAR(15),
#     cidade TEXT,
#     estado VARCHAR(2) NOT NULL,
#     data_cadastro DATE NOT NULL
#     );
# """

# objeto.criar_tabela(nome_banco='desafio', ddl_create=ddl_create)

dados = [
    {
        'nome_cliente': 'Joao',
        'cpf': '111.111.111-11',
        'email': 'joao@servidor',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'data_cadastro': '2020-01-01'
    },
    {
        'nome_cliente': 'Maria',
        'cpf': '222.222.222-22',
        'email': 'maria@safadinha',
        'cidade': 'Uberlandia',
        'estado': 'Minas gerais',
        'data_cadastro': '2021-02-03'
    }
]

# sempre que o codigo é executado, ele gera um novo registro, mesmo que repetido !
# for valor in dados:
    # objeto_crud.inserir_registro(tabela='cliente', registro=valor)


#vendo os registros
dados_carregados = objeto_crud.ler_registros('cliente')
for dado in dados_carregados:
    print(dado)

# atualizando registro
dado_atualizar = {'telefone':'(11)1.1111-1111'}
condicao = {'id_cliente': 1}

objeto_crud.atualizar_registro('cliente',dado_atualizar,condicao =condicao)

#lendo registros
dados_carregados = objeto_crud.ler_registros('cliente')
for dado in dados_carregados:
    print(dado)

#apagando registro
condicao = {'id_cliente': 1}

# objeto_crud.apagar_registro('cliente',condicao)

