# projeto-final-qa-regina-rodrigues

1. Apresentação
Nome completo: Regina Rodrigues dos Santos
Curso e semestre: GTI5NA - 5° semestre

Durante a disciplina de Quality Assurance (QA), pude aprender a importância dos testes no desenvolvimento de software, garantindo que os sistemas funcionem corretamente e atendam às expectativas dos usuários. Aprendi a criar testes automatizados, analisar resultados e aplicar métricas de qualidade, o que me ajudou a entender como prevenir falhas antes que elas cheguem ao ambiente de produção.


2. O que é Quality Assurance (QA)?
Quality Assurance (QA) é um conjunto de processos que garantem a qualidade de um software desde o seu desenvolvimento até a entrega final. Enquanto os testes (Quality Control - QC) verificam se o produto está funcionando corretamente, o QA foca em prevenir erros, estabelecendo padrões e metodologias para evitar defeitos.

Imagine um carro sendo fabricado: o QA é como um engenheiro que define os procedimentos para garantir que todas as peças sejam produzidas corretamente, enquanto o QC seria o inspetor que testa o carro pronto antes de ele sair da fábrica. No desenvolvimento de software, o QA ajuda a evitar bugs, reduzir retrabalho e entregar um produto mais confiável.


3. Conceitos Aprendidos Durante o Semestre
Qualidade em software e cultura de qualidade
Aprendi que qualidade não é apenas testar no final, mas sim integrar boas práticas em todo o ciclo de desenvolvimento. Uma cultura de qualidade envolve toda a equipe, desde desenvolvedores até gestores, priorizando testes contínuos e feedback rápido.

Tipos de testes
Testes unitários: Verificam funções isoladas (ex: uma calculadora).
Testes de integração: Checam como módulos funcionam juntos.
Testes de sistema: Validam o software como um todo.
Testes de aceitação: Confirmam se o sistema atende aos requisitos do cliente.
Testes de regressão: Garantem que novas alterações não quebrem funcionalidades existentes.
Testes exploratórios: Avaliações manuais para descobrir problemas não previstos.

Planejamento de testes
Aprendi a definir critérios de aceitação, criar planos de teste e elaborar casos de teste claros e objetivos, garantindo uma cobertura eficiente.

Ferramentas utilizadas
Google Colab: Para escrever e executar testes em Python.
GitHub: Versionamento e armazenamento de códigos de teste.
Bibliotecas Python: unittest, requests, pytest.

Automação de testes e CI/CD
Entendi como integrar testes automatizados em pipelines de CI/CD (Integração Contínua/Entrega Contínua), permitindo verificações rápidas a cada atualização no código.

Monitoramento e controle de qualidade
Aprendi a usar métricas (como cobertura de testes e taxa de falhas) e ferramentas de rastreamento de bugs para melhorar a qualidade do software continuamente.


4. Ferramentas e Sites Utilizados
Google Colab → Para testes em Python.
GitHub → Armazenamento e versionamento de código.
DeepSeek → Geração de código


5. Explicação dos Testes Entregues
✅ Teste 01 – Calculadora Básica (Unitário)
Biblioteca: unittest
Objetivo: Verificar a importação correta da classe Calculadora
Resultado esperado: Importação bem-sucedida
Resultado obtido:
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-3-cdbb58d2e5fc> in <cell line: 0>()
      1 import unittest
----> 2 from calculadora import Calculadora
      3 
      4 class TestCalculadora(unittest.TestCase):
      5     def setUp(self):

ModuleNotFoundError: No module named 'calculadora'

---------------------------------------------------------------------------
NOTE: If your import is failing due to a missing package, you can
manually install dependencies using either !pip or !apt.

To view examples of installing some common dependencies, click the
"Open Examples" button below.
---------------------------------------------------------------------------

✅ Teste 02 – API Status Check (Integração)
Biblioteca: unittest
Objetivo: Validar cálculo de raiz quadrada com 6 casas decimais
Resultado esperado: 1.414213
Resultado obtido:
...F..
======================================================================
FAIL: test_raiz_quadrada (__main__.TestCalculadora.test_raiz_quadrada)
Testa a operação de raiz quadrada
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython-input-4-04dda3e5a74d>", line 84, in test_raiz_quadrada
    self.assertAlmostEqual(self.calc.raiz_quadrada(2), 1.414213, places=6)
AssertionError: 1.4142135623730951 != 1.414213 within 6 places (5.623730952031281e-07 difference)

----------------------------------------------------------------------
Ran 6 tests in 0.012s

FAILED (failures=1)

✅ Teste 03 – Validação de Formulário (Sistema)
Biblioteca: unittest
Objetivo: Verificar todas operações após correções
Resultado obtido:
......
----------------------------------------------------------------------
Ran 6 tests in 0.006s

OK


6. Conclusão Final
O conceito mais importante que aprendi foi que QA não é apenas encontrar bugs, mas prevenir que eles aconteçam. Isso mudou minha visão sobre desenvolvimento de software, mostrando que testes devem ser parte do processo desde o início.
No futuro profissional, vejo a área de QA como essencial, especialmente com a crescente demanda por softwares confiáveis e seguros. A ferramenta que mais me chamou a atenção foi o Google Colab, por permitir testes rápidos em Python sem configurações complexas.
Esta disciplina me mostrou que qualidade é um trabalho contínuo e colaborativo, e pretendo aplicar esses conhecimentos tanto em projetos pessoais quanto profissionais. 🚀
