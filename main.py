from sys import exit
import funcoes  # from funcoes import *

usuarios = {
    "admin": {"nome": "rich", "senha": "12345"},
    }

print("-=-=-=-SISTEMA_RICH-=-=-=-=")
while True:
    logadm = str(input("LOGIN: \n")).lower().strip()
    senhadm = str(input("SENHA: \n")).lower().strip()

    if (logadm in usuarios and senhadm == usuarios[logadm]["senha"]):
        while True:
            funcoes.limpa_tela()
            print("""-=-=-=-SISTEMA_RICH-=-=-=-=
[1] Adicionar usuário
[2] Remover
[3] Pesquisar
[4] Listar
[5] Sair
            """)
            opcao = int(input("-> "))

            match opcao:
                case 1:
                    funcoes.add_usuario(usuarios)
                case 2:
                    funcoes.remover(usuarios,logadm)
                case 3:
                    funcoes.pesquisar(usuarios)
                case 4:
                    funcoes.listar(usuarios)
                case 5:
                    print("Concluído.")
                    exit()  # ou break
                case _:
                    print("Inválido.")
                    input("Presione para retornar")
                    continue
    else:
        print("Usuário ou senha incorreto.\n")
        continue
