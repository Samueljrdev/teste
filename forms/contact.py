import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(name, email, subject, message):
    # Configurações do servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = ''
    smtp_password = ''

    # Configurações do e-mail
    from_email = smtp_user
    to_email = 'vitinls387@gmail.com'
    msg_subject = subject

    # Cria o objeto MIMEMultipart e adiciona o corpo da mensagem
    message_body = f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
    msg = MIMEMultipart()
    msg.attach(MIMEText(message_body))

    # Adiciona o assunto da mensagem
    msg['Subject'] = msg_subject

    # Adiciona os anexos
    # Nenhum anexo neste exemplo

    # Cria a conexão com o servidor SMTP e envia a mensagem
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return True
    except:
        return False
