from sys import exit
import funcoes

usuarios = {
    "admin": {"nome": "rich", "senha": "12345"},
    "will": {"nome": "Willame", "senha": "09876"},
    "dani": {"nome": "Daniel", "senha": "dnl3456"},
    "joaozin": {"nome": "Joao", "senha": "20212"},
    }

print("-=-=-=-SISTEMA_RICH-=-=-=-=")
while True:
    logadm = str(input("LOGIN: \n")).lower().strip()
    senhadm = str(input("SENHA: \n")).lower().strip()

    if (logadm in usuarios and senhadm == usuarios[logadm]["senha"]):
        while True:
            opcao = funcoes.menu()
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
                    exit()
                case _:
                    print("Inválido.")
                    input("Presione para retornar")
                    continue
    else:
        print("Usuário ou senha incorreto.\n")
        continue