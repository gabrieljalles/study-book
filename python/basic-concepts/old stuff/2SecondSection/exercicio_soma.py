lista_a = [1,2,3,4,5,6,7,8,9]
lista_b = [1,2,3,4]

resultado_py = [lista_a[i] + lista_b[i] for i,_ in enumerate(lista_b)]
print(resultado_py)

#outra forma mais compacta
resultado_py_2  = [x + y for x,y in zip(lista_b,lista_a)]
print(resultado_py_2)
