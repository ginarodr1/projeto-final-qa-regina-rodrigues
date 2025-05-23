import unittest

class Calculadora:
    """Classe que implementa operações básicas de uma calculadora"""
    
    def somar(self, a, b):
        """Retorna a soma de dois números"""
        return a + b
    
    def subtrair(self, a, b):
        """Retorna a diferença entre dois números"""
        return a - b
    
    def multiplicar(self, a, b):
        """Retorna o produto de dois números"""
        return a * b
    
    def dividir(self, a, b):
        """
        Retorna a divisão de a por b
        Levanta ValueError se b for zero
        """
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def potencia(self, a, b):
        """Retorna a elevado à potência de b"""
        return a ** b
    
    def raiz_quadrada(self, a):
        """
        Retorna a raiz quadrada de a
        Levanta ValueError se a for negativo
        """
        if a < 0:
            raise ValueError("Não é possível calcular raiz de número negativo")
        return a ** 0.5


class TestCalculadora(unittest.TestCase):
    """Classe de testes unitários para a Calculadora"""
    
    def setUp(self):
        """Inicializa a calculadora antes de cada teste"""
        self.calc = Calculadora()
    
    def test_somar(self):
        """Testa a operação de soma"""
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
        self.assertEqual(self.calc.somar(0, 0), 0)
    
    def test_subtrair(self):
        """Testa a operação de subtração"""
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.subtrair(10, 15), -5)
    
    def test_multiplicar(self):
        """Testa a operação de multiplicação"""
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 5), -10)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)
    
    def test_dividir(self):
        """Testa a operação de divisão"""
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.333333, places=6)
        
        # Teste de exceção
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
    
    def test_potencia(self):
        """Testa a operação de potência"""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(10, 1), 10)
    
    def test_raiz_quadrada(self):
        """Testa a operação de raiz quadrada"""
        self.assertEqual(self.calc.raiz_quadrada(9), 3)  # Teste exato para quadrado perfeito
        self.assertAlmostEqual(self.calc.raiz_quadrada(2), 1.414213562, places=6)  # Ajuste na precisão
        
        # Teste de exceção
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-1)


# Execução dos testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
