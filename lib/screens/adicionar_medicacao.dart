import 'package:flutter/material.dart';

class AdicionarMedicacaoPage extends StatefulWidget {
  const AdicionarMedicacaoPage({Key? key}) : super(key: key);

  @override
  _AdicionarMedicacaoPageState createState() => _AdicionarMedicacaoPageState();
}

class _AdicionarMedicacaoPageState extends State<AdicionarMedicacaoPage> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _nomeMedicacaoController = TextEditingController();
  final TextEditingController _horariosController = TextEditingController();
  final TextEditingController _duracaoController = TextEditingController();
  String? _responsavel; // Variável para armazenar o responsável

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Adicionar Medicação"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _nomeMedicacaoController,
                decoration: const InputDecoration(
                  labelText: "Nome da medicação",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Por favor, insira o nome da medicação.";
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _horariosController,
                decoration: const InputDecoration(
                  labelText: "Horários (ex.: 08:00, 12:00, 18:00)",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Por favor, insira os horários.";
                  }
                  if (!RegExp(r'^([01]?\d|2[0-3]):([0-5]\d)(,\s*([01]?\d|2[0-3]):([0-5]\d))*$')
                      .hasMatch(value)) {
                    return "Horários inválidos. Use o formato HH:MM e separe por vírgulas.";
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _duracaoController,
                decoration: const InputDecoration(
                  labelText: "Duração (em dias ou 'contínuo')",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Por favor, insira a duração.";
                  }
                  if (value != 'contínuo' && !RegExp(r'^\d+$').hasMatch(value)) {
                    return "Duração inválida. Use números ou 'contínuo'.";
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              DropdownButtonFormField<String>(
                value: _responsavel,
                decoration: const InputDecoration(
                  labelText: "A medicação é para quem?",
                  border: OutlineInputBorder(),
                ),
                items: const [
                  DropdownMenuItem(value: "mim", child: Text("Para mim")),
                  DropdownMenuItem(value: "outro", child: Text("Outra pessoa")),
                ],
                onChanged: (value) {
                  setState(() {
                    _responsavel = value;
                  });
                },
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Por favor, selecione o responsável.";
                  }
                  return null;
                },
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    final nome = _nomeMedicacaoController.text;
                    final horarios = _horariosController.text;
                    final duracao = _duracaoController.text;
                    final responsavel = _responsavel == "mim" ? "Você" : "Outra pessoa";

                    // Aqui você pode salvar os dados no banco de dados ou enviar para a API
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text(
                          "Medicação '$nome' adicionada para $responsavel!\nHorários: $horarios\nDuração: $duracao",
                        ),
                      ),
                    );
                  }
                },
                child: const Text("Salvar"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
