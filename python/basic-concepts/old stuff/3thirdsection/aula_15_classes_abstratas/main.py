from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

cp = ContaPoupanca(111,22,0)
cp.depositar(22000000)
cp.sacar(500000)
cp.sacar(360000)
cp.sacar(100000)
cp.sacar(1000000)

cc = ContaCorrente(1111, 184894, 50, limite=1000)
cc.sacar(1050)

