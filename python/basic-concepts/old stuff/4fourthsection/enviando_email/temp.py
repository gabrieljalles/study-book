from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart  # pra quem ? de quem ? assunto ?
from email.mime.text import MIMEText  # corpo do email ou texto em html
from email.mime.image import MIMEImage  # imagem para enviar
import smtplib  # ferramente que vai mandar a mensagem

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='gabriel jalles', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'gabriel jalles '  # quem envia
msg['to'] = meu_email  # quem recebe CLIENTE
msg['subject'] = 'Atenção este é um email de teste'

# corpo = MIMEText("djsahdkljdhwakjhadjshd") # se fosse um texto simples, somente isso bastava
corpo = MIMEText(corpo_msg, 'html')  # estou mostrando o formato
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # cada provedor tem um específico
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)  # email que está enviando a msg
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as error:
        print('E-mail não enviado...')
        print('Erro:', error)