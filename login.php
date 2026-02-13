<?php
require_once "config.php"; // arquivo de conexão com o banco

$erro = "";

// Verifica se o formulário foi enviado
if(isset($_POST['email']) && isset($_POST['senha'])){
    $email = trim($_POST['email']);
    $senha = trim($_POST['senha']);

    // Busca usuário com email e senha **como texto puro**
    $sql = "SELECT * FROM usuarios WHERE email='$email' AND senha='$senha'";
    $resultado = $conexao->query($sql);

    if($resultado && $resultado->num_rows > 0){
        // Login correto
        header("Location: LiaIA.html"); // redireciona para página principal
        exit();
    } else {
        $erro = "Email ou senha incorretos!";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Conecte-se | Calmind</title>
<link rel="stylesheet" href="css/login.css">
</head>
<body>

<div class="login-page">
    <div class="login-box">
        <img src="Imagens-logo/LOGO.png" alt="Logo" class="logo">
        <h2>Conecte-se</h2>

        <!-- Mostra mensagem de erro -->
        <?php if(!empty($erro)) : ?>
            <div style="color:red; margin-bottom:10px;"><?php echo $erro; ?></div>
        <?php endif; ?>

        <!-- Formulário de login -->
        <form method="POST" action="">
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="senha" placeholder="Senha" required>
            <button type="submit">Entrar</button>
        </form>

        <p>Não tem conta? <a href="cadastro.php">Cadastre-se</a></p>
    </div>
</div>

</body>
</html>
