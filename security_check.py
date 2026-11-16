"""Verificações simples para evitar publicação acidental de segredos.

Não substitui ferramenta especializada de segurança.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [ROOT / 'index.html', ROOT / 'README.md', ROOT / 'SECURITY.md',
              ROOT / 'PRIVACY.md', ROOT / 'CONTRIBUTING.md']
BLOCKED_PATHS = [ROOT / '.env', ROOT / 'credentials.json', ROOT / 'secrets.json']
PATTERNS = {
    'chave privada': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'token GitHub': re.compile(r'\bgh(?:p|o|u|s|r)_[A-Za-z0-9]{20,}\b'),
    'token GitHub fine-grained': re.compile(r'\bgithub_pat_[A-Za-z0-9_]{20,}\b'),
    'chave AWS': re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    'senha em atribuição': re.compile(r'(?i)\b(?:password|passwd|secret_key|api_key|access_token)\s*[:=]\s*[\"\'](?!example|placeholder|change-me)[^\"\']{8,}[\"\']'),
}


def main() -> int:
    warnings = []
    for path in BLOCKED_PATHS:
        if path.exists():
            warnings.append(f'Arquivo sensível presente: {path.relative_to(ROOT)}')

    for path in TEXT_FILES:
        if not path.is_file():
            warnings.append(f'Arquivo obrigatório ausente: {path.relative_to(ROOT)}')
            continue
        text = path.read_text(encoding='utf-8')
        # O HTML contém grandes imagens e GIFs em data:base64.
        # Removê-los da busca reduz falsos positivos; segredos podem, ainda assim,
        # ser escondidos em mídia e não serão detectados por este script.
        if path.suffix == '.html':
            text = re.sub(r'data:(?:image|video)/[^\"\']+;base64,[A-Za-z0-9+/=]+',
                          '[MÍDIA INCORPORADA]', text)
        for name, pattern in PATTERNS.items():
            if pattern.search(text):
                warnings.append(f'Padrão suspeito ({name}) em {path.relative_to(ROOT)}')

    if warnings:
        print('VERIFICAÇÃO NÃO APROVADA:')
        for item in warnings:
            print(' -', item)
        return 1
    print('Verificação básica concluída sem padrões óbvios de segredo.')
    print('Atenção: isso não garante que o site esteja seguro.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
