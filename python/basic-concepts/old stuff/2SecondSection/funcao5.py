"""
normalmente uma funcao vem em tupla (), mas como modificamos ela pra list, ela fica [] podendo ser modificada
"""

def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1,2,3,4,5)