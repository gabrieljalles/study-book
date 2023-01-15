def func(*args,**kwargs):  #keywords são argumentos nomeados **qualquercoisa --> argumentos nomeados
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print("Idade não existe")


lista = [1,2,3,4,5,]
func(lista)  #nessa situação tem uma lista dentro de uma tupla resp: ([1, 2, 3, 4, 5],)
func(*lista) #nessa situação tem os valores dentro da tupla desempacotados resp: (1, 2, 3, 4, 5)

lista2 = [10,20,30,40,50]

func(*lista,*lista2) # estou pedindo para mesclar duas listas desempacotadas (1,2,3,4,5,10,20,30,40,50)

func(*lista,*lista2,nome="gabriel",idade=30)  #sem os **kwargs, o keyword argument não é possível,

