#!/bin/bash

DATA=$(date +%Y%m%d_%H%M%S)

PROJETO="/opt/securechain"
PASTA_DOCS="$PROJETO/documentos"
PASTA_BACKUP="$PROJETO/backup"

ARQUIVO="backup_$DATA.tar.gz"
ARQUIVO_CRIPTO="$ARQUIVO.enc"

mkdir -p "$PASTA_BACKUP"

tar -czf "$PASTA_BACKUP/$ARQUIVO" "$PASTA_DOCS"

openssl enc -aes-256-cbc \
-pbkdf2 \
-iter 100000 \
-salt \
-in "$PASTA_BACKUP/$ARQUIVO" \
-out "$PASTA_BACKUP/$ARQUIVO_CRIPTO" \
-k SecureChain123

rm "$PASTA_BACKUP/$ARQUIVO"

echo "[$DATA] Backup executado com sucesso" \
>> "$PASTA_BACKUP/backup.log"

echo "$PASTA_BACKUP/$ARQUIVO_CRIPTO"
