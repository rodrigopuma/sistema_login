🗂 Escopo do Projeto: Sistema de Login em Python
🎯 Objetivo Geral
Criar um sistema de cadastro e login de usuários, com armazenamento local simples (por exemplo, em um arquivo .txt) e utilizando funções para organização do código.

📌 Funcionalidades Principais
Menu Inicial

[1] Cadastrar novo usuário

[2] Fazer login

[3] Sair

Cadastro de Usuário

Usuário informa:

Nome de usuário (único)

Senha

Salvar os dados em um arquivo usuarios.txt no formato:

Login

Usuário digita login e senha

Verificação simples:

Se usuário e senha estão no arquivo, mostrar mensagem de sucesso

Caso contrário, mensagem de erro

Validações Simples

Impedir cadastro de usuário com nome repetido

Impedir campos vazios

Mostrar mensagens claras para o usuário

🧠 Conteúdo Python que você vai praticar
Funções (def)

Leitura e escrita em arquivos (open, readlines, write)

Manipulação de strings (split, strip)

Estruturas de decisão (if, else)

Loops (while, for)

Menu com input() e print()

🔐 Extras opcionais (se quiser deixar mais robusto)
Criptografar a senha com hashlib (se estiver curioso)

Limitar número de tentativas de login

Criar "sessão" fictícia (apenas uma mensagem de "Bem-vindo, [nome]")

📁 Estrutura de arquivos
bash
login_system/
│
├── main.py # Seu script principal
└── usuarios.txt # Arquivo com os dados salvos

🧩 Organização sugerida com funções
python
def mostrar_menu():
...

def cadastrar_usuario():
...

def fazer_login():
...

def usuario_existe(nome_usuario):
...

def ler_usuarios():
...

def salvar_usuario(nome, senha):
...
