import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="condvilaana"
)

cursor = conn.cursor()  

def cadastro_condominos():
    undadm = input('Digite a unidade administrativa: ')
    cpf = input('Digite o CPF: ')
    nome = input('Digite o nome do condômino:')
       
    cursor.execute(f"SELECT * FROM administradores WHERE undadm = '{undadm}'")
    result = cursor.fetchall()
    
    if not result:
        while True:
            admin = input('É o administrador da unidade?:')
            if admin in ["Sim", 'sim', "não", 'Nao', 'nao', "Não"]:
                if admin == "Sim" or admin == "sim":
                    uadmin = "1"
                else:
                    uadmin = "0"
                print(uadmin)       
                break
            else:
                print("Entrada inválida! Digite 'Não' para Não ou 'Sim' para Sim.")
    else:
        uadmin = "0"
             
    
    
   

    cursor.execute(f"INSERT INTO condominos (undadm, cpf, nome, uadmin) VALUES ('{undadm}', '{cpf}', '{nome}', '{uadmin}')")
    
    if uadmin == '1':
       cursor.execute(f"INSERT INTO administradores (undadm, nome, cpf, bloco, apto) SELECT c.undadm, c.nome, c.cpf, u.bloco, u.apto FROM condominos c JOIN undcond u ON c.undadm = u.id WHERE c.undadm = {undadm} and c.cpf = {cpf} ;")
    conn.commit()
    print('Cadastro realizado com sucesso!')
cadastro_condominos()   