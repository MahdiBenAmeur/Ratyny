import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class BusinessDetailsScreen extends ConsumerWidget {
  final String businessId;

  const BusinessDetailsScreen({super.key, required this.businessId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // TODO: Fetch business by ID
    return Scaffold(
      appBar: AppBar(
        title: const Text('Business Details'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              height: 200,
              width: double.infinity,
              color: Colors.blue[100],
              child: const Icon(Icons.store, size: 80, color: Colors.blue),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Business Name #$businessId', style: Theme.of(context).textTheme.headlineMedium),
                  const SizedBox(height: 8),
                  const Row(
                    children: [
                      Icon(Icons.star, color: Colors.amber),
                      Text(' 4.5 (120 ratings)'),
                    ],
                  ),
                  const SizedBox(height: 16),
                  const Text('Location: Tunis, Tunisia'),
                  const SizedBox(height: 8),
                  const Text('Website: https://example.com'),
                  const Divider(height: 32),
                  Text('Ratings & Reviews', style: Theme.of(context).textTheme.titleLarge),
                  const SizedBox(height: 16),
                  // Placeholder reviews
                  for (int i = 0; i < 3; i++)
                    ListTile(
                      leading: CircleAvatar(child: Text('U$i')),
                      title: Text('User $i'),
                      subtitle: const Text('Great service! Highly recommended.'),
                      trailing: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [Icon(Icons.star, size: 16, color: Colors.amber), Text('5')],
                      ),
                    ),
                ],
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          // Add rating dialog
        },
        label: const Text('Rate Business'),
        icon: const Icon(Icons.star_rate),
      ),
    );
  }
}
