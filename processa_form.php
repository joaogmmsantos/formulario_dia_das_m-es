<?php
// Conectar ao banco de dados SQLite
$db = new SQLite3('formulario.db');

// Criar tabela se não existir
$query = "CREATE TABLE IF NOT EXISTS clientes (
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
)";
$db->exec($query);

// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Pega os dados do formulário
    $nome = $_POST['nome'];
    $data_nascimento = $_POST['data_nascimento'];
    $cpf = $_POST['cpf'];
    $telefone = $_POST['telefone'];
    $email = $_POST['email'];
    $endereco = $_POST['endereco'];
    $cidade = $_POST['cidade'];
    $estado = $_POST['estado'];
    $cep = $_POST['cep'];
    $numero_nota = $_POST['numero_nota'];
    $cnpj = $_POST['cnpj'];
    $data_da_compra = $_POST['data_da_compra'];

    // Insere os dados no banco de dados
    $stmt = $db->prepare("INSERT INTO clientes (nome, data_nascimento, cpf, telefone, email, endereco, cidade, estado, cep, numero_nota, cnpj, data_da_compra) 
                          VALUES (:nome, :data_nascimento, :cpf, :telefone, :email, :endereco, :cidade, :estado, :cep, :numero_nota, :cnpj, :data_da_compra)");

    $stmt->bindValue(':nome', $nome, SQLITE3_TEXT);
    $stmt->bindValue(':data_nascimento', $data_nascimento, SQLITE3_TEXT);
    $stmt->bindValue(':cpf', $cpf, SQLITE3_TEXT);
    $stmt->bindValue(':telefone', $telefone, SQLITE3_TEXT);
    $stmt->bindValue(':email', $email, SQLITE3_TEXT);
    $stmt->bindValue(':endereco', $endereco, SQLITE3_TEXT);
    $stmt->bindValue(':cidade', $cidade, SQLITE3_TEXT);
    $stmt->bindValue(':estado', $estado, SQLITE3_TEXT);
    $stmt->bindValue(':cep', $cep, SQLITE3_TEXT);
    $stmt->bindValue(':numero_nota', $numero_nota, SQLITE3_TEXT);
    $stmt->bindValue(':cnpj', $cnpj, SQLITE3_TEXT);
    $stmt->bindValue(':data_da_compra', $data_da_compra, SQLITE3_TEXT);

    if ($stmt->execute()) {
        echo "<script>alert('Formulário enviado com sucesso!'); window.location.href='index.html';</script>";
    } else {
        echo "<script>alert('Erro ao enviar o formulário!'); window.history.back();</script>";
    }
}
?>
