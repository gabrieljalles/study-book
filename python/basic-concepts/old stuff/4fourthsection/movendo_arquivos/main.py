import os
import shutil

caminho_atual = r'C:\Users\Gabriel\Desktop\caminho atual'
caminho_novo = r'C:\Users\Gabriel\Desktop\caminho novo'

try: # tentando criar, caso já tenha, ele ignora ....
    os.mkdir(caminho_novo) # estou pedindo para criar uma pasta
except FileExistsError as e: #tratando os erros
    print(f'O arquivo {caminho_novo} já existe!')

for root, dirs, files in os.walk(caminho_atual):
    for file in files:
        old_file_path = os.path.join(root, file) # fazendo a junção do caminho antigo  e o nome
        new_file_path = os.path.join(caminho_novo,file) #fazendo a juncao do caminho novo e o nome

        #CASO VOCE QUEIRA CORTAR
        if '.txt' in file: # pedindo arquivos específicos
            shutil.move(old_file_path, new_file_path) #executando o movimento, muito cuidado para não substituir
            # OUTRA DICA : se você pedir para mover o arquivo para o mesmo lugar com outro nome, ele apenas renomeia.

        #CASO VOCÊ QUEIRA COPIAR:
           #shutil.copy(old_file_path,new_file_path)

        #CASO VOCE QUEIRA APAGAR, NÃO TEM VOLTA, APAGUE SOMENTE O QUE TEM CTZ
            os.remove(new_file_path) #txt apagado
