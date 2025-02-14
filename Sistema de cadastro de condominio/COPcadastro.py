import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="condvilaana"
    )

    cursor = conn.cursor(prepared=True)

    def cadastro_condominos():
        undadm = input('Digite a unidade administrativa: ')
        cpf = input('Digite o CPF: ')
        nome = input('Digite o nome do condômino:')
        
        query = "SELECT * FROM administradores WHERE undadm = %s"
        cursor.execute(query, (undadm,))
        result = cursor.fetchall()

        uadmin = "0"
        if not result:
            while True:
                admin = input('É o administrador da unidade? (Digite "Sim" ou "Não"): ')
                if admin.lower() in ["sim", "não", "nao"]:
                    uadmin = "1" if admin.lower() == "sim" else "0"
                    print(uadmin)
                    break
                else:
                    print("Entrada inválida! Digite 'Não' para Não ou 'Sim' para Sim.")
        
        insert_condominos_query = "INSERT INTO condominos (undadm, cpf, nome, uadmin) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_condominos_query, (undadm, cpf, nome, uadmin))
        
        if uadmin == '1':
            insert_admin_query = """
            INSERT INTO administradores (undadm, nome, cpf, bloco, apto) 
            SELECT c.undadm, c.nome, c.cpf, u.bloco, u.apto 
            FROM condominos c 
            JOIN undcond u ON c.undadm = u.id 
            WHERE c.undadm = %s AND c.cpf = %s
            """
            cursor.execute(insert_admin_query, (undadm, cpf))
        
        conn.commit()
        print('Cadastro realizado com sucesso!')

    cadastro_condominos()

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL encerrada.")
