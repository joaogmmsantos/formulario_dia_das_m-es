import express from "express";
import sqlite3 from "sqlite3";
import { open } from "sqlite";
import cors from "cors";

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

async function getDbConnection() {
  return open({
    filename: "./database.db",
    driver: sqlite3.Database,
  });
}

// Criar tabela se não existir
(async () => {
  const db = await getDbConnection();
  await db.exec(`CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    endereco TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    cep TEXT NOT NULL,
    numero_nota TEXT NOT NULL,
    cnpj TEXT NOT NULL,
    data_da_compra TEXT NOT NULL
  )`);
})();

// Rota para receber os dados do formulário e salvar no banco
app.post("/api/usuarios", async (req, res) => {
  const {
    nome, data_nascimento, cpf, telefone, email, endereco, cidade,
    estado, cep, numero_nota, cnpj, data_da_compra
  } = req.body;

  try {
    const db = await getDbConnection();
    await db.run(
      "INSERT INTO usuarios (nome, data_nascimento, cpf, telefone, email, endereco, cidade, estado, cep, numero_nota, cnpj, data_da_compra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
      [nome, data_nascimento, cpf, telefone, email, endereco, cidade, estado, cep, numero_nota, cnpj, data_da_compra]
    );
    res.status(201).json({ message: "Usuário cadastrado com sucesso" });
  } catch (error) {
    res.status(500).json({ error: "Erro ao cadastrar usuário", details: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
