x = 0  #coluna


while x < 10 :
    y = 0  # linha  # o y  dentro do while do x faz com que ele se torne 0 todas as vezes que o x muda os valores
    while y < 5 :
        print(f' ({x},{y})')
        y += 1
    x += 1