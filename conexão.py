from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Criar banco de dados e tabela
def criar_tabela():
    conn = sqlite3.connect("formulario.db")
    cursor = conn.cursor()  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            cep TEXT NOT NULL,
            numero_nota TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            data_da_compra TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

criar_tabela()  # Executa a criação da tabela ao iniciar o servidor

# Rota única para exibir o formulário e processar os dados
@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        try:
            dados = request.form  # Captura os dados do formulário
            print("Dados recebidos:", dados)  # Debug no terminal

            # Conectar ao banco e inserir os dados
            conn = sqlite3.connect("formulario.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO clientes (nome, data_nascimento, cpf, telefone, email, endereco, cidade, estado, cep, numero_nota, cnpj, data_da_compra) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                dados["nome"], dados["data_nascimento"], dados["cpf"], dados["telefone"], dados["email"],
                dados["endereco"], dados["cidade"], dados["estado"], dados["cep"], dados["numero_nota"],
                dados["cnpj"], dados["data_da_compra"]
            ))

            conn.commit()
            conn.close()
            return "Formulário enviado com sucesso!"

        except Exception as e:
            print("Erro ao inserir no banco:", str(e))
            return "Erro ao enviar o formulário!", 500

    return render_template("index.html")  # Renderiza o HTML do formulário

if __name__ == "__main__":
    app.run(debug=True)
