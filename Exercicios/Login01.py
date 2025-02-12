usuarios = []
apelidos = []
senhas = []

def cadastro():
    usuarios.append(input('Escolha o usuário: '))
    apelidos.append(input('Escolha seu apelido: '))
    senha=(input('Crie uma senha: '))
    while(len(senha)<=7):
        print('Sua senha é muito curta')
        senha=input('Crie uma senha mais forte com pelo menos 8 dígitos ')
    senhas.append(senha)
    print('Cadastro concluído com sucesso')
    inicio()
def login():
    global usuario
    tentativas = 0
    while(tentativas<3):
        usuario = input('Digite seu usuário: ')
        senha_login = input('Digite sua senha: ')
        if (usuario not in usuarios):
            print('Esse usuario não existe, tente novamente ou realize o cadastro')
            inicio()
        if(senha_login not in senhas):
          print('A senha está incorreta tente novamente')
          tentativas+=1
          continue
        
        if(usuarios.index(usuario) == senhas.index(senha_login)):
            print('Bem vindo'+apelidos[usuarios.index(usuario)])
            break
    if (tentativas ==3):
        print('Você excedeu as tentivas, usuário bloqueado')
        usuarios.remove(usuario)
        senhas.pop(usuarios.index(usuario))
def inicio():
    opção = input('Deseja realizar o login ou o cadastro? ')
    if (opção == "login" or opção == "Login"):
        login()
    elif(opção == "cadastro" or opção == "Cadastro"):
        cadastro()
    else:
        print('Essa opção é invalida, tente novamente')
        inicio()
print('Bem vindo')
inicio()
