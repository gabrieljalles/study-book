try:
    file = open('abc.txt', 'w+')
    file.write('linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()