import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email, subject, message):
    # Configurações do servidor SMTP para Hotmail/Outlook
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_user = 'sidcentercar@hotmail.com'  # Coloque seu e-mail do Hotmail aqui
    smtp_password = 'sid160872'  # Coloque sua senha ou senha de aplicativo aqui

    # Configurações do e-mail
    from_email = smtp_user
    to_email = 'sidcentercar@homtail.com'  # Altere conforme necessário: use 'email' se quiser enviar para o usuário que preencheu o formulário
    msg_subject = subject

    # Cria o objeto MIMEMultipart e adiciona o corpo da mensagem
    message_body = f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
    msg = MIMEMultipart()
    msg.attach(MIMEText(message_body, 'plain'))

    # Adiciona os cabeçalhos necessários
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = msg_subject

    # Cria a conexão com o servidor SMTP e envia a mensagem
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
        return True
    except Exception as e:
        print(f"Falha ao enviar o e-mail: {e}")
        return False