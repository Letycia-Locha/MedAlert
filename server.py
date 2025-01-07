from registro_numeros import init_db, register_phone_number, register_medication, get_data, remove_medication
import schedule
import time
from twilio.rest import Client
import re
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Inicializa o banco de dados
init_db()

# Configurações do Twilio
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Função para exibir o menu principal
def exibir_menu():
    return (
        "🌟 Bem-vindo ao MedAlert! 🌟\n"
        "📱 1. Cadastrar ou atualizar número de telefone\n"
        "💊 2. Adicionar medicação\n"
        "📋 3. Visualizar medicações\n"
        "🛑 4. Desativar alerta de uma medicação\n"
        "🚪 5. Sair\n\n"
        "Digite o número da opção desejada:"
    )

# Função para processar mensagens recebidas
def processar_mensagem(incoming_msg, from_number):
    opcoes_validas = ['1', '2', '3', '4', '5']

    # Lógica para opções válidas
    if incoming_msg in opcoes_validas:
        if incoming_msg == '1':
            return cadastrar_numero(from_number)
        elif incoming_msg == '2':
            return adicionar_medicacao(from_number)
        elif incoming_msg == '3':
            return visualizar_medicoes(from_number)
        elif incoming_msg == '4':
            return desativar_alerta(from_number)
        elif incoming_msg == '5':
            return "🚪 Saindo... Até logo!"

    # Mensagem inválida retorna o menu
    return "Olá!\n" + exibir_menu()

# Função para cadastrar número de telefone
def cadastrar_numero(from_number):
    phone_number = f"+55{from_number[-11:]}"  # Pega os últimos 11 dígitos
    register_phone_number(phone_number)
    return f"✅ Número {phone_number} cadastrado com sucesso!\n" + exibir_menu()

# Função para adicionar medicação
def adicionar_medicacao(from_number):
    return (
        "💊 Digite o nome da medicação:"
        "\n⏰ Depois, insira os horários separados por vírgula (HH:MM, HH:MM, ...)."
        "\n🗓️ Escolha a duração do tratamento: 1, 5, 7, 15, 30 ou contínuo."
        "\n👤 Informe se é 'mim' ou o nome de outra pessoa."
    )

# Função para visualizar medicações
def visualizar_medicoes(from_number):
    user, medications = get_data()
    if not user:
        return "📋 Nenhum número de telefone cadastrado. Cadastre um número primeiro."
    msg = f"📱 Número cadastrado: {user[1]}\n💊 Medicações registradas:\n"
    for med in medications:
        destinatario = "você" if med[5] == "mim" else med[5]
        msg += f"- {med[1]} ⏰ Horários: {med[2]} 🗓️ Duração: {med[3]} 👤 Para: {destinatario}\n"
    return msg + exibir_menu()

# Função para desativar alertas
def desativar_alerta(from_number):
    return "🛑 Digite o nome da medicação para desativar o alerta:"

# Configuração do Flask para receber mensagens do Twilio
app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '').strip()
    response_text = processar_mensagem(incoming_msg, from_number)

    # Enviar resposta via Twilio MessagingResponse
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

    while True:
        schedule.run_pending()
        time.sleep(1)
