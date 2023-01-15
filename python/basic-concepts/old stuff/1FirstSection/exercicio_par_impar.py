num1 = input("digite um número")
num2 = input("digite outro número agora")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    if num1 % 2 == 0:
        print(f'o número {num1} é par')
    else:
        print(f'o número {num1} é impar')
    if num2 % 2 == 0:
        print(f'o número {num2} é par')
    else:
        print(f'o número {num2} é impar')
else:
    print("Digite apenas números inteiros e positivos.")




