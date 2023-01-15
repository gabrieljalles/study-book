import sqlite3
import os


class DDLSQLite:


    def _conectar(self, nome_banco):
        nome_banco += '.db'
        conn = sqlite3.connect(nome_banco)
        return conn


    def criar_banco_de_dados(self, nome_banco):
        nome_banco += '.db'
        if not os.path.exists(nome_banco):
            sqlite3.connect(nome_banco).close()
            print(f'Banco de dados {nome_banco} criado com sucesso !')
        else:
            print(f'Banco de dados {nome_banco} já existe !')


    def criar_tabela(self,nome_banco, ddl_create):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(ddl_create)
        cursor.close()
        conn.close()
        print(f'Tabela criada com sucesso !')

    @staticmethod
    def apagar_tabela(self, nome_banco, tabela):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE {tabela}')
        cursor.close()
        conn.close()
        print(f'A tabela {tabela} foi excluida com sucesso !')

