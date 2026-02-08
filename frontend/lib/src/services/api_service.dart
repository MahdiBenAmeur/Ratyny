import 'package:dio/dio.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final dioProvider = Provider<Dio>((ref) {
  final dio = Dio();
  // For Android Emulator -> 10.0.2.2
  // For Physical Device -> Your PC's IP Address
  // For Web -> localhost:8000 (with proxy usually)
  dio.options.baseUrl = 'http://10.0.2.2:8000/api/v1'; 
  return dio;
});
