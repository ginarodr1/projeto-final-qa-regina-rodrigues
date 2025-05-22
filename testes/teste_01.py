# teste 1

import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para todos os testes"""
        self.calc = Calculadora()
    
    # Teste 1: Operações básicas
    def test_operacoes_basicas(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.multiplicar(4, 3), 12)
        self.assertAlmostEqual(self.calc.dividir(10, 3), 3.333333, places=6)
    
    # Teste 2: Casos especiais/erros
    def test_casos_especiais(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
        
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-1)
    
    # Teste 3: Operações avançadas
    def test_operacoes_avancadas(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertAlmostEqual(self.calc.raiz_quadrada(16), 4)
        self.assertEqual(self.calc.potencia(5, 0), 1)

# Configuração especial para o Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
