def mostrar_menu():
    print('\n[1] Cadastrar novo usuário\n'
          '[2] Fazer login\n'
          '[0] Sair\n')
    
def validar_s_n(obj):
    if obj in ['S', 'N', 's', 'n']:
        return True
    else:
        return False

def escolher_menu():
    choice = int(input('Escolha qual opção você deseja: '))
    while choice not in [0,1,2]:
        choice = int(input('Escolha inválida coloque alguma opção do menu: '))
    return choice

def ler_usuarios():
    usuarios = []
    with open("usuarios.txt", "r") as arquivo: # "r" = read (ler os usuarios)
        for linha in arquivo:
            nome, senha = linha.strip().split(';')
            usuarios.append((nome, senha))
    return usuarios

def salvar_usuario(username, senha):
    with open("usuarios.txt", "a") as arquivo: # "a" = append (adicionar ao final)
        arquivo.write(f'{username};{senha}\n')
    print(f'Usúario "{username}" cadastrado com a senha {len(senha) * '*'}')

def usuario_existe(username_prompt):
    usuarios = ler_usuarios()
    for username, senha in usuarios:    
        if username_prompt in 'usuarios.txt':
            return True
        else:
            return False
    
def cadastrar_usuario(username=None, senha=None):
    if username is None:
        username = input('Digite seu nome de usuário: ').strip()
    if senha is None:
        senha = input('Digite sua senha: ').strip()
    return username, senha

def fazer_login(username_prompt=None, senha_prompt=None):
    global username, senha
    usuarios = ler_usuarios()
    if username_prompt is None:
        username_prompt = input('Digite seu nome de usuário: ').strip()
    if senha_prompt is None:
        senha_prompt = input('Digite sua senha: ').strip()
    for username, senha in usuarios:
        if username_prompt == username and senha_prompt == senha:
            print('Login válido')
