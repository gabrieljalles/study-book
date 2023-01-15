"""
Exercício com abstração , heranca, encapsulamento polimorfismo.

    Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma
conta (poupanca ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes
e contas.

DICAS :
    Criar classe cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade ( com getters )
    Cliente Tem conta (agregação da classe contaCorrente ou ContaPoupanca)
    Criar classes ContaPoupanca e Conta Corrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agencia, numero da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato ( abstracao e polimorfismo ) as subclasses que implementam o
    metodo sacar)
    Criar classe banco para agregar classes de clientes e de contas ( agregação)
    Banco será responsável autenticar o cliente e as contas da seguinte maneira:
        checar se a agencia é daquele banco.
        checar se o cliente e daquele banco.
        checar se a conta é daquele banco.
    Só será possível sacar se passar na autenticacao do banco(descrita acima)
"""

