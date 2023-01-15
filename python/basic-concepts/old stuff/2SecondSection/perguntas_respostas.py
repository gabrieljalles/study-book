perguntas = {
    'pergunta 1' : {
        'pergunta': 'quanto é dois mais dois ?',
        'resposta': { 'a': '1','b': '2','c': '4',},
        'resposta_certa' : 'c'
    },
    'pergunta 2' : {
        'pergunta': 'Quanto é 3*2 ? ',
        'resposta': { 'a': '6','b': '2','c': '4',},
        'resposta_certa' : 'a'
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')

    for rk,rv in pv['resposta'].items():
        print(f'{rk}) {rv}')
    resposta_usuario =input('digite sua resposta entre as alternativas citadas anteriormente:')
    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1

print(f'você acertou um total de {respostas_certas} / {len(perguntas)} perguntas ')

