import 'package:flutter/material.dart';
import 'screens/cadastro_numero.dart';
import 'screens/adicionar_medicacao.dart';
import 'screens/visualizar_medicacoes.dart';
import 'screens/desativar_alertas.dart';

void main() {
  runApp(const MedAlertApp());
}

class MedAlertApp extends StatelessWidget {
  const MedAlertApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MedAlert',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MedAlert'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const CadastroNumeroPage(),
                  ),
                );
              },
              child: const Text('Cadastrar Número'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const AdicionarMedicacaoPage(),
                  ),
                );
              },
              child: const Text('Adicionar Medicação'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const VisualizarMedicacoesPage(),
                  ),
                );
              },
              child: const Text('Visualizar Medicações'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const DesativarAlertasPage(),
                  ),
                );
              },
              child: const Text('Desativar Alertas'),
            ),
          ],
        ),
      ),
    );
  }
}
