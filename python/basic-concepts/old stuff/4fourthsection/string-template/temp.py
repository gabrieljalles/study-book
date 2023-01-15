from string import Template
from datetime import datetime

with open('template.html','r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='gabriel', data=data_atual)

#caso no próprio html, tenha uma string que não foi mencionada acima, ele quebra o código.
#você pode usar safe_substitute ao invés de substitute , dessa forma, caso tenha um valor no html que não esteja no corpo_msg

print(corpo_msg)
