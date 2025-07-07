from functions import menu, validar_s_n, cadastrar_usuario, fazer_login

def loop(loop='On'):
    while loop == 'On':
        choice = menu()
        
        if choice == 1: # Cadastrar usuario
            while True:
                cadastrar_usuario()
                continuar = input('\nDeseja cadastrar outro usuario? [\033[1;32mS\033[m/\033[1;32mN\033[m]: ').upper().strip()
                while validar_s_n(continuar) is False: # Validação da entrada
                    continuar = input('Entrada inválida selecione [\033[1;32mS\033[m/\033[1;32mN\033[m]: ').upper().strip()
                if continuar == 'S': continue
                else: break

            

        elif choice == 2: # Fazer Login
            fazer_login()

        elif choice == 0: # Sair
            break

        continuar = input('\nDeseja voltar ao menu inicial? [\033[1;32mS\033[m/\033[1;32mN\033[m]: ').upper().strip()

        while validar_s_n(continuar) is False: # Validação da entrada
            continuar = input('Entrada inválida selecione [\033[1;32mS\033[m/\033[1;32mN\033[m]: ').upper().strip()
        
        if continuar == 'S':
            pass
        else:
            loop = 'Off'
            break