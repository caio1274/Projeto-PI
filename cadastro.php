<?php
require_once "config.php";

$erro = "";
$sucesso = "";

// Verifica se o formulário foi enviado
if(isset($_POST['email']) && isset($_POST['senha'])){
    $email = trim($_POST['email']);
    $senha = trim($_POST['senha']);

    // Verifica se já existe o usuário
    $sql_check = "SELECT * FROM usuarios WHERE email='$email'";
    $resultado_check = $conexao->query($sql_check);

    if($resultado_check && $resultado_check->num_rows > 0){
        $erro = "Este email já está cadastrado!";
    } else {
        // Insere o usuário com senha em texto puro
        $sql = "INSERT INTO usuarios (email, senha) VALUES ('$email', '$senha')";
        if($conexao->query($sql)){
            $sucesso = "Cadastro realizado com sucesso! Agora você pode fazer login.";
        } else {
            $erro = "Erro ao cadastrar: " . $conexao->error;
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cadastro | Calmind</title>
<link rel="stylesheet" href="css/login.css">
</head>
<body>

<div class="login-page">
    <div class="login-box">
        <img src="Imagens-logo/LOGO.png" alt="Logo" class="logo">
        <h2>Cadastre-se</h2>

        <!-- Mensagem de erro -->
        <?php if(!empty($erro)) : ?>
            <div style="color:red; margin-bottom:10px;"><?php echo $erro; ?></div>
        <?php endif; ?>

        <!-- Mensagem de sucesso -->
        <?php if(!empty($sucesso)) : ?>
            <div style="color:green; margin-bottom:10px;"><?php echo $sucesso; ?></div>
        <?php endif; ?>

        <!-- Formulário de cadastro -->
        <form method="POST" action="">
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="senha" placeholder="Senha" required>
            <button type="submit">Cadastrar</button>
        </form>

        <p>Já tem conta? <a href="login.php">Faça login</a></p>
    </div>
</div>

</body>
</html>
