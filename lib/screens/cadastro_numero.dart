import 'package:flutter/material.dart';

class CadastroNumeroPage extends StatefulWidget {
  const CadastroNumeroPage({Key? key}) : super(key: key);

  @override
  _CadastroNumeroPageState createState() => _CadastroNumeroPageState();
}

class _CadastroNumeroPageState extends State<CadastroNumeroPage> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _numeroController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Cadastrar Número"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _numeroController,
                decoration: const InputDecoration(
                  labelText: "Digite seu número (ex.: 11987654321)",
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.phone,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Por favor, insira um número.";
                  }
                  if (!RegExp(r'^\d{11}$').hasMatch(value)) {
                    return "Número inválido. Deve conter 11 dígitos.";
                  }
                  return null;
                },
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    final numero = _numeroController.text;
                    // Aqui você pode salvar o número no banco de dados ou enviar para a API
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(content: Text("Número $numero cadastrado com sucesso!")),
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
