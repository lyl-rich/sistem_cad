import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    limpa_tela()

    print("""
[1] Adicionar usuário
[2] Remover
[3] Pesquisar
[4] Listar
[5] Sair
    """)
    opcao = int(input("-> "))
    return opcao

#

def add_usuario(usuarios):
    while True:
        limpa_tela()
        print("-=-=-=-ADICIONAR_USUÁRIO-=-=-=-=")

        print("[0] - Cancelar")
        nv_usuario = input("\nNovo login:\n").lower().strip()

        if nv_usuario == '0': return

        usuarios[nv_usuario] = {
            "senha": input("Senha:\n").lower().strip(),
            "nome": input("Nome:\n").title().strip()
            }
        
        #print(usuarios)    conferir
        print("\nADICIONADO!")

        rep = input("\n[press] - Adicionar outro\n[1] - Voltar\n-> ")
        if rep == '1': return

#

def remover(usuarios,logadm):
    while True:
        limpa_tela()
        print("-=-=-=-REMOVER_USUÁRIO-=-=-=-=")
        print("[0] - Cancelar")

        remover = input("\nRemover: ").lower().strip()
        if remover == '0': return

        if remover in usuarios and remover != logadm:
            del usuarios[remover]
            #print(usuarios)    conferir
            print(f"'{remover}' REMOVIDO(A)!\n")
        else:
            print("Erro, usuário não encontrado ou restrito.")

        rep = input("\n[press] - Remover outro\n[1] - Voltar\n-> ")
        if rep == '1': return

#

def pesquisar(usuarios):
        while True:
            limpa_tela()
            print("-=-=-=-BUSCAR_USUÁRIO-=-=-=-=")
            print("[0] - Cancelar")

            user_buscado = input("\nPesquisar: ").lower().strip()
            if user_buscado == '0': return

            if user_buscado in usuarios:
                print("\nUSUÁRIO ENCONTRADO!")
                print(f"""
    Login: {user_buscado}
    Nome: {usuarios[user_buscado]["nome"]}
    Senha: {usuarios[user_buscado]["senha"]}
                """)
            else:
                print("Erro, usuário não encontrado.")

            rep = input("\n[press] - Buscar outro\n[1] - Voltar\n-> ")
            if rep == '1': return

#

def listar(usuarios):
    limpa_tela()
    print("-=-=-=-LISTA_USUÁRIOS-=-=-=-=")

    print(f"\n{'Nome':10}", f"{'Login':10}", 'Senha', sep=" | ")
    print('-' *35)

    for key,dado in usuarios.items():
        print(f"{dado['nome']:10}", f"{key:10}", dado['senha'], sep=" | ")

        '''print(f"""
    Nome: {dado["nome"]}
    Login: {key}
    Senha: {dado["senha"]}""")'''

    input("\nPressione para voltar.")
    