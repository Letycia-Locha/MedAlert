import 'package:flutter/material.dart';

class DesativarAlertasPage extends StatelessWidget {
  const DesativarAlertasPage({Key? key}) : super(key: key);

  // Simulando dados cadastrados
  final List<Map<String, String>> _medicacoes = const [
    {
      "nome": "Paracetamol",
      "horarios": "08:00, 12:00, 20:00",
      "duracao": "7 dias",
    },
    {
      "nome": "Ibuprofeno",
      "horarios": "10:00, 22:00",
      "duracao": "contínuo",
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Desativar Alertas"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: _medicacoes.isEmpty
            ? const Center(
                child: Text(
                  "Nenhuma medicação cadastrada para desativar.",
                  style: TextStyle(fontSize: 16),
                ),
              )
            : ListView.builder(
                itemCount: _medicacoes.length,
                itemBuilder: (context, index) {
                  final medicacao = _medicacoes[index];
                  return Card(
                    margin: const EdgeInsets.symmetric(vertical: 8),
                    child: ListTile(
                      title: Text(
                        medicacao["nome"]!,
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      subtitle: Text(
                          "Horários: ${medicacao["horarios"]}\nDuração: ${medicacao["duracao"]}"),
                      trailing: IconButton(
                        icon: const Icon(Icons.delete, color: Colors.red),
                        onPressed: () {
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              content: Text(
                                  'Alerta para "${medicacao["nome"]}" desativado com sucesso!'),
                            ),
                          );
                        },
                      ),
                    ),
                  );
                },
              ),
      ),
    );
  }
}