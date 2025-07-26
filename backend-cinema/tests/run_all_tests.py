import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'test_services'), pattern="test_*.py"))

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(suite)
    
    print(f"\n{'='*60}")
    print(f"RESUMO DOS TESTES CRUD:")
    print(f"Total de testes executados: {result.testsRun}")
    print(f"Sucessos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Falhas: {len(result.failures)}")
    print(f"Erros: {len(result.errors)}")
    print(f"Taxa de sucesso: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print(f"{'='*60}")
