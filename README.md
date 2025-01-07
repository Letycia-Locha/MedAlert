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
   ```bash
   git clone https://github.com/seu-usuario/MedAlert.git
   cd MedAlert
