from registro_numeros import init_db, register_phone_number, register_medication, get_data, remove_medication
import schedule
import time
from twilio.rest import Client
import re
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Inicializa o banco de dados
init_db()

# Configurações do Twilio
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Menu para gerenciar o aplicativo
while True:
    print("\n🌟 Bem-vindo ao MedAlert! 🌟")
    print("📱 1. Cadastrar ou atualizar número de telefone")
    print("💊 2. Adicionar medicação")
    print("📋 3. Visualizar medicações")
    print("🛑 4. Desativar alerta de uma medicação")
    print("🚪 5. Sair")

    opcao = input("Escolha uma opção (digite o número correspondente): ")

    if opcao == '1':
        # Cadastro ou atualização do número de telefone
        while True:
            phone_number = input("📱 Digite seu número no formato DDDNÚMERO (sem o +55, ex.: 11987654321): ")
            if re.fullmatch(r'\d{11}', phone_number):  # Validação de 11 dígitos
                phone_number = f"+55{phone_number}"  # Adiciona o prefixo +55 automaticamente
                register_phone_number(phone_number)  # Salva ou atualiza no banco
                print(f"✅ Número {phone_number} cadastrado com sucesso!")
                break
            else:
                print("❌ Número inválido! Certifique-se de inserir 11 dígitos (ex.: 11987654321).")

    elif opcao == '2':
        # Adicionar medicação
        name = input("💊 Digite o nome da medicação (ou 'sair' para finalizar): ")
        if name.lower() == 'sair':
            continue

        # Pergunta se a medicação é para o próprio usuário ou para terceiros
        responsavel = input("👤 A medicação é para você ou para outra pessoa? (digite 'mim' ou o nome da pessoa): ")
        if responsavel.lower() == 'mim':
            responsavel = "mim"

        horarios = []
        while True:
            horario_medicacao = input("⏰ Digite um horário para a medicação (formato HH:MM, ou 'pronto' para finalizar): ")
            if horario_medicacao.lower() == 'pronto':
                break
            if re.fullmatch(r'([01]\d|2[0-3]):([0-5]\d)', horario_medicacao):  # Validação de horário
                horarios.append(horario_medicacao)
                print(f"✅ Horário {horario_medicacao} adicionado.")
            else:
                print("❌ Horário inválido! Insira no formato HH:MM (ex.: 08:00).")

        duracao = input("🗓️ Informe a duração do tratamento em dias (1, 5, 7, 15, 30, contínuo): ")
        while duracao not in ['1', '5', '7', '15', '30', 'contínuo']:
            print("❌ Opção inválida! Escolha entre: 1 dia, 5 dias, 7 dias, 15 dias, 30 dias ou contínuo.")
            duracao = input("🗓️ Informe a duração do tratamento: ")

        register_medication(name, ','.join(horarios), duracao, responsavel)
        print(f"✅ Medicação '{name}' para '{responsavel}' cadastrada com sucesso!")

    elif opcao == '3':
        # Visualizar medicações
        user, medications = get_data()
        if user is None:
            print("📋 Nenhum número de telefone cadastrado.")
        else:
            print(f"\n📱 Número de telefone cadastrado: {user[1]}")
            print("💊 Medicações registradas:")
            for med in medications:
                destinatario = "você" if med[5] == "mim" else med[5]  # Mostra "você" para "mim"
                print(f"- {med[1]} ⏰ Horários: {med[2]} 🗓️ Duração: {med[3]} 👤 Para: {destinatario}")

    elif opcao == '4':
        # Desativar alerta
        name = input("🛑 Digite o nome da medicação para desativar o alerta: ")
        remove_medication(name)
        print(f"✅ Alerta para '{name}' desativado com sucesso!")

    elif opcao == '5':
        print("🚪 Saindo... Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")

# Função para enviar alertas
def send_alert(medication, phone_number):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{phone_number}',
        body=f"💊 Alerta de Medicação: Hora de tomar {medication}!"
    )
    print(f"✅ Mensagem enviada para {phone_number}: {message.sid}")

# Agendar os alertas
def schedule_alerts():
    user, medications = get_data()
    for med in medications:
        horarios = med[2].split(',')  # Divide os horários
        for horario in horarios:
            schedule.every().day.at(horario).do(send_alert, medication=med[1], phone_number=user[1])

schedule_alerts()

# Executar o agendamento
print("\n⏰ Alertas agendados. Fique tranquilo! Você será avisado no momento de tomar sua medicação.")
while True:
    schedule.run_pending()
    time.sleep(1)