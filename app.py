from functions import mostrar_menu, validar_s_n, escolher_menu, salvar_usuario, cadastrar_usuario, fazer_login

def loop(loop='On'):
    while loop == 'On':
        mostrar_menu()
        choice = escolher_menu()
        if choice == 1:
            username_prompt, senha_prompt = cadastrar_usuario()
            salvar_usuario(username=username_prompt, senha=senha_prompt)
            cadastrar_outro = input('Deseja cadastrar outro usuario? [S/N]: ').upper().strip()
            validacao = validar_s_n(cadastrar_outro)
            while validacao is False: # Validação da entrada
                cadastrar_outro = input('Entrada inválida selecione [S/N]: ').upper().strip()
                validacao = validar_s_n(cadastrar_outro)

        elif choice == 2:
            fazer_login()
        elif choice == 0:
            break
        continuar = input('\nDeseja voltar ao menu inicial? [S/N]: ').upper().strip()
        validacao = validar_s_n(continuar)

        while validacao is False: # Validação da entrada
            continuar = input('Entrada inválida selecione [S/N]: ').upper().strip()
            validacao = validar_s_n(continuar)
        
        if continuar == 'S':
            pass
        else:
            loop = 'Off'
            break