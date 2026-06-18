Projeto Auditoria Blockchain - Desenvolvido para a disciplina de Segurança de sistemas computacionais

Integrantes:
- THIAGO RODRIGUES FONSECA MARTINS
- RAFAEL ANTONIO SCHIRNER DARGONI
- VINICIUS AUGUSTO CORREA LEITE
- VINICIUS COTRIM AZZI

## Descrição

SecureChain Audit é uma plataforma de auditoria baseada em blockchain desenvolvida em Python para ambiente Debian Linux. O sistema tem como objetivo garantir rastreabilidade, integridade e segurança dos eventos registrados no ambiente monitorado.

## Funcionalidades

* Autenticação de usuários com bcrypt
* Blockchain para registro de eventos
* Monitoramento de integridade utilizando SHA-256
* Detecção de criação, alteração e remoção de arquivos
* Auditoria do sistema operacional
* Backup seguro com criptografia AES-256
* Controle de acesso baseado em usuários e grupos Linux

## Tecnologias Utilizadas

* Python 3
* Debian 13
* Bash Script
* OpenSSL
* SHA-256
* bcrypt
* Git e GitHub

## Estrutura do Projeto

* blockchain: gerenciamento da blockchain
* autenticacao: controle de usuários
* monitoramento: integridade dos arquivos
* auditoria: geração de relatórios
* backup: backup criptografado
* documentos: arquivos monitorados

## Como Executar

```bash
cd /opt/securechain
python3 main.py
```

