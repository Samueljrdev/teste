from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do Flask-Mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Rota para a página com o formulário
@app.route('/')
def home():
    return render_template('form.html')

# Rota que processa os dados do formulário
@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject, sender=email, recipients=['vitinls387@gmail.com'])
    msg.body = f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
    mail.send(msg)
    return 'Sua mensagem foi enviada com sucesso. Obrigado!'

if __name__ == '__main__':
    app.run(debug=True)

