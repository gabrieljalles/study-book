lista =[
       #0     #1     #2
    ['Edu','Joao','Luiz'],       #0
    ['Maria','Aline','Joana'],   #1
    ['Helena','Ed','lu']         #2
]

for v1, v2 in enumerate(lista):
    print(v1,v2)
#resp:
"""
0 ['Edu', 'Joao', 'Luiz']
1 ['Maria', 'Aline', 'Joana']
2 ['Helena', 'Ed', 'lu']
"""

# você pode manipular o enumerate para que ele comece a contar a partir  do número que quiser
for v1,v2 in enumerate(lista,22):
    print(v1,v2)
#resp:
"""
22 ['Edu', 'Joao', 'Luiz']
23 ['Maria', 'Aline', 'Joana']
24 ['Helena', 'Ed', 'lu']
"""
