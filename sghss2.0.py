import mariadb
import getpass

def conectar_bd():
    try:
        return mariadb.connect(
            host='localhost',
            user='root',
            password='procure_o_admin_para_senha',
            database='sghss'
        )
    except mariadb.Error as e:
        print(f"Erro ao conectar: {e}")
        exit(1)

def menu_principal():
    while True:
        print("\n=== SGHSS - Sistema de Gestão Hospitalar ===")
        print("1 - Administrador")
        print("2 - Paciente")
        print("3 - Profissional")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            menu_administrador()
        elif opcao == '2':
            menu_paciente()
        elif opcao == '3':
            menu_profissional()
        elif opcao == '0':
            print("✅ Sistema Encerrado.")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente!")

def menu_administrador():
    while True:
        print("\n=== Menu Administrador ===")
        print("1 - Cadastrar Leito")
        print("2 - Listar Leitos")
        print("3 - Cadastrar Suprimento")
        print("4 - Listar Suprimentos")
        print("5 - Alterar Suprimento")
        print("6 - Listar Agenda dos Profissionais")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            cadastrar_leito()
        elif opcao == '2':
            listar_leitos()
        elif opcao == '3':
            cadastrar_suprimento()
        elif opcao == '4':
            listar_suprimentos()
        elif opcao == '5':
            alterar_suprimento()
        elif opcao == '6':
            listar_agenda_profissionais()
        elif opcao == '0':
            break
        else:
            print("⚠️ Opção inválida. Tente novamente!")

def menu_paciente():
    while True:
        print("\n=== Menu Paciente ===")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Agendar Consulta")
        print("5 - Excluir Consulta")
        print("6 - Listar Consultas do Paciente")
        print("7 - Listar Receita Digital do Paciente")
        print("8 - Listar Prontuário do Paciente")
        print("9 - Listar Leitos")
        print("10 - Ocupar Leito")
        print("11 - Desocupar Leito")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            alterar_paciente()
        elif opcao == '4':
            agendar_consulta()
        elif opcao == '5':
            excluir_consulta()
        elif opcao == '6':
            listar_consultas_paciente()
        elif opcao == '7':
            listar_receita_digital_paciente()
        elif opcao == '8':
            listar_prontuario_paciente()
        elif opcao == '9':
            listar_leitos()
        elif opcao == '10':
            ocupar_leito()
        elif opcao == '11':
            desocupar_leito()
        elif opcao == '0':
            break
        else:
            print("⚠️ Opção inválida. Tente novamente!")

def menu_profissional():
    while True:
        print("\n=== Menu Profissional ===")
        print("1 - Cadastrar Prontuário")
        print("2 - Cadastrar Receita Digital")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            cadastrar_prontuario()
        elif opcao == '2':
            cadastrar_receita_digital()
        elif opcao == '0':
            break
        else:
            print("⚠️ Opção inválida. Tente novamente!")

# Exemplo de placeholder das funções
def cadastrar_leito():
    conn = conectar_bd()
    cursor = conn.cursor()
    numero = input("Número do Leito: ")
    status = input("Status do Leito (Disponível/Ocupado): ")
    try:
        cursor.execute("INSERT INTO Leito (numero, status) VALUES (?, ?)", (numero, status))
        conn.commit()
        print("✅ Leito cadastrado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao cadastrar leito: {e}")
    finally:
        conn.close()

def listar_leitos():
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, numero, status FROM Leito")
        for leito in cursor.fetchall():
            print(f"ID: {leito[0]}, Número: {leito[1]}, Status: {leito[2]}")
    except mariadb.Error as e:
        print(f"Erro ao listar leitos: {e}")
    finally:
        conn.close()

def cadastrar_suprimento():
    conn = conectar_bd()
    cursor = conn.cursor()
    nome = input("Nome do Suprimento: ")
    quantidade = input("Quantidade: ")
    try:
        cursor.execute("INSERT INTO Suprimento (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        print("✅ Suprimento cadastrado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao cadastrar suprimento: {e}")
    finally:
        conn.close()

def listar_suprimentos():
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nome, quantidade FROM Suprimento")
        for sup in cursor.fetchall():
            print(f"ID: {sup[0]}, Nome: {sup[1]}, Quantidade: {sup[2]}")
    except mariadb.Error as e:
        print(f"Erro ao listar suprimentos: {e}")
    finally:
        conn.close()

def alterar_suprimento():
    conn = conectar_bd()
    cursor = conn.cursor()
    id_sup = input("ID do Suprimento a alterar: ")
    nova_quantidade = input("Nova quantidade: ")
    try:
        cursor.execute("UPDATE Suprimento SET quantidade = ? WHERE id = ?", (nova_quantidade, id_sup))
        conn.commit()
        print("✅ Suprimento atualizado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao alterar suprimento: {e}")
    finally:
        conn.close()

def listar_agenda_profissionais():
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT p.nome, p.especialidade, c.data, c.hora, pa.nome
            FROM Profissional p
            JOIN Consulta c ON p.id = c.profissionalId
            JOIN Paciente pa ON c.pacienteId = pa.id
            ORDER BY p.nome, c.data, c.hora
        """)
        resultados = cursor.fetchall()

        if resultados:
            print("\n=== Consultas Agendadas por Profissional ===")
            for linha in resultados:
                print(f"Profissional: {linha[0]} | Especialidade: {linha[1]} | Data: {linha[2]} | Hora: {linha[3]} | Paciente: {linha[4]}")
        else:
            print("Nenhuma consulta agendada.")
    except mariadb.Error as e:
        print(f"Erro ao buscar consultas dos profissionais: {e}")
    finally:
        conn.close()


def cadastrar_paciente():
    conn = conectar_bd()
    cursor = conn.cursor()
    nome = input("Nome do paciente: ")
    cpf = input("CPF (somente números): ")
    data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    try:
        cursor.execute("""
            INSERT INTO Paciente (nome, cpf, dataNascimento, telefone, endereco)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, cpf, data_nascimento, telefone, endereco))
        conn.commit()
        print("✅ Paciente cadastrado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao cadastrar paciente: {e}")
    finally:
        conn.close()

def listar_pacientes():
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nome, cpf, dataNascimento, telefone, endereco FROM Paciente")
        pacientes = cursor.fetchall()
        if pacientes:
            print("\n=== Lista de Pacientes ===")
            for p in pacientes:
                print(f"ID: {p[0]} | Nome: {p[1]} | CPF: {p[2]} | Nascimento: {p[3]} | Telefone: {p[4]} | Endereço: {p[5]}")
        else:
            print("Nenhum paciente cadastrado.")
    except mariadb.Error as e:
        print(f"Erro ao listar pacientes: {e}")
    finally:
        conn.close()

def alterar_paciente():
    conn = conectar_bd()
    cursor = conn.cursor()
    paciente_id = input("ID do paciente para alterar: ")
    novo_telefone = input("Novo telefone: ")
    novo_endereco = input("Novo endereço: ")
    try:
        cursor.execute("""
            UPDATE Paciente SET telefone = ?, endereco = ? WHERE id = ?
        """, (novo_telefone, novo_endereco, paciente_id))
        conn.commit()
        print("✅ Dados do paciente alterado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao alterar paciente: {e}")
    finally:
        conn.close()

def agendar_consulta():
    conn = conectar_bd()
    cursor = conn.cursor()

    listar_pacientes()
    paciente_id = input("\nInforme o ID do paciente: ")

    # Exibe os profissionais para o paciente escolher
    cursor.execute("SELECT id, nome, especialidade FROM Profissional")
    profissionais = cursor.fetchall()
    print("\n=== Profissionais Disponíveis ===")
    for prof in profissionais:
        print(f"ID: {prof[0]} | Nome: {prof[1]} | Especialidade: {prof[2]}")

    profissional_id = input("\nInforme o ID do profissional: ")
    data = input("Data da consulta (AAAA-MM-DD): ")
    hora = input("Hora da consulta (HH:MM): ")

    try:
        cursor.execute("""
            INSERT INTO Consulta (data, hora, pacienteId, profissionalId)
            VALUES (?, ?, ?, ?)
        """, (data, hora, paciente_id, profissional_id))
        conn.commit()
        print("✅ Consulta agendada com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao agendar consulta: {e}")
    finally:
        conn.close()

def excluir_consulta():
    conn = conectar_bd()
    cursor = conn.cursor()
    consulta_id = input("Informe o ID da consulta que deseja excluir: ")
    try:
        cursor.execute("DELETE FROM Consulta WHERE id = ?", (consulta_id,))
        conn.commit()
        print("✅ Consulta excluída com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao excluir consulta: {e}")
    finally:
        conn.close()

def listar_consultas_paciente():
    conn = conectar_bd()
    cursor = conn.cursor()
    paciente_id = input("Informe o ID do paciente: ")
    try:
        cursor.execute("""
            SELECT c.id, c.data, c.hora, p.nome 
            FROM Consulta c
            JOIN Profissional p ON c.profissionalId = p.id
            WHERE c.pacienteId = ?
            ORDER BY c.data, c.hora
        """, (paciente_id,))
        consultas = cursor.fetchall()
        if consultas:
            print("\n=== Consultas do Paciente ===")
            for c in consultas:
                print(f"ID Consulta: {c[0]} | Data: {c[1]} | Hora: {c[2]} | Profissional: {c[3]}")
        else:
            print("Nenhuma consulta encontrada.")
    except mariadb.Error as e:
        print(f"Erro ao listar consultas: {e}")
    finally:
        conn.close()

def listar_receita_digital_paciente():
    conn = conectar_bd()
    cursor = conn.cursor()
    paciente_id = input("Informe o ID do paciente: ")
    try:
        cursor.execute("""
            SELECT r.id, r.data, r.conteudo 
            FROM ReceitaDigital r
            JOIN Consulta c ON r.consultaId = c.id
            WHERE c.pacienteId = ?
        """, (paciente_id,))
        receitas = cursor.fetchall()
        if receitas:
            print("\n=== Receitas Digitais do Paciente ===")
            for r in receitas:
                print(f"ID Receita: {r[0]} | Data: {r[1]} | Conteúdo: {r[2]}")
        else:
            print("Nenhuma receita digital encontrada.")
    except mariadb.Error as e:
        print(f"Erro ao listar receitas digitais: {e}")
    finally:
        conn.close()

def listar_prontuario_paciente():
    conn = conectar_bd()
    cursor = conn.cursor()
    paciente_id = input("Informe o ID do paciente: ")
    try:
        cursor.execute("""
            SELECT pr.id, pr.descricao 
            FROM Prontuario pr
            JOIN Consulta c ON pr.consultaId = c.id
            WHERE c.pacienteId = ?
        """, (paciente_id,))
        prontuarios = cursor.fetchall()
        if prontuarios:
            print("\n=== Prontuário do Paciente ===")
            for pr in prontuarios:
                print(f"ID: {pr[0]} | Descrição: {pr[1]}")
        else:
            print("Nenhum prontuário encontrado.")
    except mariadb.Error as e:
        print(f"Erro ao listar prontuário: {e}")
    finally:
        conn.close()

def ocupar_leito():
    conn = conectar_bd()
    cursor = conn.cursor()

    listar_pacientes()
    paciente_id = input("\nInforme o ID do paciente: ")

    # Lista leitos disponíveis
    cursor.execute("SELECT id, numero FROM Leito WHERE status = 'Disponível'")
    leitos = cursor.fetchall()

    if not leitos:
        print("⚠️ Nenhum leito disponível no momento.")
        conn.close()
        return

    print("\n=== Leitos Disponíveis ===")
    for leito in leitos:
        print(f"ID: {leito[0]} | Número: {leito[1]}")

    leito_id = input("\nInforme o ID do leito a ocupar: ")
    try:
        cursor.execute("INSERT INTO OcupadoPor (idPaciente, idLeito) VALUES (?, ?)", (paciente_id, leito_id))
        cursor.execute("UPDATE Leito SET status = 'Ocupado' WHERE id = ?", (leito_id,))
        conn.commit()
        print("✅ Leito ocupado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao ocupar leito: {e}")
    finally:
        conn.close()

def desocupar_leito():
    conn = conectar_bd()
    cursor = conn.cursor()

    paciente_id = input("Informe o ID do paciente para desocupar o leito: ")
    try:
        cursor.execute("SELECT idLeito FROM OcupadoPor WHERE idPaciente = ?", (paciente_id,))
        resultado = cursor.fetchone()

        if resultado:
            leito_id = resultado[0]
            cursor.execute("DELETE FROM OcupadoPor WHERE idPaciente = ?", (paciente_id,))
            cursor.execute("UPDATE Leito SET status = 'Disponível' WHERE id = ?", (leito_id,))
            conn.commit()
            print("✅ Leito desocupado com sucesso!")
        else:
            print("⚠️ O paciente não ocupa nenhum leito.")
    except mariadb.Error as e:
        print(f"Erro ao desocupar leito: {e}")
    finally:
        conn.close()

def cadastrar_prontuario():
    conn = conectar_bd()
    cursor = conn.cursor()

    # Listar consultas para selecionar
    cursor.execute("""
        SELECT c.id, p.nome, c.data, c.hora
        FROM Consulta c
        JOIN Paciente p ON c.pacienteId = p.id
    """)
    consultas = cursor.fetchall()
    if not consultas:
        print("⚠️ Nenhuma consulta encontrada para adicionar o prontuário.")
        conn.close()
        return

    print("\n=== Consultas Disponíveis ===")
    for c in consultas:
        print(f"ID Consulta: {c[0]} | Paciente: {c[1]} | Data: {c[2]} | Hora: {c[3]}")

    consulta_id = input("\nInforme o ID da consulta: ")
    descricao = input("Descrição do prontuário: ")

    try:
        cursor.execute("""
            INSERT INTO Prontuario (descricao, consultaId)
            VALUES (?, ?)
        """, (descricao, consulta_id))
        conn.commit()
        print("✅ Prontuário cadastrado com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao cadastrar prontuário: {e}")
    finally:
        conn.close()

def cadastrar_receita_digital():
    conn = conectar_bd()
    cursor = conn.cursor()

    # Listar consultas para vincular a receita
    cursor.execute("""
        SELECT c.id, p.nome, c.data, c.hora
        FROM Consulta c
        JOIN Paciente p ON c.pacienteId = p.id
    """)
    consultas = cursor.fetchall()
    if not consultas:
        print("⚠️ Nenhuma consulta encontrada para gerar receita.")
        conn.close()
        return

    print("\n=== Consultas Disponíveis ===")
    for c in consultas:
        print(f"ID Consulta: {c[0]} | Paciente: {c[1]} | Data: {c[2]} | Hora: {c[3]}")

    consulta_id = input("\nInforme o ID da consulta: ")
    data = input("Data da receita (AAAA-MM-DD): ")
    conteudo = input("Conteúdo da receita: ")

    try:
        cursor.execute("""
            INSERT INTO ReceitaDigital (data, conteudo, consultaId)
            VALUES (?, ?, ?)
        """, (data, conteudo, consulta_id))
        conn.commit()
        print("✅ Receita digital cadastrada com sucesso!")
    except mariadb.Error as e:
        print(f"Erro ao cadastrar receita digital: {e}")
    finally:
        conn.close()

# Função para autenticar o usuário
def autenticar_usuario():
    conn = conectar_bd()
    cursor = conn.cursor()

    login = input("Login: ")
    senha = getpass.getpass("Senha: ")

    try:
        cursor.execute("""
            SELECT id FROM Usuario WHERE login = ? AND senha = ?
        """, (login, senha))
        usuario = cursor.fetchone()

        if usuario:
            print("✅ Acesso autorizado. Bem-vindo ao SGHSS!")
            return True
        else:
            print("❌ Login ou senha inválidos.")
            return False
    except mariadb.Error as e:
        print(f"Erro na autenticação: {e}")
        return False
    finally:
        conn.close()

# Executar o sistema
if __name__ == "__main__":
    if autenticar_usuario():
        menu_principal()
    else:
        print("Encerrando o sistema por falha na autenticação.")
