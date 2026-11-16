# Política de Segurança — LÚMEN

## Escopo

Este repositório contém um **protótipo acadêmico estático**. As câmeras, o mapa, as ocorrências, os sensores e as métricas são demonstrações. **Não existe autenticação, controle de acesso, backend ou integração segura com câmeras reais.** A ausência dessas funções é uma limitação importante, não uma garantia de segurança.

## Reportar uma vulnerabilidade

**Não divulgue credenciais ou dados de terceiros em uma issue pública.** Utilize o mecanismo privado **GitHub → Security → Advisories → Report a vulnerability**, se estiver habilitado pelo responsável pelo repositório. Caso não esteja, contate os mantenedores por um canal privado previamente combinado. Nenhum e-mail institucional de segurança foi designado neste projeto.

Ao reportar, informe uma descrição, como reproduzir o problema, o impacto possível e, se aplicável, uma sugestão de correção. Não inclua dados reais ou imagens privadas das rodovias.

## Antes de publicar

- Nunca armazene senhas, tokens de API, chaves privadas, cookies de sessão, endereços internos ou credenciais RTSP no HTML ou no histórico do Git.
- Use apenas imagens e localizações **autorizadas e demonstrativas**. Evite dados pessoais, placas legíveis reais e rostos identificáveis.
- Não considere `localStorage` armazenamento seguro: o protótipo usa esse recurso apenas para a preferência visual de tema.
- Bibliotecas, fontes e scripts externos devem usar HTTPS e versões revisadas. O projeto atual carrega recursos de **Google Fonts** e do CDN **jsDelivr**.
- Antes de integrar câmeras reais, implemente autenticação e autorização, tratamento seguro de credenciais no servidor, HTTPS, segmentação de rede, logs, políticas de retenção, proteção contra acesso indevido, validação de dados e testes de segurança.
- A verificação automatizada em `.github/workflows/security-check.yml` faz apenas checagens **heurísticas**. Não prova ausência de vulnerabilidades.

## Se um segredo for publicado por engano

Revogue ou rotacione a credencial imediatamente no serviço de origem. Remova-a do código, analise o histórico do repositório, investigue possíveis acessos e siga o procedimento aplicável da organização. Apagar apenas o arquivo atual **não** remove o segredo do histórico do Git.

## Escopo da automação

O script `scripts/security_check.py` procura padrões comuns de credenciais e verifica alguns pontos de higiene do repositório. Ele **não** é antivírus, scanner de dependências nem auditoria de código JavaScript. Em caso de falso positivo ou novo risco, revise o script de forma documentada.
