import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class HomeScreen extends ConsumerWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ratyny Feed'),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
              // Search modal
            },
          ),
          IconButton(
            icon: const Icon(Icons.account_circle),
            onPressed: () {},
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: 10, // Placeholder count
        itemBuilder: (context, index) {
          // Placeholder incidents
          return Card(
            margin: const EdgeInsets.only(bottom: 16),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      CircleAvatar(child: Text('U$index')),
                      const SizedBox(width: 8),
                      Text('User $index', style: Theme.of(context).textTheme.titleSmall),
                      const Spacer(),
                      const Text('2h ago', style: TextStyle(color: Colors.grey)),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text('Incident report about a business scam... #$index',
                      style: Theme.of(context).textTheme.bodyMedium),
                  const SizedBox(height: 12),
                  Container(
                    height: 200,
                    width: double.infinity,
                    color: Colors.grey[300],
                    child: const Center(child: Icon(Icons.image, size: 48, color: Colors.grey)),
                  ),
                  const SizedBox(height: 8),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      TextButton.icon(
                        icon: const Icon(Icons.comment),
                        label: const Text('Comments'),
                        onPressed: () {},
                      ),
                      TextButton.icon(
                        icon: const Icon(Icons.warning_amber),
                        label: const Text('Report'),
                        onPressed: () {},
                      ),
                    ],
                  ),
                ],
              ),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.add),
      ),
    );
  }
}
