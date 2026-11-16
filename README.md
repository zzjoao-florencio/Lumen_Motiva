# LÚMEN — Manutenção Inteligente

**Protótipo acadêmico de monitoramento e priorização da manutenção de câmeras rodoviárias.**

Projeto desenvolvido no contexto do **Challenge FIAP × Motiva**, com o objetivo de apoiar operadores na identificação de perda de qualidade das imagens e na escolha das câmeras que exigem atendimento primeiro.

> **Importante:** interface demonstrativa. Não há conexão com o Centro de Controle Operacional da Motiva, câmeras em tempo real ou sensores físicos. Números, localizações, ocorrências, animações e níveis de risco exibidos na plataforma são **dados simulados**, não informações operacionais reais. A análise com Python e sensores é uma **proposta de implementação futura**, explicada na própria interface.

## O problema

Câmeras nas rodovias ajudam equipes de operação a identificar incidentes e acompanhar o tráfego. Mas sujeira, chuva, neblina, teias, obstruções, desfoque e outros fatores podem prejudicar a visibilidade. O problema não é só saber *qual câmera está ruim*: também importa entender *o quanto a falha afeta a segurança do trecho* e se existe outra câmera capaz de cobrir aquela região.

## Nossa solução

O **LÚMEN** reúne indicadores de qualidade, ocorrências e contexto operacional em uma interface de leitura rápida. Ele simula um mecanismo de priorização que considera quatro fatores:

| Fator | O que representa |
| --- | --- |
| Degradação visual | Intensidade da perda de qualidade da imagem |
| Criticidade do trecho | Importância operacional e risco do local monitorado |
| Histórico de falhas | Frequência de problemas anteriores da câmera |
| Cobertura alternativa | Existência ou ausência de outra câmera próxima |

O protótipo calcula uma **pontuação ponderada demonstrativa**, permitindo organizar uma fila de atenção e apresentar motivos para o operador priorizar o atendimento.

## Funcionalidades do protótipo

- **Dashboard:** resumo geral, gráficos, câmera de referência limpa, mapa e exemplos de câmeras com problemas.
- **Monitoramento:** pesquisa, filtros, visualização de câmeras e indicadores de qualidade.
- **Mapa Operacional:** visualização **ilustrativa** da rede, com marcadores coloridos por prioridade.
- **Priorização Inteligente:** lista ordenada por score, com pesos ajustáveis durante a demonstração.
- **Câmeras Críticas:** seis casos exemplificados, cada um com causa, motivo da prioridade, impacto operacional e ação recomendada.
- **Ocorrências:** lista e atualização demonstrativa de status.
- **Histórico e Relatórios:** gráficos e elementos ilustrativos para acompanhar degradação e manutenção.
- **Como identificamos:** explicação da arquitetura proposta com **Python, OpenCV e sensores**; **não é um pipeline de análise implementado neste repositório**.
- **Configurações e temas:** alternância entre roxo e branco; a preferência do tema pode ser guardada localmente no navegador.

A interface exibe um **cenário simulado de 328 câmeras**, das quais 276 aparecem como operacionais, 38 com degradação e 14 críticas. **Somente 12 câmeras têm exemplos visuais individuais na interface**; a aba de câmeras críticas apresenta seis estudos demonstrativos. Isso **não significa** que existem 328 transmissões ou GIFs reais.

## Como executar

**Opção 1 — arquivo local:** baixe o projeto e abra `index.html` em um navegador atualizado.

**Opção 2 — servidor local (recomendado para testar):**

```bash
python -m http.server 8000
```

Depois, acesse `http://localhost:8000`.

Não é necessário instalar dependências de Python para abrir o site. O arquivo HTML contém imagens e animações incorporadas, mas usa **Google Fonts**, **Chart.js** e **Lucide** via CDN; portanto, a aparência completa pode depender de conexão com a internet. Há um desenho simplificado de gráficos como fallback caso Chart.js não carregue.

## Publicar com GitHub Pages

1. Crie um repositório no GitHub e envie os arquivos da pasta do projeto, **incluindo `index.html` na raiz**.
2. Acesse **Settings → Pages**.
3. Em *Build and deployment*, selecione **Deploy from a branch** e a branch `main`, pasta `/ (root)`.
4. Aguarde o GitHub Pages disponibilizar a URL da página.

> O GitHub Pages publica conteúdo estático: não executa Python, não conecta sensores nem protege dados que foram escritos no HTML. Não publique URLs privadas de câmeras, credenciais ou dados reais da operação.

## Estrutura do repositório

```text
LUMEN_GitHub/
├── index.html                 # Interface demonstrativa completa
├── README.md                  # Apresentação e instruções
├── SECURITY.md                # Política e boas práticas de segurança
├── PRIVACY.md                 # Informações sobre dados e privacidade
├── CONTRIBUTING.md            # Orientações para contribuir
├── .gitignore                 # Arquivos que não devem ir para o Git
├── .gitattributes             # Tratamento de arquivos no Git
├── .github/workflows/security-check.yml
└── scripts/security_check.py  # Verificações automáticas básicas
```

## Como a detecção com Python poderia funcionar

Em uma evolução do projeto, um serviço backend em Python poderia: (1) capturar quadros de câmeras autorizadas, (2) medir nitidez, contraste e obstruções com OpenCV, (3) cruzar esses dados com telemetria de sensores climáticos e equipamentos, (4) calcular um score de risco e (5) encaminhar alertas à interface. **Nenhuma dessas integrações reais está presente nesta versão.**

## Segurança e privacidade

Leia [`SECURITY.md`](SECURITY.md) e [`PRIVACY.md`](PRIVACY.md) antes de publicar. A verificação automatizada do repositório é **básica** e não substitui auditoria. **Não** adicione tokens, senhas, imagens privadas, dados pessoais ou credenciais de câmeras ao código.

## Tecnologias

**HTML5, CSS3, JavaScript, Chart.js, Lucide Icons e Google Fonts.** Python e OpenCV são parte da **proposta técnica**, não dependências do protótipo executável.

## Créditos

Projeto acadêmico do **Challenge FIAP × Motiva**. Logos e nomes institucionais pertencem aos respectivos titulares; a menção às marcas identifica o contexto acadêmico e **não constitui produto oficial nem endosso**. Imagens e animações de rodovias usadas no protótipo são ilustrativas.

**Licença:** ainda não foi escolhida uma licença de distribuição para este repositório. Antes de adotar uma licença aberta, verifique os direitos de uso do material visual e a autorização dos integrantes do grupo.
