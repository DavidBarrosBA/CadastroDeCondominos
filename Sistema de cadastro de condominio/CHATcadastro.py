import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="condvilaana"
)
cursor = conn.cursor()

def cadastro_condominos():
    undadm = input('Digite a unidade administrativa: ').strip()
    cpf = input('Digite o CPF: ').strip()
    nome = input('Digite o nome do condômino: ').strip()

    # Verifica se a unidade já possui um administrador
    cursor.execute("SELECT 1 FROM administradores WHERE undadm = %s", (undadm,))
    existe_admin = cursor.fetchone() is not None

    # Determina se o usuário será administrador
    uadmin = "0"
    if not existe_admin:
        while True:
            admin = input('É o administrador da unidade? (Sim/Não): ').strip().lower()
            if admin in ["sim", "não", "nao"]:
                uadmin = "1" if admin == "sim" else "0"
                break
            else:
                print("Entrada inválida! Digite 'Sim' ou 'Não'.")

    # Insere o novo condômino
    cursor.execute(
        "INSERT INTO condominos (undadm, cpf, nome, uadmin) VALUES (%s, %s, %s, %s)",
        (undadm, cpf, nome, uadmin)
    )

    # Se for administrador, adiciona na tabela de administradores
    if uadmin == "1":
        cursor.execute("""
            INSERT INTO administradores (undadm, nome, cpf, bloco, apto)
            SELECT c.undadm, c.nome, c.cpf, u.bloco, u.apto 
            FROM condominos c 
            JOIN undcond u ON c.undadm = u.id 
            WHERE c.undadm = %s AND c.cpf = %s
        """, (undadm, cpf))

    conn.commit()
    print('Cadastro realizado com sucesso!')

cadastro_condominos()
