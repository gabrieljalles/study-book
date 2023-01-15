# usado para executar comandos em segundo plano
# o stdout é usado para a saida do comando
#bom para monitorar servidores

import subprocess

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True # estou pedindo que o resultado do stdout va para a variavel e não para a tela do computador
                        # dessa forma, posso mandar e trabalhar com ela em outro lugar
)

print(proc.stderr) # verificação de erro no comando
print(proc.stdout) #verificação da saida
print(proc.returncode) # = 0 , conclui com sucesso !
print(proc.args) #argumentos que eu passei