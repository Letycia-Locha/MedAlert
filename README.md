# 🌟 MedAlert 🌟

O **MedAlert** é um sistema de gerenciamento de medicações desenvolvido em Python, que utiliza o WhatsApp para enviar lembretes automáticos. Ele ajuda os usuários a nunca esquecerem de tomar seus remédios no horário correto. Ideal para quem gerencia seus próprios medicamentos ou os de terceiros.

---

## 📋 Funcionalidades

- 📱 **Cadastrar/Atualizar Número de Telefone**: Registre o número para receber lembretes via WhatsApp.
- 💊 **Adicionar Medicações**: Inclua nome, horários, duração do tratamento e o responsável pela medicação.
- 📋 **Visualizar Medicações**: Liste todas as medicações cadastradas, com detalhes de horários e destinatários.
- 🛑 **Desativar Alertas**: Remova alertas de medicações específicas.
- ⏰ **Envio de Alertas Automáticos**: Receba lembretes no WhatsApp nos horários programados.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para backend.
- **Flask**: Framework web para gerenciar as interações com o WhatsApp.
- **Twilio API**: Serviço para envio e recebimento de mensagens via WhatsApp.
- **SQLite**: Banco de dados para armazenar números de telefone e informações de medicações.
- **dotenv**: Gerenciamento seguro de variáveis de ambiente.
- **schedule**: Agendamento de tarefas para envio automático de alertas.

---

## 🚀 Como Configurar e Executar

1. **Clone o repositório**:
 -  ```bash
 - git clone https://github.com/seu-usuario/MedAlert.git
 - cd MedAlert
2. **Configure o ambiente virtual**:
 -   python -m venv venv
 -  source venv/bin/activate # No Windows: venv\Scripts\activate
3. **Instale as dependências**:
 -  pip install -r requirements.txt
4. **Crie um arquivo .env na raiz do projeto**:
 -   ACCOUNT_SID=seu_account_sid
 -   AUTH_TOKEN=seu_auth_token
 -   TWILIO_PHONE=seu_numero_twilio
5. **Inicie o Servidor**:
 -   python server.py
6. **Configure o Ngrok para expor o servidor local ao Twilio:**:
 -   lembre-se de criar uma conta no Ngrok antes de utiliza-lo e fazer o download do mesmo
 -   ngrok http 8080
7. **Teste o sistema enviando uma mensagem para o número Twilio no WhatsApp.**

## 📝 Estrutura do Projeto
MedAlert/
- ├── app.py               # Código do fluxo principal do app
- ├── server.py            # Integração com Twilio e WhatsApp
- ├── registro_numeros.py  # Funções de manipulação do banco de dados
- ├── database.db          # Banco de dados SQLite
- ├── requirements.txt     # Dependências do projeto
- ├── .env                 # Variáveis de ambiente (não versionado)
- └── venv/                # Ambiente virtual Python

## 🔒 Segurança
  -  Certifique-se de *NUNCA* versionar informações sensíveis como ACCOUNT_SID, AUTH_TOKEN ou TWILIO_PHONE. Utilize o arquivo .env para proteger esses dados.
**Adicione o seguinte ao seu .gitignore:**
   - .env
   - *.db
   - venv/

# 🤝 Contribuições
  - Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou enviar um Pull Request. 


